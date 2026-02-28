.PHONY: build ensure-build ensure-scm clean print-version

clean:
	rm -rf dist/
	rm -rf build/
	find . -name "*.eggs" -type d -exec rm -rf '{}' +
	find . -name "*.egg-info" -type d -exec rm -rf '{}' +
	find . -name "__pycache__" -type d -exec rm -rf '{}' +

ensure-build:
	python3 -c "import build" || python3 -m pip install -U build

ensure-scm:
	python3 -c "import setuptools_scm" || python3 -m pip install -U setuptools_scm

build: clean ensure-build
	python3 -m build --wheel

print-version: ensure-scm
	python3 -c "import setuptools_scm as s; print(s.get_version())"
