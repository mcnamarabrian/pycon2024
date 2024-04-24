import function.instrumented.instrumented as instrumented
import http

import pydantic
import pytest

def test_valid_user(valid_input, lambda_context):
    ret = instrumented.handler(valid_input, lambda_context)
    expected = {
        "status_code": int(http.HTTPStatus.OK),
        "user_id": "brian1",
        "first_name": "Brian",
        "last_name": "McNamara",
        "email": "brian@mcnamara.com"
    }

    assert ret == expected


def test_invalid_user_invalid_email(invalid_input_invalid_email, lambda_context):
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        ret = instrumented.handler(invalid_input_invalid_email, lambda_context)


def test_invalid_user_missing_attribute(invalid_input_invalid_email, lambda_context):
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        ret = instrumented.handler(invalid_input_invalid_email, lambda_context)
