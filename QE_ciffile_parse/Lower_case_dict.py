
# Code to convert dict keys and values into lower case
import re 


  
def remove_white_space(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string) 

def Hall_format(input_hall):
    output_hall = remove_white_space(input_hall)
    output_hall = output_hall.lower()
    return output_hall


with open("myfile.txt", "w") as file1: 
    # Writing data to a file 
    file1.write("Hello \n") 

# specify the dict to convert
dict_one = { }

# Appending to file 
with open("myfile1.txt", 'a') as file1: 
    for i in dict_one.keys():
        key = Hall_format(str(i))
        value = Hall_format(dict_one[i])
        file1.write("{}:'{}',\n".format(key,value)) 
