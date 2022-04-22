f = open("encrypt.txt")
s2 = f.read()
f.close()
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ' ', '.', ',', ';', '!', '?', '(', ')', '-', '\'', '\\', '"']

print(len(a))

s = "ALAN TURING WAS A COMPUTER"
print(len(s))

def encrypt(a, s, r1 = 0, r2 = 25):
    e = 0
    l = []
    for chr in s:
            e = (a.index(chr) + r1 + r2) % len(a)
            l.append(e)
            r1 += 1
            if r1 % len(a) == len(a) - 1:
                r2 += 1


    for i in l:
        print(a[i], end='')

    print()

encrypt(a, s)


def count(s, num):
    num = num + 1
    l = []
    for i in range(len(s)-num):
        if ord(s[i]) == ord(s[i+num]):
            l2.append(i)
            #print(s[i], s[i+num])
    print(l2)


'''
l2 = []
for i in range(len(s)-2):
    if ord(s[i]) == ord(s[i+2]):
        l2.append(i)
        #print(s[i], s[i+2])
print(l2)

l3 = []

for i in range(len(s)-4):
    if ord(s[i]) == ord(s[i+4]):
        l3.append(i)
        #print(s[i], s[i+4])
print(l3)
'''



"""s = "HELLO BOB. A CAT"
# blanks: 5, 10, 12
l = []
e = 0
r1 = 0
r2 = 25
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ' ', '.', ',', ';', '!', '?', '(', ')', '-', '\'', '\\', '"']
for chr in s:
    if chr != '\n':
        e = (a.index(chr) + r1 + r2) % len(a)
        l.append(e)
        r1 += 1
        if r1 % len(a) == len(a) - 1:
            r2 += 1
    else:
        l.append(-1)


'''for i in l:
    if i == -1:
        print()
    else:
        print(a[i], end='')
print()'''
s2 = ''.join([a[elem] for elem in l])
print(s2)
print(s)
print("length:", len(s))
l2 = []
for i in range(len(s)-2):
    if ord(s[i]) == ord(s[i+2]):
        l2.append(i)
        print(s[i], s[i+2])
print(l2)
"""
