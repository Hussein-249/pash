import os
import sys
# import psutil


def htop(args=None):
    try:
        # if name == win
        cores = os.cpu_count()
        print(cores)
        return "Numcores = " + str(cores)

    except Exception as e:
        print(f'Exception occurred during htop execution : {e}')
        return
