import random
from flag import flag

key = "This needs to be private lol"

for i in range(len(key)):
    ciphertext = ""
    for j in range(len(flag)):
        ciphertext += chr(ord(flag[j]) ^ ord(key[i]));
