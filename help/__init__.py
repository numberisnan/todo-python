import os
import colorama


def execute(name, args):
    with open("help/allhelp.txt", "r") as helpfile:
        commandHelp = helpfile.read()
    print(colorama.Fore.RED + "TODO: A helpful CLI todo list")
    print(colorama.Fore.GREEN + "Commands: ")
    print(colorama.Fore.BLUE + commandHelp)


def generateAllHelp():
    helpString = ""
    for d in filter(lambda s: s != "shared" and s != "__pycache__" and "." not in s, next(os.walk('../'))[1]):  # TODO Filter by if file exists
        with open("../%s/help.txt" % d, "r") as file:
            helpString += d + " " * (30-len(d)) + file.read() + "\n"

    os.remove("./allhelp.txt")

    with open("allhelp.txt", "w") as helpFile:
        helpFile.write(helpString)


if __name__ == "__main__":
    generateAllHelp()