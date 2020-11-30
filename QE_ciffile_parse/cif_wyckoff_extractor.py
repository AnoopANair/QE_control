import re
import numpy as np

"""
Pseudo code:
1. Taking the array of lines
2. Invert it
3. Match the first occurence of loop_
4. slice till the index
5. new list  == sliced list inverted
6. find index of keywords within sliced list
7. find max index
8. remove the '\ n' and ' ' charachter lines
9. rematch the indices of the key_words
10. match the coloumn to the index of the last value arrays
"""
def find_index(search_word,set_of_words):
    count = 0
    for i in set_of_words:
        line = re.findall(rf'{search_word}.*', i)
        if line:
            return count
        count += 1

# step 1
file_lines = np.array([])
with open("Test.cif") as origin_file:
    for line in origin_file:
        file_lines = np.append(file_lines,line)


# step 3
key_words = ["_atom_site_label","_atom_site_type_symbol","_atom_site_fract_x","_atom_site_fract_y","_atom_site_fract_z","_atom_site_occupancy","_atom_site_U_iso_or_equiv"]

# step 4
inital_term_space = file_lines.copy()



temp_dict = {} # define the dictionary

# step 6
for iter_term in key_words:
    index_number = find_index(iter_term,inital_term_space)
    if index_number != None :
        temp_dict[index_number] = iter_term

min_key  = int(min(temp_dict.keys()))
max_key  = int(max(temp_dict.keys()))


# # step 8
for iter_term in range(0,len(inital_term_space[:max_key+1])):
    inital_term_space[iter_term] = inital_term_space[iter_term].replace(" ",'')

final_term_space = [k for k in inital_term_space[min_key:max_key+1] if k != '\n']
print(final_term_space)
# step 9
temp_dict_one = {}

for iter_term in key_words:
    index_number = find_index(iter_term,final_term_space)
    if index_number != None:
        temp_dict_one[index_number] = iter_term

# step 10
max_index_number = len(temp_dict_one)
value_lines = inital_term_space[max_key+1:].copy()

# defining dummy array for vstack
temp_array = np.zeros((1,max_index_number)) 

for iter_term in value_lines:
    temp_val = iter_term.split("{}".format(' ')) # change this to regex
    if len(temp_val) == max_index_number:
        temp_array = np.vstack((temp_array,temp_val))
    else :
        break


temp_array = temp_array[1:]

temp_array[:,-1]

for k in range(0,len(temp_array[:,-1])):
    temp_array[k,-1] = temp_array[k,-1].replace('\n','')

print(temp_dict_one)
final_dict = {}
for iter_term in range(0,len(temp_dict_one)):
    print(iter_term)
    final_dict[temp_dict_one[iter_term]] = temp_array[:,iter_term]

print(final_dict)