'''s = "DDEEBWLJFKWPJLZQNRQJ"
#s = "NJDTRNH"
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                'Z', ' ']

"""a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                'Z', ' ', '.', ',', ';', '!', '?', '(', ')', '-', '\'', '\\', '"']"""
l = []
for i in range(len(s)-4):
    if ord(s[i]) + 4 == ord(s[i+4]):
        l.append(i+1)
        print(s[i], s[i+4])
loc = -1
n = 0
b = True
c = 0
print(l)
"""for i in l:
    for j in range(i, i + 3):
        if j == i:
            print("j==i", j)
            #if i <= 19:
            n = 19 - i
            print("n", n)
            #else:
            #    n = 
        else:
            print("ord(s[j])", a.index(s[j]))
            c = (a.index(s[j]) + n) % (26+j)
            #print(i, c, a[c])
            print(a.index(s[j]) + n)
            if j == i + 1 and a[c] != 'H':
                b = False
                break
            if j == i + 2:
                if a[c] != 'E':
                    b = False
                    break
                else:
                    loc = i

print("loc", loc, s[loc:loc+3])"""
'''

s = "FEED THE DOG AND CAT"
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
'Z', ' ']

r1 = 0
r2 = 25
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