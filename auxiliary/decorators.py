def safe_call(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            print(f'{exc} occured while calling {func} with {args}, {kwargs}.')
    return wrapper
