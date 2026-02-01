a = []
for _ in range(4):
    s = input()
    a.append(s)
if len(set(a)) == 4:
    print("Yes")
else:
    print("No")