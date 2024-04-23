# pycon2024

The project is used to support [Python Powered Serverless Observability (PyCon US 2024)](https://us.pycon.org/2024/schedule/presentation/149/).

Serverless applications powered by services like [AWS Lambda](https://aws.amazon.com/lambda) allow developers to shift their focus almost exclusively to writing code and delivering value to customers without being overly concerned with server management, resiliency, or capacity planning. There is no question that there are fewer operational requirements but one operational need does not change - the need to understand what is happening in your serverless application!

The need for observability in serverless applications is exactly the same as server-based applications. However, serverless applications require a degree of rigor to properly plan for observability. While there are servers in serverless applications, developers and operators do not have access to them. Traditional, non-scalable techniques of using shell commands like `grep`, `top`, `netstat`, or `free` will not work. Instead, signal sources like logs, metrics, and traces must be used to understand what is happening in our application.

This session explores cloud native and industry standard tooling that can be used by application developers and operators to understand what is happening in their serverless applications. The examples use [AWS Lambda](https://aws.amazon.com/lambda) to illustrate how to take advantage of native integrations as well as industry standard observability mechanisms.

The simple function will receive an event payload that interacts with a simulated user creation service. Each variation of the function will highlight different observability capabilities.

* **VanillaFunction** relies exclusively on native cloud integrations with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for logs and metrics and AWS X-Ray for traces. Data is not enriched in a meaningful way - this is the default experience when integrating with these services.

* **InstrumentedFunction** uses the same native cloud integration with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS X-Ray](https://aws.amazon.com/xray/) but employs techniques to enrich our signals to make them more meaningful for developers and operators.

* **OtelFunction** shifts away from cloud native integration and toward the [OpenTelemetry (OTEL)](https://opentelemetry.io/) industry standard for sending logs, metrics, and traces to a receiver. The application sends data to [Honeycomb](https://honeycomb.io) but this is for illustrative purposes only. Data can be sent to any OTEL-compatible receiver with a simple configuration change.

> :warning: **You may incur charges if you deploy resources to the cloud. Please be aware of your cloud spend by setting up a billing alarm ([AWS example](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)).**

## Dependencies

* [AWS Account](https://console.aws.amazon.com)

* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

* [Python3.12](https://www.python.org/downloads/)

* [Pipenv](https://pipenv.pypa.io/en/latest/)

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

* [Honeycomb](https://www.honeycomb.io/) (Free trial account)

## Installing Python Dependencies

The local testing environment makes use of dependencies in the project's Pipfile. These dependencies can be installed by running the following command:

```bash
make install
```

## Setting Required Shell Variables

Many of the make tasks depend upon several environment variables. Before moving on, set the following environment variables:

```bash
# Can be us-east-1, us-east-2, us-west-2, eu-west-1, or eu-west-2
export AWS_REGION=your-region-value

# The AWS profile you use to interact with AWS APIs locally
export AWS_PROFILE=your-aws-profile

# The name of the CloudFormation stack
export CFN_STACK=pycon2024
```

## Sign Up for a Honeycomb Trial

The OTEL examples in this project emit data to [Honeycomb](https://www.honeycomb.io/). You will need to sign-up for a free trial and record the API key. We will store the Honeycomb API key in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/).

**NOTE**: Honeycomb is used in this example but you can configure AWS Lambda to emit to other OTEL-compatible providers.

### Storing the Honeycomb API in AWS Secrets Manager

The project makes the assumption Honeycomb secrets are stored in the keyspace `pycon2024/honeycomb`. The API key secret is stored with the key `api_key`. The value is your Honeycomb API key. Use the following command to write the API key.

```bash
export HONEYCOMB_SECRET_ARN=$(aws secretsmanager create-secret \
--name pycon2024/honeycomb \
--description "Secret created for Python Powered Serverless Observability (PyCon US 2024)" \
--secret-string "{\"api_key\":\"your-honeycomb-api-key\"}" \
--query "ARN" \
--output text \
--profile $AWS_PROFILE \
--region $AWS_REGION)
```

## What's Next

Now that you have you have your project dependencies installed, you can [build and interact with your functions locally](./README-LOCAL-INTERACTION.md).
