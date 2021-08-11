import cv2
import numpy as np
from encrypt import encrpytion

def img_process(input_Dir,e,N):
    img = cv2.imread(input_Dir)
    resized_img = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)
    img = np.array(resized_img)
    np_array_list = list(img)
    input_data=[]
    for i in range(0,100):
        for j in range(0,100):
            for k in range(0,3):
                input_data.append(int(np_array_list[i][j][k]))
    
    data_ciphered = []
    for i in input_data:
        data_ciphered.append(encrpytion(i,e,N))
    
    return data_ciphered
