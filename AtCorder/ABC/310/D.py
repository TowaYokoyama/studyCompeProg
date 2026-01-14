"""
AtCorder.ABC.310.D の Docstring
N 人のスポーツ選手がいます。

N 人の選手たちには互いに相性の悪い選手のペアが M 組あり、相性の悪い組のうち i (1≤i≤M) 組目は A 
i
​	
  番目の選手と B 
i
​	
  番目の選手です。

あなたは、選手を T チームに分けます。 どの選手もちょうど一つのチームに属さなければならず、どのチームにも少なくとも一人の選手が属さなければなりません。 さらに、どの i=1,2,…,M についても、 A 
i
​	
  番目の選手と B 
i
​	
  番目の選手が同じチームに属していてはいけません。

この条件を満たすチーム分けの方法は何通りあるか求めてください。 ただし、チーム分けの方法が異なるとは、ある二人が存在して、彼らが一方のチーム分けでは同じチームに所属し、もう一方では異なるチームに所属することをいいます。

制約
1≤T≤N≤10
0≤M≤ 
2
N(N−1)
​	
 
1≤A 
i
​	
 <B 
i
​	
 ≤N (1≤i≤M)
(A 
i
​	
 ,B 
i
​	
 )

=(A 
j
​	
 ,B 
j
​	
 ) (1≤i<j≤M)
入力はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

N T M
A 
1
​	
  B 
1
​	
 
A 
2
​	
  B 
2
​	
 
⋮
A 
M
​	
  B 
M
​	
 
出力
答えを 1 行で出力せよ。

入力例 1
Copy
5 2 2
1 3
3 4
出力例 1
Copy
4
次の 4 通りのチーム分けが条件を満たします。



他に条件を満たすチーム分けは存在しないので、4 を出力してください。

入力例 2
Copy
5 1 2
1 3
3 4
出力例 2
Copy
0
条件を満たすチーム分けがひとつも存在しないこともあります。

入力例 3
Copy
6 4 0
出力例 3
Copy
65
相性の悪いペアがひとつも存在しないこともあります。

入力例 4
Copy
10 6 8
5 9
1 4
3 8
1 6
4 10
5 7
5 6
3 7
出力例 4
Copy
8001
"""
import sys
sys.setrecursionlimit(10**7)

N, T, M = map(int, sys.stdin.readline().split())

# badmask[i] の j ビットが 1 なら「i と j は同じチーム不可」
badmask = [0] * N
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    badmask[a] |= 1 << b
    badmask[b] |= 1 << a

ans = 0

# groups: 各チームのメンバー集合を bitmask で持つ（空チームは作らない）
# idx: 次に割り当てる選手番号（0-index）
def dfs(idx, groups):
    global ans

    # 全員割り当てた
    if idx == N:
        if len(groups) == T:
            ans += 1
        return

    gcnt = len(groups)
    rem = N - idx

    # もうチーム数が多すぎる
    if gcnt > T:
        return
    # 残り人数を全部新チームにしてもTに届かない
    if gcnt + rem < T:
        return

    # 既存チームに入れる（入れられるところだけ）
    for k in range(gcnt):
        g = groups[k]
        # idx がこのチームの誰とも相性悪くないならOK
        if (badmask[idx] & g) == 0:
            groups[k] = g | (1 << idx)
            dfs(idx + 1, groups)
            groups[k] = g  # 戻す

    # 新しいチームを作る（ただし作れるのは最大 T 個まで）
    # これを「最後」にしか作らないことで、チームの入れ替え重複を防ぐ
    if gcnt < T:
        groups.append(1 << idx)
        dfs(idx + 1, groups)
        groups.pop()

# 対称性除去：選手0は必ず最初のチームに入れる（チームの順番入れ替えをさらに潰す）
dfs(1, [1 << 0])

print(ans)
