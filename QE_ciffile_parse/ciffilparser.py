import re


def FileParser(File_name,search_word,splitter):
    with open(File_name) as origin_file:
        for line in origin_file:

            line = re.findall(rf'{search_word}.*', line)
            if line:
               line = line[0].split("{}".format(splitter))[1]
            if len(line) != 0:
                print(line)


FileParser("Test.cif","_symmetry_space_group_name_H-M","'")