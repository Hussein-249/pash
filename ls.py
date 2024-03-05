import os
from internal.c_pwd import c_pwd


def ls():
    path = c_pwd()

    print(path)

    os.chdir(path)

    files = os.listdir()

    print(files)

    # print(ls)

    for file in files:
        print(file)

    return
