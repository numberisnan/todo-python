import colorama
import argparse
import json


def execute(name, args):
    with open(name + "/help.txt", "r") as helpFile:
        helpString = helpFile.read()

    parser = argparse.ArgumentParser(description=helpString, prog=name)
    parser.add_argument("-f", "-force", help="Bypass confirmation", default=False, action="store_const", const=True, dest="f")

    parsed = parser.parse_args(args)

    if parsed.f or input(colorama.Fore.RED + "Are you sure? (N/y)").lower() == "y":
        with open("./.data/todo.json", "w") as todoFile:
            todoFile.write(json.dumps({
                "items": []
            }))
        print(colorama.Fore.RED + "Cleared!")


if __name__ == "__main__":
    pass
