import colorama
import argparse
import json
import difflib


def execute(name, args): # TODO Use decorators to execute general module stuff instead of PyCharm template
    with open(name + "/help.txt", "r") as helpFile:
        helpString = helpFile.read()

    parser = argparse.ArgumentParser(description=helpString, prog=name)
    parser.add_argument("item", help="The item to edit", metavar="ITEMNAME")
    parser.add_argument("prop", help="The property of item to edit", metavar="PROP")
    parser.add_argument("v", help="New value of property", metavar="VALUE")

    parsed = parser.parse_args(args)

    with open("./.data/todo.json", "r") as todoFile:
        todoDict = json.loads(todoFile.read())

    itemNames = []
    for item in todoDict["items"]:
        itemNames.append(item["name"])

    matchString = difflib.get_close_matches(parsed.item, itemNames, 1)[0]
    matchIndex = itemNames.index(matchString)

    if todoDict["items"][matchIndex][parsed.prop]:
        if type(todoDict["items"][matchIndex][parsed.prop]) == list:
            todoDict["items"][matchIndex][parsed.prop].append(parsed.v)
        elif type(todoDict["items"][matchIndex][parsed.prop]) == int:
            todoDict["items"][matchIndex][parsed.prop] = int(parsed.v)
        else:
            todoDict["items"][matchIndex][parsed.prop] = parsed.v
        print(colorama.Fore.WHITE + "List element " + matchString + " has been modified!")
    else:
        print(colorama.Fore.WHITE + "Error: Prop does not exist")

    with open("./.data/todo.json", "w") as todoFile:
        todoFile.write(json.dumps(todoDict))


if __name__ == "__main__":
    pass
