import time

def get_str_seconds():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())

print(get_str_seconds())

