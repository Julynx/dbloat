import os
from os import listdir
from os.path import isfile, join
import sys
import time


def enter_prompt(question):

    print(question)
    print("")

    answer = input("[Press Enter to continue]")
    return answer


def menu(choice_list, default=None, question=None):

    tab4 = "    "
    default_str = "" if default is None else " (Default " + str(default) + ")"
    question = "" if question is None else "\n" + str(question) + "\n"

    selected = -1
    while not index_belongsto(selected, choice_list):

        # Print question and menu choices
        print(question, end="")
        print("")
        for choice in choice_list:
            print(f"{tab4}{choice_list.index(choice)} {choice}")
        print("")

        # Ask for user selection
        selected = input(f"Your choice{default_str}: ")

        # Fall back to default if selection is out of bounds
        if not index_belongsto(selected, choice_list):
            selected = default
        else:
            selected = int(selected)

    if choice_list[selected] == "Exit":
        raise KeyboardInterrupt

    return selected


def index_belongsto(idx, list_):

    try:
        idx = int(idx)
    except (ValueError, TypeError) as e:
        idx = -1

    return False if (idx < 0) or (idx >= len(list_)) else True


def read_file_lines(filename):

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    return lines


def adb_prepare_bulk_execute(command, arg_list, loud=False):

    # Construct and add each command to the command string
    cmd_str = ""
    for arg in arg_list:
        if not arg.startswith("#"):
            partial_str = f"{command} {arg}"
            if loud:
                print(partial_str, end="")
                time.sleep(0.1)
            cmd_str += partial_str

    # Add command to close the ADB shell
    cmd_str += "exit\n"

    return cmd_str


def build_file_dict():

    files = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    dict_ = {}

    files.sort()
    for file in files:

        name = file.replace("_", " ")
        name = name.capitalize()
        name = name.strip()

        if name.endswith(".txt"):
            name = name.replace(".txt", "")
        else:
            continue

        dict_[name] = file

    return dict_


def main():

    prompt_txt = """
         88  88           88
         88  88           88                             ,d
         88  88           88                             88
 ,adPPYb,88  88,dPPYba,   88   ,adPPYba,   ,adPPYYba,  MM88MMM
a8"    `Y88  88P'    "8a  88  a8"     "8a  ""     `Y8    88
8b       88  88       d8  88  8b       d8  ,adPPPPP88    88
"8a,   ,d88  88b,   ,a8"  88  "8a,   ,a8"  88,    ,88    88,
 `"8bbdP"Y8  8Y"Ybbd8"'   88   `"YbbdP"'   `"8bbdP"Y8    "Y888

Android Debloater by Julynx (github.com/Julynx/dbloat)

Prerequisites:
    - Install ADB. Ubuntu / Debian: sudo apt install android-tools-adb
    - Enable USB debugging: 'Settings > Developer options > USB debugging'
    - Connect your device to the computer with a USB cable."""

    # Get command line arguments
    try:
        uninstall_cmd = f"pm {sys.argv[1]} --user 0"
    except IndexError:
        uninstall_cmd = "pm uninstall --user 0"

    # Enter prompt to continue
    enter_prompt(prompt_txt)

    # Build file dictionary
    file_dict = build_file_dict()
    choices = list(file_dict.keys())
    choices.append("Exit")

    # Ask and get answer from user input
    try:
        selected_idx = menu(choices, question="Select bloatware to remove:")
    except KeyboardInterrupt:
        print("")
        exit(0)

    # Get the selected file
    selected = choices[selected_idx]
    selected_file = file_dict[selected]

    # Read the file and get the list of packages to uninstall
    print("Running commands from file:", selected_file)
    cmd_list = read_file_lines(selected_file)
    command_str = adb_prepare_bulk_execute(uninstall_cmd, cmd_list)
    os.system(f"adb shell '{command_str}'")


if __name__ == "__main__":
    main()
