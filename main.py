import os
import glob
import sys
from ls import ls
from internal.c_pwd import c_pwd
from internal.cd import cd
from internal.htop import htop

import subprocess

arguments = sys.argv

# debug_flag = False
# if arguments[1] == "debug":
#     print("pash operating in debug mode - expect many messages")
#     debug_flag = True


def main():
    user = os.getlogin()

    # internal_binaries = set("ls", "pwd") # does not work bc creates set from letters!

    internal_binaries = {'ls': ls, 'pwd': c_pwd, 'cd': cd, 'htop': htop}

    print(internal_binaries)

    prompt_loop(user, internal_binaries)

    return


def prompt_loop(user: str, intern: dict):
    prompt = user + " $ "

    while 1:
        userinput = input(prompt)
        # print(userinput)
        if userinput == "exit":
            break

        else:
            internal_check = search_internal(userinput, intern)

            if internal_check[0]:
                # print(userinput)
                execute_internal(userinput, intern)
                continue
            else:
                # print(internal_check[1])
                search_external(userinput)


def search_internal(cmd: str, internal_binaries: dict) -> tuple:

    if cmd in internal_binaries:
        res = tuple((True, cmd))
        return res
    else:
        res = tuple((False, "Unable to find internal executable."))
        return res


def search_external(cmd: str):
    path = c_pwd()

    files = os.listdir(path)

    temp = glob.glob(os.path.join(path, '*.py')) # for later

    # print(temp)

    for file in files:
        parts = file.split('.')

        name = parts[0]

        if name == cmd:
            ext = parts[-1]

            if ext == 'py':
                print(f'Found py')

                script_path = os.path.join(path, file)

                subprocess.run((['python', script_path]))
                return

            elif ext == 'exe':
                print(f'Found exe')
                return

        else:
            continue

    print(f'No internal or external command found.')

    return


def execute_internal(cmd: str, internal_binaries: dict):
    # NOTICE THAT THIS ONLY WORKS WITH FUNCTIONS TAKING NO ARGUMENTS
    # HOWEVER CD AND OTHERS TAKE ARGUMENTS
    # need to import inspect
    # also args = inspect.getfullargspec(function_to_execute).args
    try:
        if cmd in internal_binaries:
            internal_binaries[cmd]()

        else:
            print("Command not found in internal bins")

        return

    except Exception as e:
        print(f'Exception occurred during internal execution: {e}')

        return


if __name__ == '__main__':
    main()
