import os
from .git_manager import GIT
from .tools import ExcalocalServer,AgentAssistant,PythonEnvironment

tool = [ExcalocalServer(),AgentAssistant(),PythonEnvironment()]
git = GIT()
def main() -> None:
    while True:
        try:
            # draft for other tools
            choose_tools = int(input('List of Tools\n' + "1.Excalocal\n" + "2.Aider\n" + "3.Git Setup\n" + "4.Lazy-Git-Commit\n"+ "5.Create Python env\n" +"6.Exit\n" + "Enter:"))
            if not choose_tools:
                print("Invalid.Try again")
                continue
            if choose_tools == 1:
                tool[0].run_excalocal()
                print("Server Excalocal Running on http://localhost:3030/")
            elif choose_tools == 2:
                tool[1].run_aider()
            elif choose_tools == 3:
                if not os.path.exists(".gitignore"):
                    git.create_gitignore()
                    git.add_more_git_ignore()
                    git.git_init()
                else:
                    # path project already have git 
                    git.updated_gitignore()
            elif choose_tools == 4:
                git.auto_commit()
            elif choose_tools == 5:
                # for now only check environment that only using default name
                if not os.path.exists(".venv"):
                    tool[2].create_new_env()
                else:
                    print("Python Environment already exists.")
            else:
                tool[0].terminate_excalocal()
                break
        except Exception as e:
            print("Outer error handler",type(e).__name__,e)
            
if __name__ == "__main__":
    main()
