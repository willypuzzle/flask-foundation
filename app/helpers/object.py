def is_method(obj, name):
    return hasattr(obj, name) and callable(getattr(obj, name))
