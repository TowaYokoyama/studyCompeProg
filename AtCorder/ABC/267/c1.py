N, M = map(int, input().split())
A = list(map(int, input().split()))

# ① 最初の区間を作る
res = 0          # 重み付き和
window_sum = 0   # 区間の合計

for i in range(M):
    res += (i+1) * A[i]
    window_sum += A[i]

ans = res

# ② 区間を右にずらす
for r in range(M, N):
    # 1つ右にスライド
    res -= window_sum        # 係数が1ずつ減る分を引く
    window_sum -= A[r-M]     # 左端が消える

    res += M * A[r]          # 新しく入る要素はM倍
    window_sum += A[r]       # 合計も更新

    ans = max(ans, res)

print(ans)
