import colorama
import argparse
import sys
import json

sys.path.insert(1, "./shared/classes/")
from Task import Task

def execute(name, args):
    with open(name + "./help.txt", "r") as helpFile:
        helpString = helpFile.read()

    parser = argparse.ArgumentParser(description=helpString, prog=name)
    parser.add_argument("-p", "-priority", help="List only items with given priority level and above", metavar="PRIORITY", dest="p", type=int, default=0)
    parser.add_argument("-c", "-class", help="List only items from given class", metavar="CLASS", dest="c", default=None)

    parsed = parser.parse_args(args)

    with open("./.data/todo.json", "r") as todoFile:
        todoList = json.loads(todoFile.read())["items"]

    tasks = []

    for item in todoList:
        task = Task(item["name"], item["description"], p=item["p"], c=item["c"])
        if task.p < parsed.p:
            continue
        if parsed.c and parsed.c not in task.c:
            continue
        tasks.append(task)

    tasks.sort()
    print("")

    for task in tasks:
        color = colorama.Fore.BLUE
        if task.p == 1:
            color = colorama.Fore.GREEN
        elif task.p == 2:
            color = colorama.Fore.RED
        elif task.p >= 3:
            color = colorama.Fore.YELLOW
        print(color + "%s: %s     -     %s" % (task.name, task.description, task.p))

    print("")


if __name__ == "__main__":
    pass
