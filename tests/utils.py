"""
Copyright 2024, EPFL/Blue Brain Project

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
from contextlib import contextmanager
from pathlib import Path

TEST_ROOT = Path(__file__).parent
DATA = TEST_ROOT / "test_data"


@contextmanager
def cwd(path):
    """Context manager to temporarily change the working directory."""
    original_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(original_cwd)
