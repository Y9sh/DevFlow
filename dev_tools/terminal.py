import subprocess
from typing import List

# later make the terminal can be access by ('\')

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