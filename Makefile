.PHONY: build ensure-build clean

clean:
	rm -rf dist/
	find . -name "*.eggs" -type d -exec rm -rf {} +
	find . -name "*.egg-info" -type d -exec rm -rf {} +
	find . -name "__pycache__" -type d -exec rm -rf {} +

ensure-build:
	python3 -c "import build" || python3 -m pip install -U build

build: clean ensure-build
	python3 -m build

