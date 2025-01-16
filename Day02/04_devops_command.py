import subprocess

def execute_cammand(command):
    process = subprocess.run(command,
                             shell=True,
                             check=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE
                            )
    return process.stdout.decode()

print(execute_cammand("python --version"))