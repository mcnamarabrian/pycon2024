# Conclusion

Observability signals like logs, metrics, and traces are what allows us as developers and operators to understand the behavior of our applications. The need to observe serverless functions is no different than other applications. For better or worse, not having access to the execution environment forces a degree of rigor. Though initially painful, it's ultimately a good thing.

## Advice

* Log only what you need and nothing more.

* Structure your logs - it will make search and understanding so much easier.

* Keep your logs for as long as your need and no longer. Storing logs has a real cost associated with it.

* Understand the standard metrics available to you from AWS.

* If you need to emit custom metrics use AWS Embedded Metrics Formate (EMF). Avoid using synchronous calls in your functions to create custom metrics.

* Use [Powertools for AWS Lambda (Python)](https://docs.powertools.aws.dev/lambda/python/latest/) - there's a lot of win for observability but there's so much more available.

* Traces are wonderful - you get a lot of value in understanding your distributed application out of the box but know that you can customize traces with annotations and metadata

* If you'd rather use open standards for emitting and collecting observability data you should use OpenTelemetry. There are a lot of open source tools and vendors to explore.


## Resources

* [Powertools for AWS Lambda (Python)](https://docs.powertools.aws.dev/lambda/python/latest/)

* [AWS Lambda Operators Guide - Monitoring and observability](https://docs.aws.amazon.com/lambda/latest/operatorguide/monitoring-observability.html)

* [AWS Distro for OpenTelemetry Lambda Support for Python](https://aws-otel.github.io/docs/getting-started/lambda/lambda-python)

* [OpenTelemetry](https://opentelemetry.io/)

* [OpenTelemetry in Python](https://opentelemetry.io/docs/languages/python)

* [Manual Instrumentation for OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/instrumentation/)


## Thank You

Congrats if you've made it this far!

![Congrats](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3MyazVwNHBlYmMzZWZrZDFqZzdqdGxyc2loMHd2d2RxNGtpZ29pdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QMkPpxPDYY0fu/giphy.gif)
