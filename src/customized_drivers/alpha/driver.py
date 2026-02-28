import json
import os
from importlib.metadata import version

class Driver:
    def __init__(self):
        self.version = "alpha"

    def run(self, molecule_path: str, config_path: str):
        def get_version(name: str):
            try:
                return version(name)
            except Exception:
                return "unknown"

        with open(config_path, "r") as f:
            task_config = f.read()

        info = {
            "driver": self.version,
            "molecule_path": molecule_path,
            "config_path": config_path,
            "versions": {
                "numpy": get_version("numpy"),
                "requests": get_version("requests"),
                "pyscf": get_version("pyscf"),
                "gpu4pyscf-cuda12x": get_version("gpu4pyscf-cuda12x"),
                "pysisyphus": get_version("pysisyphus"),
                "volcengine-qcworker": get_version("volcengine-qcworker"),
            },
            "task_config": task_config,
        }

        with open("info.json", "w") as f:
            json.dump(info, f, indent=2)
