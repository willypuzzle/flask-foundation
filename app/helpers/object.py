import inspect

def is_method(obj, name):
    return hasattr(obj, name) and inspect.ismethod(getattr(obj, name))
