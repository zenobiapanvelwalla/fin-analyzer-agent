import os
from dotenv import load_dotenv
import pytest

# Load this at the module level so it runs BEFORE any tests are collected
load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def env_vars():
    # This ensures keys are present for all tests
    return os.environ