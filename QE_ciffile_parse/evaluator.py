import numpy as np

def evaluate_symmetry_equals(x,y,z,symm_list):
    symm_list = np.array(symm_list)
    symm_eq_pos = np.zeros(symm_list.shape)
    for iter_item1 in range(0,symm_eq_pos.shape[0]):
        for iter_item2 in range(0,symm_eq_pos.shape[1]):
            symm_eq_pos[iter_item1,iter_item2] = eval(symm_list[iter_item1,iter_item2])
    return symm_eq_pos

x = 5
y = 1
z = 8
symm_list = [['x',' y',' z'],
              ['z',' x',' y'],
              ['y',' z',' x'],
              ['-y',' -z',' x'],
              ['z',' -x',' -y'],
              ['-y',' z',' -x'],
              ['-z',' -x',' y'],
              ['-z',' x',' -y'],
              ['y',' -z',' -x'],
              ['-x',' -y',' z'],
              ['x',' -y',' -z'],
              ['-x',' y',' -z']]
print(evaluate_symmetry_equals(x,y,z,symm_list))
