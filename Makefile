.PHONY: build ensure-build

ensure-build:
	python3 -c "import build" || python3 -m pip install -U build

build: ensure-build
	python3 -m build

