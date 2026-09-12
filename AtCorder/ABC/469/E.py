N, K = map(int, input().split())
S = list(input())

left = 0
right = 1.001
for _ in range(30):
    mid = (left + right) * 0.5

    A = [1-mid if S[i] == "o" else -mid for i in range(N)]
    Asum = [0]
    for i in range(N):
        Asum.append(Asum[-1] + A[i])

    Asum_min = [0]
    for i in range(N):
        Asum_min.append(min(Asum_min[-1], Asum[i]))

    l = 0
    k = 0
    f = False
    for r in range(N):
        if S[r] == "o":
            k += 1

        while k >= K and l < r:
            if S[l] == "x":
                l += 1
            else:
                if k == K:
                    break
                else:
                    k -= 1
                    l += 1

        if k >= K:
            if Asum[r+1] >= Asum_min[l+1]:
                f = True
                break

    if f:
        left = mid
    else:
        right = mid

print(left)
