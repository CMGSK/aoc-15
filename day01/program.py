file=open("input.txt")
data=file.read()
if data=="": 
    print("Reading error")

floor=0
basement=0
for i in range(0, len(data)):
    floor = floor+1 if data[i]=="(" else floor-1
    if basement==0 and floor<0:
        basement=i+1 #we start at index 1 for the result

print(floor)
print(basement)

