import json
import os
from importlib.metadata import version

class Driver:
    def __init__(self, task_config: dict):
        self.task_config = task_config

    def run(self, molecule_path: str, working_dir: str) -> str:
        def get_version(name: str):
            try:
                return version(name)
            except Exception:
                return "unknown"

        info = {
            "driver": "beta",
            "molecule_path": molecule_path,
            "working_dir": working_dir,
            "versions": {
                "numpy": get_version("numpy"),
                "requests": get_version("requests"),
                "pyscf": get_version("pyscf"),
                "gpu4pyscf-cuda12x": get_version("gpu4pyscf-cuda12x"),
                "pysisyphus": get_version("pysisyphus"),
                "volcengine-qcworker": get_version("volcengine-qcworker"),
            },
            "task_config": self.task_config,
        }

        output_path = os.path.join(working_dir, "beta_output.json")
        with open(output_path, "w") as f:
            json.dump(info, f, indent=2)

        return output_path
