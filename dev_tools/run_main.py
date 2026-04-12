import os
from .git_manager import GIT
from .excalocal import ExcalocalServer

excalocal = ExcalocalServer()
git = GIT()
def main() -> None:
    try:
        # draft for other tools
        choose_tools = int(input('List of Tools (1.Excalocal 2.Skip):'))
        if choose_tools == 1:
            excalocal.run_excalocal()
            print("Server Excalocal Run on http://localhost:3030/")

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
                    excalocal.terminate_excalocal()
                    print("See yaa~~~")
                    break    
        else:
            # path project already have git 
            git.updated_gitignore()
            excalocal.terminate_excalocal()
    except Exception as e:
        print("Outer error handler",type(e).__name__,e)
        excalocal.terminate_excalocal()
        
if __name__ == "__main__":
    main()
