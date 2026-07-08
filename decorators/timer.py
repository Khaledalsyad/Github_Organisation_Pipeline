import time


def timer_decorator(func):
    def inner(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f'function {func.__name__} takes {end - start:.2f} seconds')

        return result

    return inner