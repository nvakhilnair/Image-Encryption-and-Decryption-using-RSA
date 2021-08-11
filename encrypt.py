def encrpytion(data,e,N):
    cipher = pow(data,e)%N
    return cipher