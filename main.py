import logging
import os
from  subprocess import Popen, PIPE, STDOUT
import sys

def log_subprocess_output(pipe):
    for line in iter(pipe.readline, b''): # b'\n'-separated lines
        logging.info('got line from subprocess: %r', line)

if __name__ == '__main__':
    print("started main.py")
    print("Env vairables now:")
    print(os.getenv('test'))
    print(os.getenv('botMode'))
    print(os.getenv('testing'))
    input()
    #subprocess.call(['highrise', "demo:Bot", "63c08fb2d0187c1745407652", "605989e0149119cb9095f303d86e43ea35eed73237fe52960c562800d8b277c5"])
    process = Popen("highrise demo:Bot 63c08fb2d0187c1745407652 605989e0149119cb9095f303d86e43ea35eed73237fe52960c562800d8b277c5", stdout=PIPE, stderr=STDOUT)
    with process.stdout:
        log_subprocess_output(process.stdout)
    exitcode = process.wait()  # 0 means success
    #sys.argv = ["demo:Bot", "63c08fb2d0187c1745407652", "605989e0149119cb9095f303d86e43ea35eed73237fe52960c562800d8b277c5"]
