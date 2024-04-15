import http
import os
import random
import sys

from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities.parser import event_parser, BaseModel
from aws_lambda_powertools.utilities.typing import LambdaContext
from pydantic import EmailStr
import requests

MODULES = [
    "requests"
]

logger = Logger()
metrics = Metrics(
    namespace=os.getenv('POWERTOOLS_METRICS_NAMESPACE'),
    service=os.getenv('POWERTOOLS_SERVICE_NAME')
)
tracer = Tracer(patch_modules=MODULES)

class User(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email:  EmailStr


@tracer.capture_method
def submit_user(endpoint: str, payload: dict, context: LambdaContext) -> dict:
    response = {}
    tracer.put_annotation(key='user_id', value=payload.user_id)
    tracer.put_metadata(key='log', value=f'{context.log_group_name}/{context.log_stream_name}')
    tracer.put_metadata(key='request_id', value=f'{context.aws_request_id}')
    try:
        # Imagine if this was a POST to a new user API
        # and we wanted to capture when submissions to the submit_user endpoint
        # were successful and when they were not.
        r = requests.get(endpoint)
        response["status_code"] = r.status_code

        metrics.add_metric(name='SuccessfulSubmission', unit=MetricUnit.Count, value=1)
    except Exception:
        metrics.add_metric(name='UnsuccessfulSubmission', unit=MetricUnit.Count, value=1)
        response["status_code"] = http.HTTPStatus.INTERNAL_SERVER_ERROR
    return response


@metrics.log_metrics
@logger.inject_lambda_context
@tracer.capture_lambda_handler
@event_parser(model=User)
def handler(event: User, context: LambdaContext) -> dict:
    user_id = event.user_id
    first_name = event.first_name
    last_name = event.last_name
    email = event.email

    response = submit_user('https://us.pycon.org/2024/', event, context)
    if response["status_code"] and response["status_code"] == 200:
        logger.info({
            "detail": "submit_user successful",
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        })
        return {
            "status_code": http.HTTPStatus.OK,
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
    else:
        logger.error(f"Could not add user {first_name} {last_name} ({user_id}): {response['status_code']}")
        sys.exit(1)
