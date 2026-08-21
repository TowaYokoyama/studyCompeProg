"""
<方針>
- 一個前の個数が分かれば、それに一つ足してあげて、あとは、あたりを引き続ける限り加算していけば良い。
"""
N = int(input())
S = input()

ans = 0
for _ in range(N):
  # 一つ足す
  ans += 1
  # あたりを引き続ける限り加算
  while (ans <= N) and (S[ans-1] == "o"):
    ans += 1
  
  # 調整
  ans = min(ans, N)
  print(ans)
