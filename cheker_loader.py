import subprocess
internet = False
while not internet:
    try:
        subprocess.check_call(["ping","-t 4" , "www.google.ru"])
    except subprocess.CalledProcessError:
        subprocess.call(r"""explorer C:\Users\1\Downloads""", shell=True,)
    finally:
        internet = True
