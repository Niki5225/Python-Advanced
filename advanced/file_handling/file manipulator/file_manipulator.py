from os.path import exists
from os import remove

while True:
    line = input()
    if line == "End":
        break
    command_parts = line.split("-")
    command, file_name = command_parts[0], command_parts[1]

    if command == "Create":
        with open(f"{file_name}", 'w'):
            pass
    elif command == "Delete":
        if not exists(file_name):
            print("An error occurred")
            continue
        remove(file_name)
    elif command == "Add":
        content = command_parts[2]
        with open(f"{file_name}", "r+") as file:
            file.write(content + "\n")
    elif command == "Replace":
        old_str, new_str = command_parts[2], command_parts[3]
        if not exists(file_name):
            print("An error occurred")
            continue
        with open(f"{file_name}", "r+") as file:
            file_content = file.read().replace(old_str, new_str)
            file.seek(0)
            file.truncate()
            file.write(file_content)
