def outer_fn(x):
    def inner_fn(y):
        print(x * y)

    return inner_fn


double = outer_fn(2)

double(10)


def logger(prefix):
    def log(msg):
        print(f'[{prefix}]: {msg}')

    return log


info_logger = logger('INFO')

info_logger('Message 1')
info_logger('Message 2')


print(info_logger.__code__.co_freevars)

print(info_logger.__closure__[0].cell_contents)
