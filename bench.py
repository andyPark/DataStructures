import time

def benchmark(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    print((end - start) * 10000)

"""
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print((end - start) * 10000)
        return res
    return wrapper
"""