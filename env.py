import sys
import os
from getpass import getuser
# import subprocess
import shutil
import keyboard


argv = sys.argv[1:]
user = getuser()
path = os.getcwd()
try:
    os.mkdir(f"C:\\Users\\{user}\\envs")
except:
    pass
os.chdir(f"C:\\Users\\{user}\\envs")
# print(os.getcwd())

def prHelp():
    print("""
Commands are:
    create "env name" (create env),
    activate "env name" (activate env),
    deactivate (deactivate env),
    delete "env name" (delete env),
    path "env name" (get env path),
    all (show all environments),
    setup (setup env command),
    help (show all the commands)
""")


def makeEnv(name):
    os.system(f"python -m venv {name}")
    try:
        os.remove(f"{name} run.bat")
    except:
        pass
    shutil.copy(__file__, f"{name}\\Lib\\site-packages\\env.py")
    # shutil.copy(, f"{name}\\Lib\\site-packages\\keyboard.py")
    shutil.copytree(os.path.dirname(__file__)+r"\keyboard", f"{name}\\Lib\\site-packages\\keyboard")
    

def activateEnv(name, user):
    activate = name + r"\scripts\activate.bat"
    # os.chdir(path)
    # os.system('start cmd /k "C:\\Users\\'+user+f'\\envs\\{activate}"')
    keyboard.write('"C:\\Users\\'+user+f'\\envs\\{activate}"')
    keyboard.press_and_release("ENTER")


def killTerminal():
    os.system("title forkill")
    os.system('taskkill /FI "WINDOWTITLE eq forkill" /IM cmd.exe')

def setup():
    os.system("pip install keyboard")
    cmd = "env=python -m env $*"
    os.chdir(f"C:\\Users\\{user}")
    with open("setup.doskey", "w") as f:
        f.write(cmd)
    os.system(f'reg add "HKCU\\Software\\Microsoft\\Command Processor" /v Autorun /d "doskey /macrofile=\\"c:\\Users\\{user}\\setup.doskey"" /f')

# print(os.path.dirname(__file__))

if len(argv) == 2:
    if argv[1] in os.listdir() or argv[0] == "create":
        if argv[0] == "create":
            makeEnv(argv[1])
            print("Env created succesfuly")
        elif argv[0] == "activate":
            activateEnv(argv[1], user)
            # killTerminal()
        elif argv[0] == "delete":
            ans = input("You sure you want to remove this env?(Y/N): ")
            if ans.lower() == "y":
                shutil.rmtree(argv[1], ignore_errors=True)
                print()
                print("env removed succesfuly")
            else:
                print()
                print("env not removed")
        elif argv[0] == "path":
            p = f"#!/Users/{user}/envs/{argv[1]}/Scripts/python"
            print()
            print("The path is: ",p)
        else:
            print()
            print("Wrong syntax")
            prHelp()
    else:
        print()
        print("This environment not exists")
elif len(argv) == 1:
    if argv[0] == "help":
        print()
        prHelp()
    elif argv[0] == "deactivate":
        # os.system(f'start cmd /k cd "{path}"')
        # killTerminal()
        keyboard.write(f"\"C:\\Users\\{user}\\envs\\{os.listdir()[0]}\\Scripts\\deactivate.bat\"")
        keyboard.press_and_release("ENTER")
    elif argv[0] == "all":
        di = os.listdir()
        if di:
            for d in di:
                print(d)
        else:
            print("You dont have any environments")
    elif argv[0] == "setup":
        setup()
    else:
        print()
        print("Wrong syntax")
        prHelp()
elif len(argv) == 0:
    print()
    prHelp()
else:
    print()
    print("Wrong syntax")
    prHelp()
