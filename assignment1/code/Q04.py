import re
import hashlib

f = open("words.txt")
w = open("password.txt", 'w')
result = {}

def l33t(str):
    for s in str:
        str = re.sub('a', '4', str)
        str = re.sub('e', '3', str)
        str = re.sub('i', '1', str)
        str = re.sub('o', '0', str)
    return str

for line in f:
    line = line.strip()
    line_t = l33t(line)
    w.write(line_t+"\n")

f.close()
w.close()

with open("password.txt","rb") as w:
    sha256obj = hashlib.sha256()
    sha256obj.update(w.read())
    hash_value = sha256obj.hexdigest()
    print(hash_value)



