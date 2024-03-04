import os
import sys
from ls import ls
from pwd import pwd

import subprocess

arguments = sys.argv

# debug_flag = False
# if arguments[1] == "debug":
#     print("pash operating in debug mode - expect many messages")
#     debug_flag = True


def main():
    user = os.getlogin()

    # internal_binaries = set("ls", "pwd") # does not work bc creates set from letters!

    # print(internal_binaries)

    internal_binaries = {'ls', 'pwd'}

    print(internal_binaries)

    prompt_loop(user, internal_binaries)

    return


def prompt_loop(user: str, intern: set):

    prompt = user + " $ "
    prompt_flag = True
    while prompt_flag:
        userinput = input(prompt)
        # print(userinput)
        if userinput == "exit":
            prompt_flag = False
            break

        else:
            internal_check = search_internal(userinput, intern)

            if internal_check[0]:
                # print(userinput)
                execute_internal(userinput)
                continue
            else:
                # print(internal_check[1])
                search_external(userinput)


def search_internal(cmd: str, internal_binaries: set) -> tuple:

    if cmd in internal_binaries:
        res = tuple((True, cmd))
        return res
    else:
        res = tuple((False, "Unable to find internal executable."))
        return res


def search_external(cmd: str):

    exe = set()
    py = set()

    path = pwd()

    files = os.listdir(path)

    print(ls)

    # for file in files:
    #     print(file)

    for file in files:
        parts = file.split('.')

        name = parts[0]

        if name == cmd:

            ext = parts[-1]

            if ext == 'py':
                py.add(file)
                print(f'Found py')

                script_path = os.path.join(path, file)

                subprocess.run((['python', script_path]))
                return
            elif ext == 'exe':
                exe.add(file)
                print(f'Found exe')
                return
        else:
            continue

    print(f'No internal or external command found.')

    return

    # if cmd in internal_binaries:
    #
    #     res = tuple((True, cmd))
    #     return res
    # else:
    #     res = tuple((False, "Unable to find executable as internal or external command file"))
    #     return res


def execute_internal(cmd: str):

    if cmd == "ls":
        # print("Executing " + cmd)
        ls()

    if cmd == "pwd":
        # print("Executing " + cmd)
        res = pwd()
        print(res)

    else:
        print("")

    return


if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
