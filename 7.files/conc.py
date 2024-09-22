import os

directory = "./txts/"
filenames = os.listdir(directory)


def get_lines_num(file_info):
    return file_info["lines_num"]


files_info = []
for fname in filenames:
    with open(f"{directory}{fname}", "r") as file:
        lin = file.read()
        files_info.append(
            {"name": fname, "lines": lin, "lines_num": len(lin.split("\n"))}
        )

sorted_files = sorted(files_info, key=get_lines_num)
with open("result.txt", "a") as result:
    for i in sorted_files:
        stri = "Название файлда: {}\nКоличество строк: {}\n{}\n{}\n"
        result.write(stri.format(i["name"], i["lines_num"], i["lines"], "-" * 76))
