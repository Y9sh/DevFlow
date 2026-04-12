import subprocess

class ExcalocalServer:
    '''
    Tools for sketching diagram
    '''
    def __init__(self):
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
        print("Shutdown Server")
        subprocess.run([self.server,'-k', '3030'],text=True)
    
    def checking_open_port(self):
        print("Check any port still open")
        subprocess.run([self.server, '-l'],text=True)

    
