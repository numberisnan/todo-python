import colorama
import argparse
import json


def execute(name, args):
    with open(name + "/help.txt", "r") as helpFile:
        helpString = helpFile.read()

    parser = argparse.ArgumentParser(description=helpString, prog=name)

    parser.add_argument("name", help="Name of the task")
    parser.add_argument("description", help="Task description")
    parser.add_argument("-p", "-priority", dest="p", default=0, type=int, help="Priority level for task", metavar="PRIORITY")
    parser.add_argument("-c", "-class", dest="c", nargs="*", help="Task class used for organisation (e.g. study, read, test)", metavar="CLASSNAME", default=[])

    parsed = parser.parse_args(args)

    with open("./.data/todo.json", "r") as todoFile:
        todoDict = json.loads(todoFile.read())
        todoDict["items"].append({
            "name": parsed.name,
            "description": parsed.description,
            "p": parsed.p,
            "c": parsed.c
        })

    with open("./.data/todo.json", "w") as todoFile:
        todoFile.write(json.dumps(todoDict))

    print(colorama.Fore.RED + "Successfully saved task: " + parsed.name)


if __name__ == "__main__":
    pass
