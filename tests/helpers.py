from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def load_module(module_name: str, relative_path: str):
    repo_root = Path(__file__).resolve().parent.parent
    module_path = repo_root / relative_path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
