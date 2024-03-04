import os


def pwd():
    try:
        cwd = os.path.abspath('.')
        return cwd

    except Exception as e:
        print(f"Exception occurred: {e}")

        return
