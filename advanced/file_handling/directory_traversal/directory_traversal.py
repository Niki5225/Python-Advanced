from os.path import isdir, join
from os import listdir


def directory_traversal(path, files_by_ext):
    for el in listdir(path):
        if isdir(join(path, el)):
            directory_traversal(join(path, el), files_by_ext)
        else:
            extension = el.split()[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(el)


result = {}
directory_traversal("../", result)
with open("result.txt", "w") as output_file:
    sorted_dict = sorted(result.items(), key=lambda x: (x[0], x[1]))
    for ext, files in result.items():
        output_file.write(f"{ext}\n")
        for file in files:
            output_file.write(f"- - - {file}\n")
