# Interacting with the Serverless Application Locally

The AWS SAM CLI allows developers to build and test applications locally without the need to deploy resources to the AWS cloud. This allows for faster iterations during development.

## Ensure the SAM Template is Valid and Follows Best Practices

The AWS SAM CLI has the ability to performing linting on your template to make sure it's valid. This is done through the use of [cfn-lint](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/validate-cfn-lint.html) capabilities integrated with the CLI.

## Local Testing

Standard Python tooling can be used to test Lambda applications. You should use standard testing tooling to ensure your application is behaving as expected. You can run the following command to test each Lambda function:

```bash
make test
```

## Building and Invoking Functions Locally

AWS SAM allows us to build and invoke our Lambda functions. Below are the steps for each.

### Building

```bash
make local-build
```

### Invoking Locally

#### VanillaFunction

The following commands can be used to invoke the `VanillaFunction` successfully locally.

```bash
# Valid event
make local-vanilla

# Invalid event - invalid email address
sam local invoke VanillaFunction -e events/invalid_user_invalid_email.json

# Invalid event - missing field
sam local invoke VanillaFunction -e events/invalid_user_missing_attribute.json
```

#### InstrumentedFunction

The following commands can be used to invoke the `InstrumentedFunction` successfully locally.

```bash
# Valid event
make local-instrumented

# Invalid event - invalid email address
sam local invoke InstrumentedFunction -e events/invalid_user_invalid_email.json

# Invalid event - missing field
sam local invoke InstrumentedFunction -e events/invalid_user_missing_attribute.json
```

#### OtelFunction

The following commands can be used to invoke the `OtelFunction` successfully locally.

```bash
# Valid event
make local-otel

# Invalid event - invalid email address
sam local invoke OtelFunction -e events/invalid_user_invalid_email.json

# Invalid event - missing field
sam local invoke OtelFunction -e events/invalid_user_missing_attribute.json
```

## What's Next?

Now that your function is building and invoking locally as expected, let's [deploy our Lambda functions to the AWS cloud](./README-CLOUD-DEPLOY.md).