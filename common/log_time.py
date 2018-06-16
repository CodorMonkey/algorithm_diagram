import time


def log_time(func):
    def wrapper(*args, **kwargs):
        print('开始执行 %s 方法' % func.__name__)
        start = time.time() * 1000
        res = func(*args, **kwargs)
        end = time.time() * 1000
        print('执行 %s 结束，耗时 %d ms' % (func.__name__, end - start))
        return res

    return wrapper
