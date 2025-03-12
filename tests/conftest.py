# Sets up the database in case they haven't run their script yet
import pytest
import subprocess
import os
import time
import shutil

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Detects the correct Python command and runs tech_talent.py before tests start."""

    script_path = os.path.join(os.path.dirname(__file__), "..", "tech_talent.py")

    # Detect whether 'python3' or 'python' should be used
    python_cmd = "python3" if shutil.which("python3") else "python"

    # Run the script
    process = subprocess.run([python_cmd, script_path], capture_output=True, text=True)

    if process.returncode != 0:
        raise RuntimeError(f"Failed to run python_pulse.py:\n{process.stderr}")

    # Give some time to ensure database setup completes
    time.sleep(2)