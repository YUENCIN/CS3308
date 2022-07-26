f = open("secret.txt", "r")

def recover(secret: str):
    index, content = secret.split(":", 1)
    p = int(index)
    l = 100 - p
    content = content[p:p + 1]
    return content

plaintext = []

for line in f:
    plaintext.append(recover(line))
res = "".join(plaintext)
print(res)
