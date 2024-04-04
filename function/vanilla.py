import json

from aws_lambda_powertools.utilities.parser import event_parser, BaseModel
from aws_lambda_powertools.utilities.typing import LambdaContext
from pydantic import EmailStr


class User(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email:  EmailStr


@event_parser(model=User)
def handler(event: User, context: LambdaContext) -> dict:
    print(event)

    
