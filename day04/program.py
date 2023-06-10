import hashlib

data = "yzbqklnj"
i=0
part1=False
while True:
    h = data + str(i)
    res = hashlib.md5(h.encode()).hexdigest()
    if res[0:5] == 5*'0' and not part1 :
        print(i)
        part1 = True
    if res[0:6] == 6*'0':
        print(i)
        break
    i+=1
