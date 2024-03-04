import os
from pwd import pwd


def ls():
    path = pwd()

    files = os.listdir(path)

    # print(ls)

    for file in files:
        print(file)

    return