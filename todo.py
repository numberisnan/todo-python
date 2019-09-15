import sys
import os.path
import importlib


def main(args):
    if not len(args):  # No arguments given
        module = importlib.import_module("help")
        module.execute("help", [])
    elif os.path.isdir(args[0]):
        module = importlib.import_module(args[0])
        module.execute(args[0], args[1:])
    else:
        print("'%s' is not a command! Try 'todo help' for command list." % args[0])
        return


if __name__ == "__main__":
    main(sys.argv[1:])
