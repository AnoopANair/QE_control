import re
import numpy as np


set_of_words = np.array([])
with open("Test.cif") as origin_file:
    for line in origin_file:
        set_of_words = np.append(set_of_words,line)
set_of_words = set_of_words[::-1]

def find_index(search_word,set_of_words):
    count = 0
    for i in set_of_words:
        line = re.findall(rf'{search_word}.*', i)
        if line:
            return count
        count += 1

index = find_index("loop_",set_of_words)

words = ["_atom_site_label","_atom_site_type_symbol","_atom_site_fract_x","_atom_site_fract_y","_atom_site_fract_z","_atom_site_occupancy","_atom_site_U_iso_or_equiv"]


terms = set_of_words[:index].copy()
terms = terms[::-1]
wyckoff_dict = {}

for term in words:
    index_number = find_index(term,terms)
    wyckoff_dict[index_number] = term


max_key = len(wyckoff_dict)
new_set_of_words = terms[max_key:index].copy()

temp_array = np.zeros((1,max_key))

for value in new_set_of_words:
    temp_val = value.split("{}".format(' ')) # change this to regex
    if len(temp_val) == max_key:
        
        temp_array = np.vstack((temp_array,temp_val))


temp_array = temp_array[1:]

temp_array[:,-1]

for k in range(0,len(temp_array[:,-1])):
    temp_array[k,-1] = temp_array[k,-1].replace('\n','')



final_wycoff_dict = {}
for j in range(0,max_key):
    final_wycoff_dict[wyckoff_dict[j]] = temp_array[:,j]


print(final_wycoff_dict["_atom_site_occupancy"])
