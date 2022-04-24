# space before A is at 68
f = open("encrypt.txt")
es = f.read()
f.close()

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ' ', '.', ',', ';', '!', '?', '(', ')', '-', '\'', '"']

def encrypt(a, s, r1 = 0, r2 = 47):
    e = 0
    string = ""
    for chr in s:
            e = (a.index(chr) + r1 + r2) % len(a)
            string += a[e]
            r1 += 1
            if r1 % len(a) == len(a) - 1:
                r2 += 1

    return string

'''
firstRotor = 46
secondRotor = 19
es = encrypt(a, s, firstRotor, secondRotor)
print(es)
'''


def count(es, num):
    num = num + 1
    l = []
    for i in range(100):
        if(i == len(a)):
            num += 1
        if ord(es[i]) + num == ord(es[i+num]):
            l.append(i)
            #print(s[i], s[i+num])
    print(l)
    return l

indices = count(es, 1)
print()
num = 0
num2 = 0
found = False
for i in indices:
    r1 = a.index(es[i]) - (a.index(" ") + i)
    #print(r1)
    #print(36 - )
    num = r1 % len(a)
    print("r1:", num)
    #print("a" + a[(a.index(" ") + r1 + i) % 48] + "b")

    r2 = a.index(es[i+1]) - (0 + i+1)
    num2 = r2 % len(a)
    print("r2:", num2)
    print()
    #print((3-5) % 27)

    #print(es[i])
    #print((36 + i + 47) % 48)
    #print(a[(36 + i + 47) % 48])

    if(num == r2 % len(a)):
        found = True
        break

found = True
num = 63
if found:
    decrypted = ""
    index = 0
    for i in range(len(es)):
        # initial = (encrypted - (rotors + slide)) % 47
        index = (a.index(es[i]) - (num + i)) % len(a)
        decrypted += a[index]

    print()
    print(decrypted)
    print()

    tup = (-1, -1)

    for p in range(len(a)):
        for q in range(len(a)):
            if(encrypt(a, decrypted, p, q) == es):
                tup = (p, q)

    print(tup)