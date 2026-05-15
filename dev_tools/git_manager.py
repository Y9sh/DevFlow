import os
import subprocess
from .terminal import cmd 

class GIT:
    '''
    GIT automations wrapper
    '''
    def __init__(self):
        self.cmd =cmd
        self.base_git_ignore = """env/
venv/
.env
.venv/
__pycache__/
.aider*
node_modules/
"""

    def git_init(self) -> None:
        """
        Check if .git files is exist
        """
        if not os.path.exists(".git"):
            self.cmd(["git", "init"])
            print("Git repository initialized.")
            self.git_add_commit()
        else:
            print("Repository already exists.")

    def git_add_commit(self) -> None:
        """
        1st snapshot of commited projects
        """
        try:
            self.cmd(["git", "add", "."])
            name_commit = input("Enter commit message: ").strip()
            if not name_commit:
                raise ValueError("Commit message cannot be empty.")
            self.cmd(["git", "commit", "-m", name_commit])
            print("Commit saved successfully.")
        except Exception as e:
            print(f"Failed to commit: {type(e).__name__}: {e}")

    def git_check_stats(self) -> None:
        """
        Details git status
        """
        try:
            print("\nChecking for uncommitted changes...")
            print("Latest Modified Files:")
            self.cmd(["git", "diff", "--name-only"])
            self.cmd(["git", "status"])
        except Exception as e:
            print(f"Git check failed: {type(e).__name__}: {e}")
            
    def git_details_stats(self) -> None:
        """
        Details changing each file being modified.
        """
        while True:
            try:
                user = int(input("Do you want to see the details stats files changes? (1-yes,2-no):"))
                if not user:
                    print("Input can't left empty")
                    continue
                if user == 1:   
                    print("\nChecking for changes...")
                    self.cmd(["git", "status"])
                    print("Press q to quit")
                    self.cmd(["git", "diff"])
                    break
                else:
                    print("Skip to auto-commit")
                    break
            except Exception as e:
                print(f"Git check failed: {type(e).__name__}: {e}")
            

    def auto_commit(self)-> None:
        print("-Welcome to Lazy-Commit-")
        try:
            result = subprocess.run(["git","status","--porcelain"], capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Git command failed - {e}")
        if result.returncode == 0:
            list_output = result.stdout.strip().split("\n")
            new_list = ['']
            while True:
                print("Warning: Lazy-commit will skip stage-changes (Modified -> Commit)")
                choices = int(input("Commit all files? (0-cancel/1-yes/2-no):"))
                if choices == 2:
                    print("Choose files to commit (0-cancel):")
                    num = 1
                    for i in range(len(list_output)):
                        print([num],list_output[i].strip())
                        new_list.append(list_output[i])
                        num +=1
                    print("Length list:",len(list_output))
                    u_i = int(input("Enter:"))
                    if u_i == 0:
                        print("Cancel")
                        break
                    if u_i <= len(list_output):
                        choose = new_list[u_i].strip()
                        if choose.startswith("M"):
                            try:
                                self.cmd(["git", "add", choose[1:].strip()])
                                commit_name =input("Enter commit name:")
                                self.cmd(["git", "commit", "-m",commit_name])
                                print("Git Commit Done")
                                break
                            except subprocess.CalledProcessError as e:
                                print(f"Git command failed - {e}")
                        elif choose.startswith("?"):
                            try:
                                self.cmd(["git", "add", choose[2:].strip()])
                                commit_name =input("Enter commit name:")
                                self.cmd(["git", "commit", "-m",commit_name])
                                print("Git Commit Done")
                                break
                            except subprocess.CalledProcessError as e:
                                print(f"Git command failed - {e}")
                    else:
                        print("Invalid input")
                        continue
                elif choices == 1: 
                    # correct again to make this only for files that related not all.
                    self.git_check_stats()
                    self.cmd(["git", "add", "-A"])
                    commit_name = str(input("Enter commit name:"))
                    self.cmd(["git", "commit", "-m", commit_name])
                    self.git_check_stats()
                    break
                elif choices == 0:
                    break
                else:
                    print("Invalid input")
                    continue
        else: 
            print("No files changes.")
            
    def create_gitignore(self) -> None:
        """
        Create git .gitignore
        """
        try:
            if not os.path.exists(".gitignore"):
                with open(".gitignore", "w") as w:
                    w.write(self.base_git_ignore)
                print("Created .gitignore file.")
            else:
                with open(".gitignore", "a") as a:
                    a.write(self.base_git_ignore) # just for safe..if gitignore already exists..
        except Exception as e:
            print(f"Failed to create .gitignore: {type(e).__name__}: {e}")

    def updated_gitignore(self) -> None:
        self.git_init()
        with open(".gitignore", "r") as r:
            content = r.read()
            print("\nCurrent .gitignore contents:")
            print(content)
        while True:
            choice = input("Update .gitignore? (y/n):").strip().lower()
            if not choice:
                print("No entries provided.Input can't be empty")
                continue
            if choice == "y":
                new_entries = input("Enter files to ignore (comma-separated):").strip()
                print("Let me check this: ",new_entries)
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
                with open(".gitignore","r") as r:
                    print("After Updated:\n",r.read())
                break
            else:
                print("Skip update .gitignore...")
                self.git_check_stats()
            break

    def add_more_git_ignore(self) -> None:

        with open(".gitignore", "r") as r:
            content = r.read()
            print("\nCurrent .gitignore contents:")
            print(content)
        while True:
            choice = input("Add more files to .gitignore? (y/n):").strip().lower()
            if not choice:
                print("No entries provided.Input can't be empty")
                continue
            if choice == "y":
                new_entries = input("Enter files to ignore (comma-separated):").strip()
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
                        a.write(f"{entry}\n")
                    print("Updated .gitignore.")
                with open(".gitignore","r") as r:
                    print("After Updated:\n",r.read())
                break
            break
        