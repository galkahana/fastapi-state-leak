.PHONY : run

run: 
	poetry run uvicorn --host 0.0.0.0 --port 5002 main:app

test:
	poetry run python -m test