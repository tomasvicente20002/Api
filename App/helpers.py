import os

def combine_with_base_path(path):
    base_path = os.getcwd()
    return os.path.join(base_path,path)

def convert(value, type_):
    import importlib
    try:
        # Check if it's a builtin type
        module = importlib.import_module('__builtin__')
        cls = getattr(module, type_)
        return cls(value)
    except AttributeError:
        raise Exception("Non native type")

