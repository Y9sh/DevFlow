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
    try:
        if not os.path.exists(".git"):
            cmd(["git", "init"])
            print("Git repository initialized.")
            git_add_commit()
        else:
            print("Repository already exists.")
    except Exception as e:
        print("Caught in error")
        print(type(e).__name__,e)

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
        
def git_details_stats() -> None:
    while True:
        try:
            user = int(input("Do you want to see the details stats files changes? (1-yes,2-no):"))
            if not user:
                print("Input can't left empty")
                continue
            if user == 1:   
                print("\nChecking for changes...")
                cmd(["git", "status"])
                print("Press q to quit")
                cmd(["git", "diff"])
                break
            else:
                print("Skip to auto-commit")
                break
        except Exception as e:
            print(f"Git check failed: {type(e).__name__}: {e}")
        
def run_aider() -> None:
    while True:
        model_name = input("Enter model name (e.g., 'liquid/lfm2-1.2b'): ").strip()
        if not model_name:
            print("Model name cannot be empty.")
            continue
        else:
            print(f"Running Aider with model: {model_name}")
            cmd(["aider", "--model", f"openai/{model_name}"])
            break
            
def auto_commit()-> None:
    print("-Welcome to Auto-Commit-")
    try:
        result = subprocess.run(["git","status","--porcelain"], capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Git command failed - {e}")
    if result.returncode == 0:
        list_output = result.stdout.strip().split("\n")
        new_list = ['']
        while True:
            choices = int(input("Commit all files? (0-skip/1-yes/2-no):"))
            if choices == 2:
                print("Choose files to commit:")
                num = 1
                for i in range(len(list_output)):
                    print([num],list_output[i].strip())
                    new_list.append(list_output[i])
                    num +=1
                print("Length list:",len(list_output))
                u_i = int(input("Enter:"))
                if not u_i:
                    print("Input can't empty")
                    continue
                if u_i <= len(list_output):
                    choose = new_list[u_i].strip()
                    if choose.startswith("M"):
                        try:
                            cmd(["git", "add", choose[1:].strip()])
                            commit_name =input("Enter commit name:")
                            cmd(["git", "commit", "-m",commit_name])
                            print("Thank You~~~Byee")
                            break
                        except subprocess.CalledProcessError as e:
                            print(f"Git command failed - {e}")
                    elif choose.startswith("?"):
                        try:
                            cmd(["git", "add", choose[2:].strip()])
                            commit_name =input("Enter commit name:")
                            cmd(["git", "commit", "-m",commit_name])
                            print("Thank You~~~Byee,SYS")
                            break
                        except subprocess.CalledProcessError as e:
                            print(f"Git command failed - {e}")
                else:
                    print("Invalid input")
                    continue
            elif choices == 1: 
                # correct again to make this only for files that related not all.
                cmd(["git", "add", "."])
                cmd(["git", "commit", "-m", "Auto-commited all files related"])
                break
            elif choices == 0:
                print("GoodBye~~")
                break
            else:
                print("Invalid input")
                continue
    else: 
        print("No files changes.")
        
def create_gitignore() -> None:
    try:
        with open(".gitignore", "w") as w:
            w.write(base_git_ignore)
        print("Created .gitignore file.")
    except Exception as e:
        print(f"Failed to create .gitignore: {type(e).__name__}: {e}")

def updated_gitignore() -> None:
    
    with open(".gitignore", "r") as r:
        content = r.read()
        print("\nCurrent .gitignore contents:")
        print(content)
    while True:
        choice = input("Update .gitignore? (y/n): ").strip().lower()
        if not choice:
            print("No entries provided.Input can't be empty")
            continue
        if choice == "y":
            new_entries = input("Enter files to ignore (comma-separated): ").strip()
            if not new_entries:
                print("No entries provided.Input can't be empty")
                continue
            for entry in new_entries.split(","):
                print(new_entries.split(","))
                entry = entry.strip()
                if not os.path.exists(entry):
                    print("Folder/files not found")
                    continue
                print(os.path.exists(entry))
                with open(".gitignore", "a") as a:
                    a.write(f"\n{entry}")
                print("Updated .gitignore.")
            git_check_stats()  # Refresh Git status
            run_aider()
            git_details_stats()
            auto_commit()
        else:
            print("Skip update .gitignore...")
            git_check_stats()
            run_aider()
            git_details_stats()
            auto_commit()

def add_more_git_ignore() -> None:

    with open(".gitignore", "r") as r:
        content = r.read()
        print("\nCurrent .gitignore contents:")
        print(content)
    while True:
        choice = input("Update .gitignore? (y/n): ").strip().lower()
        if not choice:
            print("No entries provided.Input can't be empty")
            continue
        if choice == "y":
            new_entries = input("Enter files to ignore (comma-separated): ").strip()
            if not new_entries:
                print("No entries provided.Input can't be empty")
                continue
            for entry in new_entries.split(","):
                print(new_entries.split(","))
                entry = entry.strip()
                if not os.path.exists(entry):
                    print("Folder/files not found")
                    continue
                print(os.path.exists(entry))
                with open(".gitignore", "a") as a:
                    a.write(f"\n{entry}")
                print("Updated .gitignore.")
            break

        
def main() -> None:
    
    # path for new project wihout any git
    if not os.path.exists(".gitignore"):
        create_gitignore()
        add_more_git_ignore()
        git_init()
        run_aider()
        git_details_stats()
        auto_commit()
        
    else:
        # path project already have git 
        updated_gitignore()
            


if __name__ == "__main__":
    main()
