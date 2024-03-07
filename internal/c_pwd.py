import os


def c_pwd(args=None):
    try:
        cwd = os.path.abspath('')

        print(cwd)
        return cwd

    except Exception as e:
        print(f"Exception occurred: {e}")

        return
