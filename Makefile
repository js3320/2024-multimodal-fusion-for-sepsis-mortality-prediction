.PHONY: setup lint test clean

setup:
	python -m pip install -r requirements.txt

lint:
	black src --check
	isort src --check-only

nb:
	jupyter lab

clean:
	rm -rf __pycache__ .pytest_cache .ipynb_checkpoints
