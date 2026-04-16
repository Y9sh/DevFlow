import subprocess
from typing import List

def cmd(value: List[str]) -> None:
    """
    Access to terminal 
    """
    try:
        subprocess.run(value, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except Exception as e:
        print(f"Unexpected error executing command: {type(e).__name__}: {e}")