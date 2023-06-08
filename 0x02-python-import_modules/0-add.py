#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util

    spec = importlib.util.spec_from_file_location("add_0", "./add_0.py")
    add_0 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(add_0)

    a = 1
    b = 2
    c = add_0.add(a, b)
    print("{} + {} = {}".format(a, b, c))
