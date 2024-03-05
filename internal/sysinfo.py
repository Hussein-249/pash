import platform
import multiprocessing


def sysinfo():
    system_info = {
        'System': platform.system(),
        'Processor': platform.processor(),
        'Cores': multiprocessing.cpu_count(),
    }

    for key, value in system_info.items():
        print(f'{key} : {value}')

    return
