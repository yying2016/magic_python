import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call {}()'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("{} call {}()".format(text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log
def now():
    print('2020-1-12')

@log2('execute')
def now2():
    print('2020-1-12')


if __name__ == "__main__":
    now()
    now2()
    print(now2.__name__)