import json
from uuid import uuid4

import pytest


class MockContext(object):
    def __init__(self, function_name):
        uuid = str(uuid4)
        self.function_name = function_name
        self.function_version = "v$LATEST"
        self.memory_limit_in_mb = 256
        self.invoked_function_arn = (
            f"arn:aws:lambda:us-east-1:123456789012:function:{self.function_name}"
        )
        self.aws_request_id = uuid
        self.log_group_name = f"/aws/lambda/{self.function_name}"
        self.log_stream_name = uuid


@pytest.fixture
def lambda_context():
    return MockContext("dummy_function")


@pytest.fixture
def valid_input():
    """Generate a valid event to create a user"""
    with open("./events/valid_user.json", "r") as fp:
        return json.load(fp)


@pytest.fixture
def invalid_input_invalid_email():
    """Generate invalid event (invalid email)"""
    with open("./events/invalid_user_invalid_email.json", "r") as fp:
        return json.load(fp)


@pytest.fixture
def invalid_input_missing_attribute():
    """Generate invalid event (invalid email)"""
    with open("./events/invalid_user_missing_attribute.json", "r") as fp:
        return json.load(fp)
