N = int(input())
A = list(map(int, input().split()))

# P が最終的に作りたい順列
P = [-1] * N

# すでに使われた数字を記録する集合
used = set()

# ① 固定されている値を入れる & 重複チェック
for i in range(N):
    if A[i] != -1:
        # すでに同じ数字が使われていたらアウト
        if A[i] in used:
            print("No")
            exit()
        P[i] = A[i]
        used.add(A[i])

# ② まだ使われていない数字を集める
remain = []
for x in range(1, N + 1):
    if x not in used:
        remain.append(x)

# ③ -1 の場所を残りの数字で埋める
idx = 0
for i in range(N):
    if P[i] == -1:
        P[i] = remain[idx]
        idx += 1

# ④ 出力
print("Yes")
print(*P)
