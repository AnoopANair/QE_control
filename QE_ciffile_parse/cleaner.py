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
  
dict_one = {
 1 : 'P 1',
                2 : '-P 1',
                16 : 'P 2 2',
                19 : 'P 2ac 2ab',
                22 : 'F 2 2',
                23 : 'I 2 2',
                24 : 'I 2b 2c',
                47 : '-P 2 2',
                69 : '-F 2 2',
                71 : '-I 2 2',
                75 : 'P 4',
                76 : 'P 4w',
                77 : 'P 4c',
                78 : 'P 4cw',
                79 : 'I 4',
                80 : 'I 4bw',
                81 : 'P -4',
                82 : 'I -4',
                83 : '-P 4',
                84 : '-P 4c',
                87 : '-I 4',
                89 : 'P 4 2',
                90 : 'P 4ab 2ab',
                91 : 'P 4w 2c',
                92 : 'P 4abw 2nw',
                93 : 'P 4c 2',
                94 : 'P 4n 2n',
                95 : 'P 4cw 2c',
                96 : 'P 4nw 2abw',
                97 : 'I 4 2',
                98 : 'I 4bw 2bw',
                99 : 'P 4 -2',
                100 : 'P 4 -2ab',
                101 : 'P 4c -2c',
                102 : 'P 4n -2n',
                103 : 'P 4 -2c',
                104 : 'P 4 -2n',
                105 : 'P 4c -2',
                106 : 'P 4c -2ab',
                107 : 'I 4 -2',
                108 : 'I 4 -2c',
                109 : 'I 4bw -2',
                110 : 'I 4bw -2c',
                111 : 'P -4 2',
                112 : 'P -4 2c',
                113 : 'P -4 2ab',
                114 : 'P -4 2n',
                115 : 'P -4 -2',
                116 : 'P -4 -2c',
                117 : 'P -4 -2ab',
                118 : 'P -4 -2n',
                119 : 'I -4 -2',
                120 : 'I -4 -2c',
                121 : 'I -4 2',
                122 : 'I -4 2bw',
                123 : '-P 4 2',
                124 : '-P 4 2c',
                127 : '-P 4 2ab',
                128 : '-P 4 2n',
                131 : '-P 4c 2',
                132 : '-P 4c 2c',
                135 : '-P 4c 2ab',
                136 : '-P 4n 2n',
                139 : '-I 4 2',
                140 : '-I 4 2c',
                143 : 'P 3',
                144 : 'P 31',
                145 : 'P 32',
                147 : '-P 3',
                149 : 'P 3 2',
                150 : 'P 3 2"',
                151 : 'P 31 2c (0 0 1)',
                152 : 'P 31 2"',
                153 : 'P 32 2c (0 0 -1)',
                154 : 'P 32 2"',
                156 : 'P 3 -2"',
                157 : 'P 3 -2',
                158 : 'P 3 -2"c',
                159 : 'P 3 -2c',
                162 : '-P 3 2',
                163 : '-P 3 2c',
                164 : '-P 3 2"',
                165 : '-P 3 2"c',
                168 : 'P 6',
                169 : 'P 61',
                170 : 'P 65',
                171 : 'P 62',
                172 : 'P 64',
                173 : 'P 6c',
                174 : 'P -6',
                175 : '-P 6',
                176 : '-P 6c',
                177 : 'P 6 2',
                178 : 'P 61 2 (0 0 -1)',
                179 : 'P 65 2 (0 0 1)',
                180 : 'P 62 2c (0 0 1)',
                181 : 'P 64 2c (0 0 -1)',
                182 : 'P 6c 2c',
                183 : 'P 6 -2',
                184 : 'P 6 -2c',
                185 : 'P 6c -2',
                186 : 'P 6c -2c',
                187 : 'P -6 2',
                188 : 'P -6c 2',
                189 : 'P -6 -2',
                190 : 'P -6c -2c',
                191 : '-P 6 2',
                192 : '-P 6 2c',
                193 : '-P 6c 2',
                194 : '-P 6c 2c',
                195 : 'P 2 2 3',
                196 : 'F 2 2 3',
                197 : 'I 2 2 3',
                198 : 'P 2ac 2ab 3',
                199 : 'I 2b 2c 3',
                200 : '-P 2 2 3',
                202 : '-F 2 2 3',
                204 : '-I 2 2 3',
                205 : '-P 2ac 2ab 3',
                206 : '-I 2b 2c 3',
                207 : 'P 4 2 3',
                208 : 'P 4n 2 3',
                209 : 'F 4 2 3',
                210 : 'F 4d 2 3',
                211 : 'I 4 2 3',
                212 : 'P 4acd 2a 3',
                213 : 'P 4bd 2ab 3',
                214 : 'I 4bd 2c 3',
                215 : 'P -4 2 3',
                216 : 'F -4 2 3',
                217 : 'I -4 2 3',
                218 : 'P -4n 2 3',
                219 : 'F -4c 2 3',
                220 : 'I -4bd 2c 3',
                221 : '-P 4 2 3',
                223 : '-P 4n 2 3',
                225 : '-F 4 2 3',
                226 : '-F 4c 2 3',
                229 : '-I 4 2 3',
                230 : '-I 4bd 2c 3'
    }

# Appending to file 
with open("myfile1.txt", 'a') as file1: 
    for i in dict_one.keys():
        key = Hall_format(str(i))
        value = Hall_format(dict_one[i])
        file1.write("{}:'{}',\n".format(key,value)) 