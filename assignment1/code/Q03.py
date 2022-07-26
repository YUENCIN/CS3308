import hashlib
import os
path = "Q03"
files= os.listdir(path)
key = "a92536e3c31979736460be6e6729147f974411ef193629999b022b96f5682450"
for file in files:
     if not os.path.isdir(file):
          f = open(path+"/"+file)
          iter_f = iter(f)
          str = ""
          for line in iter_f:
              str = str + line
              hash = hashlib.sha256(str.encode('utf-8')).hexdigest()
              if hash == key:
                  print(f.name)


