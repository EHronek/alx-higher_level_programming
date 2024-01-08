#!/usr/bin/python3
import importlib.util
if __name__ == "__main__":
    t_spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    module = importlib.util.module_from_spec(t_spec)
    t_spec.loader.exec_module(module)
    names = [name for name in dir(module) if not name.startswith('__')]
    for name in sorted(names):
        print(name)
