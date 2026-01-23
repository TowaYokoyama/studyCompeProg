x, y, z = map(int, input().split())

# y が負なら、全体を反転
if y < 0:
    x = -x
    y = -y
    z = -z

if x < y:
    print(abs(x))
else:
    if z > y:
        print(-1)
    else:
        print(abs(z) + abs(x - z))
