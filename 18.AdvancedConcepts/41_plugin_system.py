# plugin_system.py

import importlib


def load_plugin(plugin_name):
    try:
        module = importlib.import_module(plugin_name)

        if hasattr(module, "run"):
            return module.run
        else:
            print(f"{plugin_name} does not have a 'run' function")
            return None

    except ModuleNotFoundError:
        print("Plugin not found")
        return None


def main():
    plugin_name = input("Enter plugin name (without .py): ")

    plugin_func = load_plugin(plugin_name)

    if plugin_func:
        plugin_func()


main()
