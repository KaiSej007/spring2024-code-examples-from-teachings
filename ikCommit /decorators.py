import datetime
import logging

logging.basicConfig(filename='times.log', level=logging.INFO)

def log_timestamp(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now()
        logging.info(f'Function {func.__name__} called at {timestamp}')
        return func(*args, **kwargs)
    return wrapper

@log_timestamp
def add(*args):
    return sum(args)

result = add(5, 7)
print(result)

with open('function_calls.log', 'r') as f:
    contents = f.read()
print(contents)

@log_timestamp
def printer(text):
    return text

result = printer('Hello, World!')
print(result)



