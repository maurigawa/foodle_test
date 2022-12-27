install: ## Install python environment.
	pip install -r requirements.txt

test:
	pytest test_sentences.py