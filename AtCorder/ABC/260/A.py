from collections import Counter
S = input()
a = Counter(S)

for i in a:
    if a[i] == 1:
        print(i)
        exit()

print(-1)