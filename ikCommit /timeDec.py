import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Time elapsed during {func.__name__} is {elapsed_time} seconds')
        return result
    return wrapper

@time_decorator
def add(*args):
    return sum(args)

result = add(5, 7)
print(result)