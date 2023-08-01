import re


def cont(input):
    for i in range(len(input) - 2):
        if input[i] + input[i + 1] + input[i + 2] in 'abcdefghijklmnopqrstuvwxyz':
            return True
    return False


def iol(input):
    if any(('i', 'o', 'l') for c in input):
        return False
    return True


def reg(input):
    m = re.search('.*([a-z])\1.*([a-z])\2.*', input)
    if m == None:
        return False
    return True


og = 'hxbxwxba'
input = og
initial_state = int(len(input)/2)
first_half = input[:initial_state]
second_half = input[initial_state:]

ok = False
second_half = chr(ord(first_half[len(first_half) - 1])) + second_half[1:]
while (not ok):
    last = len(second_half) - 1
    while (second_half[last] == 'z'):
        second_half = second_half[:last] + 'a' + second_half[last + 1:]
        last -= 1
    second_half = second_half[:last] + chr(ord(second_half[last]) + 1) + second_half[last + 1:]
    print(first_half + second_half)
    if(len(first_half + second_half) != 8):
        input = og
        first_half = input[:initial_state-1]
        second_half = input[initial_state+1:]
    ok = cont(first_half + second_half) and reg(first_half + second_half) and iol(first_half + second_half)
print('Result: ' + first_half + second_half)
