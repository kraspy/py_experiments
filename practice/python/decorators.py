def deco_fn(p1, p2):
    def wrapper(fn):
        def foo(*args, **kwargs):
            print(f'Decorator params: {p1=}, {p2=}')
            print('before fn...')
            print('Call: ', fn.__name__)
            fn(*args, **kwargs)
            print('after fn...')

        return foo

    return wrapper


@deco_fn(1, 2)
def decorated_fn(*args, **kwargs):
    print(args)
    print(kwargs)


decorated_fn(1, 2)
