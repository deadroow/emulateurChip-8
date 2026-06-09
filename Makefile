.PHONY: help run install
.DEFAULT_GOAL := help

PY = .venv/bin/python
ifeq ($(OS),Windows_NT)
    PY = .venv/Scripts/python
endif

help: ## show this help
	@grep -E "^[a-zA-Z_-]+.*: ## .*$$" $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ": ## "}; {printf "$(CYAN_COLOR)%-15s$(NO_COLOR) %s\n", $$1, $$2}'

install: ## installe le venv et les dependances
	@./init.sh

run: ## lance le launcher Gooey, qui lance ensuite l'emulateur
	@$(PY) outils/Explorateur.py