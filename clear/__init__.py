import colorama
import argparse
import json
import difflib


def execute(name, args):
    with open(name + "./help.txt", "r") as helpFile:
        helpString = helpFile.read()

    parser = argparse.ArgumentParser(description=helpString, prog=name)
    parser.add_argument("-f", "-force", help="Bypass confirmation", default=False, action="store_const", const=True, dest="f")
    parser.add_argument("-t", "-title", help="Title of task. Deletes closest match if none are found", dest="title", default=False)

    parsed = parser.parse_args(args)

    if parsed.title and (parsed.f or input(colorama.Fore.RED + "Are you sure you want to delete " + parsed.title + " from the list? (N/y)").lower() == "y"):
        with open("./.data/todo.json", "r") as todoFile:
            todoDict = json.loads(todoFile.read())

        itemNames = []
        for item in todoDict["items"]:
            itemNames.append(item["name"])

        matchString = difflib.get_close_matches(parsed.title, itemNames, 1)[0]

        todoDict["items"].pop(itemNames.index(matchString))

        with open("./.data/todo.json", "w") as todoFile:
            todoFile.write(json.dumps(todoDict))







    elif parsed.f or input(colorama.Fore.RED + "Are you sure you want to delete the ENTIRE LIST? (N/y)").lower() == "y":
        with open("./.data/todo.json", "w") as todoFile:
            todoFile.write(json.dumps({
                "items": []
            }))
        print(colorama.Fore.RED + "Cleared!")


if __name__ == "__main__":
    pass
