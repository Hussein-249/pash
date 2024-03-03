import os
import sys
from ls import ls
from pwd import pwd

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
            else:
                print(internal_check[1])


def search_internal(cmd: str, internal_binaries: set) -> tuple:

    if cmd in internal_binaries:
        res = tuple((True, cmd))
        return res
    else:
        res = tuple((False, "Unable to find executable."))
        return res


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
