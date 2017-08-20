import pkgutil


def find(path):
    for finder, name, is_pkg in pkgutil.walk_packages(path):
        loader = finder.find_module(name)
        mod = loader.load_module(name)
        yield mod
