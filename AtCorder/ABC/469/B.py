"""
<方針>
- 番兵 `x` をつけて、判定すれば良い。
"""
# 入力
N = int(input())
S = input()

# 番兵
S = "x" + S + "x"

ans = 0
for i in range(1, N+1):
  if(S[i-1] == S[i] == S[i+1] == "x"):
    ans += 1

# 出力
print(ans)
