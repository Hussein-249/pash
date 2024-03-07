# To view the list of available internal commands, view the internal_binaries data structure

# import inspect
# import glob
# import curses
import os
import sys
import subprocess
import multiprocessing
import shlex
from ls import ls
from internal.c_pwd import c_pwd
from internal.cd import cd
from internal.htop import htop
from internal.sysinfo import sysinfo


arguments = sys.argv

# debug_flag = False
# if arguments[1] == "debug":
#     print("pash operating in debug mode - expect many messages")
#     debug_flag = True


def main():
    user = os.getlogin()
    # internal_binaries = set("ls", "pwd") # does not work bc creates set from letters!
    internal_binaries = {'ls': ls, 'pwd': c_pwd, 'cd': cd, 'htop': htop, 'sysinfo': sysinfo}
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
            args = parse_args(userinput)
            internal_check = search_internal(args[0], intern)

            execute_internal(args, intern) if internal_check else search_external(args[0])


def search_internal(cmd: str, internal_binaries: dict) -> bool:
    return cmd in internal_binaries


def search_external(cmd: str):
    path = c_pwd()
    files = os.listdir(path)

    # temp = glob.glob(os.path.join(path, '*.py'))
    # print(temp)

    for file in files:
        parts = file.split('.')
        name = parts[0]
        if name == cmd:
            ext = parts[-1]

            if ext == 'py':
                script_path = os.path.join(path, file)

                subprocess.run((['python', script_path]))
                return

            elif ext == 'exe':
                exe_path = os.path.join(path, file)
                subprocess.run([exe_path])
                return

        else:
            continue

    print(f'No internal or external command found.')

    return


def execute_internal(args: list, internal_binaries: dict):
    try:
        cmd = args[0]
        if cmd in internal_binaries:
            f = internal_binaries[cmd]
            # args = inspect.getfullargspec(f).args
            # print(args)

            only_args = args[1:]

            # if '&' in only_args[-1]:
            #     print(f'Found & character, running background')
            #
            #     subprocess.Popen([cmd] + only_args, capture_output=True, text=True)
            # else:
            #     f(only_args)

            f(only_args)

        else:
            print("Command not found in internal bins")

        return

    except Exception as e:
        print(f'Exception occurred during internal execution: {e}')
        return


def parse_args(userinput):
    index = 1
    args = userinput.split(' ')
    options = []

    for arg in args:
        if arg[0] == '-':
            options.append(arg[1:])
            index += 1

    files = []

    for i in range(index, len(args)):
        files.append(args[i])

    parsed = [args[0], options, files]

    # print(parsed)
    return parsed


if __name__ == '__main__':
    main()
