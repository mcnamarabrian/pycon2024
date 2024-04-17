PIPENV ?= pipenv


.PHONY: help
help:
	$(info ${HELP_MESSAGE})
	@exit 0

.PHONY: local-build
local-build:
	$(info [*] Performing SAM build)
	sam build

.PHONY: local-instrumented
local-instrumented: local-build
	$(info [*] Invoking InstrumentedFunction)
	sam local invoke --event ./events/valid_user.json InstrumentedFunction

.PHONY: local-vanilla
local-vanilla: local-build
	$(info [*] Invoking VanillaFunction)
	sam local invoke --event ./events/valid_user.json VanillaFunction

.PHONY: test
test:
	PYTHONPATH="./function/vanilla:${PYTHONPATH}" POWERTOOLS_METRICS_NAMESPACE="Pycon2024" POWERTOOLS_TRACE_DISABLED=1 $(PIPENV) run python -m pytest tests/ -vvvv

define HELP_MESSAGE
	Usage: make [target]
		help                   Display help and exit
		local-build            Build SAM project locally
		local-instrumented     Build and invoke InstrumentedFunction with valid input
		local-vanilla          Build and invoke VanillaFunction with valid input
endef
