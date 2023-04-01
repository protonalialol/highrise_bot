import os
import subprocess

if __name__ == '__main__':
    print("started main.py")
    print("Env vairables now:")
    print(os.getenv('test'))
    print(os.getenv('botMode'))
    print(os.getenv('testing'))
    subprocess.call(['highrise', "demo:Bot", "63c08fb2d0187c1745407652", "605989e0149119cb9095f303d86e43ea35eed73237fe52960c562800d8b277c5"])
