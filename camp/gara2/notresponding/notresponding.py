from collections import defaultdict

with open("output.txt", "r") as f:
    lines = f.readlines()

a = defaultdict(list)
for i in lines:
    a[int(i.split(',')[0].split('=')[-1].strip())].append(i.split(',')[-1].split('=')[-1].strip())
a = dict(sorted(a.items()))

s = [""]*4
for i in a.keys():
    for j, c in enumerate(a[i]):
        s[j] += c

print(s)