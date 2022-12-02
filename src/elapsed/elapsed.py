import time

def elapsed_time(func):
    def wraper(*args, **kwarg):
        start = time.time()
        func(*args, **kwarg)
        end = time.time()
        print(f'Elapsed time: {end - start}')
    return wraper
