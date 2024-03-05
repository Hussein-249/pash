import os


def mkdir(path):
    try:

        c = path.split(os.path.sep)

        print(c)
        return

    except Exception as e:
        print(f'Exception: {e}')
        return
