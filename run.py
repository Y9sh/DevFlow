import os
from git import Git
git = Git()
def main() -> None:
    # maybe i can make 2 modes, 1st one to use basic git and 2nd is automate fully git and run aider
    # for now only 2nd mode 
    # path for new project wihout any git
    if not os.path.exists(".gitignore"):
        git.create_gitignore()
        git.add_more_git_ignore()
        git.git_init()
        while True:
            # ask for rerun aider
            rerun = input("Run aider (y/n)?")
            if not rerun:
                print("Invalid")
                continue
            if rerun == "y":
                git.loop_step()
            else:
                print("See yaa~~~")
                break    
    else:
        # path project already have git 
        git.updated_gitignore()


if __name__ == "__main__":
    main()
