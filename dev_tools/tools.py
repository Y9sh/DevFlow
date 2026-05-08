import subprocess
from .terminal import cmd
import os

class ExcalocalServer:
    '''
    Tools for sketching diagram
    '''
    def __init__(self):
        #self.based = os.getcwd()
        #self.server = f'{self.based}/node_modules/.bin/excalocal.cmd' 
        # find out how to make it run even at other device
        self.server = 'E:/in_dev/tools/node_modules/.bin/excalocal.cmd' 
    
    def run_excalocal(self) -> None:
        # Start the server in the background

        subprocess.Popen(
            [self.server],
            stdout= subprocess.PIPE,
            stdin=subprocess.PIPE,
            text= True
        )
    
    def terminate_excalocal(self):
        print("Shutdown Server\n")
        subprocess.run([self.server,'-k', '3030'],text=True)
    
    def checking_open_port(self):
        print("Check any port still open")
        subprocess.run([self.server, '-l'],text=True)

class AgentAssistant:
    
    def __init__(self):
        self.cmd = cmd
        
    def run_aider(self) -> None:
        # need to install aider.exe manually..then setup as global execute..
        """
        Run 3rd party aider partner code agents
        """
        while True:
            model_name = input("Enter model name (e.g., 'liquid/lfm2-1.2b'): ").strip()
            if not model_name:
                print("Model name cannot be empty.")
                continue
            else:
                print(f"Running Aider with model: {model_name}")
                self.cmd(["aider", "--model", f"openai/{model_name}"])
                break
            