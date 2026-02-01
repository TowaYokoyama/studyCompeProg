from collections import deque

n = int(input())
INF = 10**9
d = [INF] * (10 * n)
to = [-1] * (10 * n)
d[0] = 0
q = deque([0])
while q:
    idx = q.popleft()
    c, x = idx % 10, idx // 10
    for cc in range(max(1, c), 10):
        xx = (10 * x + cc) % n
        idx2 = 10 * xx + cc
        if d[idx2] != INF:
            break
        d[idx2] = d[idx] + 1
        q.append(idx2)
        to[idx2] = idx
        if xx == 0:
            ans = []
            cur = idx2
            while cur != 0:
                ans.append(str(cur % 10))
                cur = to[cur]
            print("".join(ans[::-1]))
            exit()
print(-1)
