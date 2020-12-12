def safe_call(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            print(f'{func}({args}, {kwargs}): {exc}.')
    return wrapper
