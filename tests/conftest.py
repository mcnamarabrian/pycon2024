import json
from uuid import uuid4

import pytest


class MockContext(object):
    def __init__(self, function_name):
        self.function_name = function_name
        self.function_version = "v$LATEST"
        self.memory_limit_in_mb = 256
        self.invoked_function_arn = (
            f"arn:aws:lambda:us-east-1:123456789012:function:{self.function_name}"
        )
        self.aws_request_id = str(uuid4)


    @pytest.fixture()
    def lambda_context():
        return MockContext("dummy_function")


    @pytest.fixture()
    def valid_input():
        """Generate """


    @pytest.fixture()