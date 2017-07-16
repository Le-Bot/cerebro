import pkgutil

NEURONS = {}

def get_all_neurons(path):
    for finder, name, is_pkg in pkgutil.walk_packages(path):
        try:

            loader = finder.find_module(name)
            mod = loader.load_module(name)
        except:
            print("Error loading '%s'".format(name))
        else:
            if hasattr(mod, 'KEYWORDS'):
                NEURONS.update(mod.KEYWORDS)