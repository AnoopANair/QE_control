import re 
  
def remove_white_space(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string) 

def Hall_format(input_hall):
    output_hall = remove_white_space(input_hall)
    output_hall = output_hall.lower()
    return output_hall

input_hall = "-P 6c 2c"
print(Hall_format(input_hall))