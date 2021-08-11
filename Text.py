from decrypt import decrpytion

def text_process(input_Dir,d,N):
    with open(input_Dir) as f:
        line = f.readline()
    f.close()
    line = line[1:len(line)-1]
    line_list = list(line.split(","))
    data_ciphered = []
    for i in line_list:
        data_ciphered.append(int(i))
    data_deciphered = []
    for i in data_ciphered:
        data_deciphered.append(decrpytion(i,d,N))
    return data_deciphered