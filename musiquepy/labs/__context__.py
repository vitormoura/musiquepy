import os

PACKAGE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def package_path(*paths, package_directory=PACKAGE_ROOT_DIR):
    return os.path.join(package_directory, *paths)