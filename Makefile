PIPENV ?= pipenv
AWS_PROFILE := $(shell echo ${AWS_PROFILE})
AWS_REGION := $(shell echo ${AWS_REGION})
HONEYCOMB_SECRET_ARN := $(shell echo ${HONEYCOMB_SECRET_ARN})
CFN_STACK := $(shell echo ${CFN_STACK})

.PHONY: deploy
deploy: local-build
	$(info [*] Deploying to AWS)
	sam deploy --stack-name $$CFN_STACK \
		--tags application=$$CFN_STACK \
		--on-failure ROLLBACK \
		--no-confirm-changeset \
		--parameter-overrides HoneycombSecretsArn=$$HONEYCOMB_SECRET_ARN \
		--resolve-s3 \
		--capabilities CAPABILITY_IAM \
		--region $$AWS_REGION \
		--profile $$AWS_PROFILE

.PHONY: dev
dev:
	$(info [*] Installing project dependencies)
	@$(PIPENV) install --dev

.PHONY: help
help:
	$(info ${HELP_MESSAGE})
	@exit 0

.PHONY: install
install:
	$(info [*] Installing pipenv)
	@pip install pipenv --upgrade
	$(MAKE) dev

.PHONY: lint
lint:
	$(info [*] Linting SAM template)
	sam validate --region $$AWS_REGION --lint

.PHONY: local-build
local-build:
	$(info [*] Performing SAM build)
	sam build

.PHONY: local-instrumented
local-instrumented: local-build
	$(info [*] Invoking InstrumentedFunction)
	sam local invoke --event ./events/valid_user.json InstrumentedFunction

.PHONY: local-otel
local-otel: local-build
	$(info [*] Invoking OtelFunction)
	sam local invoke --event ./events/valid_user.json OtelFunction --region $$AWS_REGION --profile $$AWS_PROFILE

.PHONY: local-vanilla
local-vanilla: local-build
	$(info [*] Invoking VanillaFunction)
	sam local invoke --event ./events/valid_user.json VanillaFunction

.PHONY: remote-instrumented
remote-instrumented:
	$(info [*] Invoking InstrumentedFunction in AWS)
	sam remote invoke --event-file ./events/valid_user.json InstrumentedFunction --stack-name $$CFN_STACK --profile $$AWS_PROFILE --region $$AWS_REGION

.PHONY: remote-otel
remote-otel:
	$(info [*] Invoking OtelFunction in AWS)
	sam remote invoke --event-file ./events/valid_user.json OtelFunction --stack-name $$CFN_STACK --profile $$AWS_PROFILE --region $$AWS_REGION

.PHONY: remote-vanilla
remote-vanilla:
	$(info [*] Invoking VanillaFunction in AWS)
	sam remote invoke --event-file ./events/valid_user.json VanillaFunction --stack-name $$CFN_STACK --profile $$AWS_PROFILE --region $$AWS_REGION

.PHONY: test
test:
	PYTHONPATH="./function/vanilla:./function/instrumented:${PYTHONPATH}" POWERTOOLS_METRICS_NAMESPACE="Pycon2024" POWERTOOLS_TRACE_DISABLED=1 $(PIPENV) run python -m pytest tests/ -vvvv

define HELP_MESSAGE
	Usage: make [target]
		help                   Display help and exit
		deploy                 Deploy AWS Lambda functions to AWS
		install                Install pipenv and local project dependencies
		lint                   Validate and lint SAM template template.yaml
		local-build            Build SAM project locally
		local-instrumented     Build and invoke InstrumentedFunction with valid input
		local-otel             Build and invoke OtelFunction with valid input
		local-vanilla          Build and invoke VanillaFunction with valid input
		remote-instrumented    Invoke InstrumentedFunction with valid input in AWS
		remote-otel            Invoke OtelFunction with valid input in AWS
		remote-vanilla         Invoke VanillaFunction with valid input in AWS
		test                   Unit test the Lambda functions
endef
