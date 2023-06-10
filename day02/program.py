file=open("input.txt")
wrapping=0
ribbon=0
for line in file:
    dim=line.split("x")

    h2=int(dim[0])*int(dim[1])
    l2=int(dim[0])*int(dim[2])
    w2=int(dim[1])*int(dim[2])
    wrapping += h2*2+l2*2+w2*2+min(h2,l2,w2)

    h=int(dim[0])
    l=int(dim[1])
    w=int(dim[2])
    ribbon += (h*l*w)+min((h+h+w+w),(h+h+l+l),(w+w+l+l))

print(wrapping)
print(ribbon)
