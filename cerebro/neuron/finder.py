import pkgutil


def find(path):
    for package in pkgutil.walk_packages(path):
        finder, name = package[0], package[1]
        loader = finder.find_module(name)
        mod = loader.load_module(name)
        yield mod
