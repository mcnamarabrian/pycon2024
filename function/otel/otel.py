import http
import os
import sys

from aws_lambda_powertools import Logger, Metrics
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities.parser import event_parser, BaseModel
from aws_lambda_powertools.utilities.typing import LambdaContext
from pydantic import EmailStr
import requests


logger = Logger()
metrics = Metrics(
    namespace=os.getenv("POWERTOOLS_METRICS_NAMESPACE"),
    service=os.getenv("POWERTOOLS_SERVICE_NAME")
)


class User(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email:  EmailStr


def submit_user(endpoint: str, payload: dict, context: LambdaContext) -> dict:
    response = {}
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
@event_parser(model=User)
def handler(event: User, context: LambdaContext) -> dict:
    user_id = event.user_id
    first_name = event.first_name
    last_name = event.last_name
    email = event.email

    response = submit_user('https://us.pycon.org/2024/', event, context)
    if response.get("status_code") and response.get("status_code") == int(http.HTTPStatus.OK):
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
