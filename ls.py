import os
from internal.c_pwd import c_pwd


def ls(args=None):
    options = {'l'}
    selected = []

    try:
        if not args[0] and not args[1]:
            path = c_pwd()
            os.chdir(path)
            del path
            files = os.listdir()
            for file in files:
                print(file)
        else:
            path = c_pwd()
            os.chdir(path)
            for option in args[0]:
                if option in options:
                    selected.append(option)
                else:
                    raise ValueError(f'Error: Invalid option {option}')
            if 'l' in selected:
                long()
        return

    except Exception as e:
        print(f'Exception: {e}')
        return


def long():
    nr = 0
    files = os.listdir()
    for file in files:
        nr += 1
        print(os.stat(file))

    print(f'Total # of files: {nr}')
    return
