.PHONY: install test lint run

install:
	pip install -r requirements.txt -r requirements-dev.txt

test:
	pytest -q

lint:
	ruff check financial_risk_control

run:
	uvicorn financial_risk_control.serving.api.app:app --reload
