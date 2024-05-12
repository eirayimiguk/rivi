init:
	pip install -r requirements.txt

run:
	flask --app application run

.PHONY: init run
