import os
import subprocess
from typing import List

base_git_ignore = """env/
venv/
.env/
.venv/
__pycache__/
"""

def cmd(value: List[str]) -> None:
    try:
        subprocess.run(value, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except Exception as e:
        print(f"Unexpected error executing command: {type(e).__name__}: {e}")

def git_init() -> None:
    if not os.path.exists(".git"):
        cmd(["git", "init"])
        print("Git repository initialized.")
        git_add_commit()
    else:
        print("Repository already exists.")

def git_add_commit() -> None:
    try:
        cmd(["git", "add", "."])
        name_commit = input("Enter commit message: ").strip()
        if not name_commit:
            raise ValueError("Commit message cannot be empty.")
        cmd(["git", "commit", "-m", name_commit])
        print("Commit saved successfully.")
    except Exception as e:
        print(f"Failed to commit: {type(e).__name__}: {e}")

def git_check_stats() -> None:
    try:
        print("\nChecking for uncommitted changes...")
        cmd(["git", "fetch"])
        cmd(["git", "status"])
    except Exception as e:
        print(f"Git check failed: {type(e).__name__}: {e}")

def run_aider() -> None:
    valid= True
    while valid:
        try:
            model_name = input("Enter model name (e.g., 'liquid/lfm2-1.2b'): ").strip()
            if not model_name:
                raise ValueError("Model name cannot be empty.")
            else:
                valid = False
                print(f"Running Aider with model: {model_name}")
                cmd(["aider", "--model", f"openai/{model_name}"])
        except Exception as e:
            print(e)
    

def create_gitignore() -> None:
    try:
        with open(".gitignore", "w") as w:
            w.write(base_git_ignore)
        print("Created .gitignore file.")
    except Exception as e:
        print(f"Failed to create .gitignore: {type(e).__name__}: {e}")
        

def main() -> None:
    try:
        # path for new project wihout any git
        if not os.path.exists(".gitignore"):
            create_gitignore()
            git_init()
            run_aider()
        else:
            # path project already have git 
            with open(".gitignore", "r") as r:
                content = r.read()
                print("\nCurrent .gitignore contents:")
                print(content)
                
            valid = True
            while valid:
                try:
                    choice = input("Update .gitignore? (y/n): ").strip().lower()
                    if not choice:
                        raise ValueError("No entries provided.Input can't be empty")
                    if choice == "y":
                        new_entries = input("Enter files to ignore (comma-separated): ").strip()
                        if os.path.exists(new_entries):
                            if not new_entries:
                                raise ValueError("No entries provided.Input can't be empty")

                            for entry in new_entries.split(","):
                                entry = entry.strip()
                                with open(".gitignore", "a") as a:
                                    a.write(f"\n{entry}")
                            valid = False
                            print("Updated .gitignore.")
                            git_check_stats()  # Refresh Git status
                            run_aider()
                        raise FileNotFoundError("File or directory not exists")
                    else:
                        valid = False
                        git_check_stats()
                        run_aider()
                except Exception as err:
                    print(err)

    except Exception as e:
        print(f"Script error: {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
