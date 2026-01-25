n, q = map(int, input().split())
A = list(map(int, input().split()))

seg = SegTree(A)

for _ in range(q):
    t, *rest = input().split()

    if t == "1":
        x = int(rest[0]) - 1  # 0-index
        # swap
        A[x], A[x+1] = A[x+1], A[x]
        seg.update(x, A[x])
        seg.update(x+1, A[x+1])

    else:
        l, r = map(int, rest)
        print(seg.query(l-1, r))
