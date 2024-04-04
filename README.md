# pycon2024

The project is used to support **Supercharging Your AWS Lambda Functions for Fun, Profit, and Chaos**.

## Dependencies

* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

* [Python3.12](https://www.python.org/downloads/)

* [Pipenv](https://pipenv.pypa.io/en/latest/)

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Building and Testing Locally

### Building

```bash
sam build
```

### Testing Locally - Vanilla Function

The following commands can be used to invoke the `VanillaFunction` locally.

```bash
# Valid event
sam local invoke VanillaFunction -e events/valid_user.json

# Invalid event - invalid email address
sam local invoke VanillaFunction -e events/invalid_user_invalid_email.json

# Invalid event - missing field
sam local invoke VanillaFunction -e events/invalid_user_missing_attribute.json
```
