import re


def FileParser(File_name,search_word,splitter):
    with open(File_name) as origin_file:
        for line in origin_file:

            line = re.findall(rf'{search_word}.*', line)
            if line:
               line = line[0].split("{}".format(splitter))
            if len(line) != 0:
                    line = [x for x in line if (x != '')]
                    line = [x for x in line if (x != "'")]
                    print(line)

List_to_searched =["chemical_formula_sum","","space_group_IT_number","symmetry_space_group_name_Hall","symmetry_space_group_name_H-M","cell_angle_alpha","cell_angle_beta","cell_angle_gamma","cell_formula_units_Z","cell_length_a","cell_length_b","cell_length_c","cod_database_code"]               


FileParser("Test.cif","symmetry_space_group_name_Hall","'")