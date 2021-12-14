import os

def combine_with_base_path(path):
    base_path = os.getcwd()
    return os.path.join(base_path,path)