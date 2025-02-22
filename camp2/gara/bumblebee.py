s1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}!(),.-+?"
s2 = "OovI7yaMg5Q}K3kLWVSZweN9?A6Pd+(piJTGjc1mrUl)XhCEztfH-84{0FD,.xBqnRY2b!us"

permtable = {i: s2.index(char) for i, char in enumerate(s1)}

permflag = "zomrgiziomiiBolooi}i!agoBiBoioiomigozizgfrzonminiionB!ozpzr{ig!zpoiooir!"

flag = list(range(72))
for i, c in enumerate(permflag):
    flag[permtable[i]] = permflag[ i ]

print(''.join(flag))