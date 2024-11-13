def file_line_sort(f_list):
    f_count_line = dict()
    for file_ in f_list:
        with open(file_, "r", encoding='utf-8') as f_from_list:
            f_count_line[file_] = len(f_from_list.readlines())
    return dict(sorted(f_count_line.items(), key=lambda item: item[1]))               


def file_itog(dict_s, f_itog):
    with open(f_itog, "a", encoding='utf-8') as file_itog:
        for key, value in dict_s.items():
            file_itog.write(key + "\n")
            file_itog.write(str(value) + "\n")
            file_in = open(key,'r', encoding='utf-8')
            content = file_in.read()
            file_itog.write(content + "\n")
            file_in.close()


files_list = ["1.txt", "2.txt", "3.txt"]
dict_sort = file_line_sort(files_list)

file_itog(dict_sort, "4.txt")