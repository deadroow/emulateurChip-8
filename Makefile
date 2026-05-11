.PHONY: help run menu
.DEFAULT_GOAL := help

help: ## show this help
	@grep -E "^[a-zA-Z_-]+.*: ## .*$$" $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ": ## "}; {printf "$(CYAN_COLOR)%-15s$(NO_COLOR) %s\n", $$1, $$2}'

run: ## run the app
	@py main.py

menu: ## show menu
	@./init.sh
