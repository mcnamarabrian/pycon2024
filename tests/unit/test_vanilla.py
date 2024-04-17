import function.vanilla.vanilla as vanilla

import pydantic
import pytest

def test_valid_user(valid_input, lambda_context):
    ret = vanilla.handler(valid_input, lambda_context)
    expected = {
        "status_code": 200,
        "user_id": "brian1",
        "first_name": "Brian",
        "last_name": "McNamara",
        "email": "brian@mcnamara.com"
    }

    assert ret == expected


def test_invalid_user_invalid_email(invalid_input_invalid_email, lambda_context):
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        ret = vanilla.handler(invalid_input_invalid_email, lambda_context)


def test_invalid_user_missing_attribute(invalid_input_invalid_email, lambda_context):
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        ret = vanilla.handler(invalid_input_invalid_email, lambda_context)
