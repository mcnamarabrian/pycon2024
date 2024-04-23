# Deploying to the AWS Cloud

The AWS SAM CLI also allows developers to build and deploy resources to the AWS cloud. In this section, we'll go through the simplified deployment steps using a single `Make` task.

**NOTE:** You must set the environment variables `AWS_PROFILE`, `AWS_REGION`, and `CFN_STACK` in order for the deployment to AWS to be successful. Please see [Setting Required Shell Variables](./README.md) for more detail.

```bash
make deploy
```

The deployment to AWS may take several minutes. Be patient as your resources are created.

## What's Next?

Now that our Lambda functions have been deployed to AWS, let's start examining our observability signals beginning with [**logging**](./README-LOGGING.md).