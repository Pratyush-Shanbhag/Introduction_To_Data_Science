s = "HELLO BOB. A CAT"
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
