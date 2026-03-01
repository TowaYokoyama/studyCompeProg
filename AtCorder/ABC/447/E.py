"""
問題文
N 頂点 M 辺からなる単純連結無向グラフ G が与えられます。 ここで、N≥2 です。 頂点には 1 から N までの、辺には 1 から M までの番号がそれぞれ付けられており、辺 i は頂点 U 
i
​	
  と頂点 V 
i
​	
  を結んでいます。 また、各辺には コスト とよばれる値が定められており、辺 i のコストは 2 
i
  です。

あなたは今から、G の連結成分の個数がちょうど 2 になるように、G の辺のうちいくつかを選んで削除します。 （なお、本問題の制約下でこれは必ず達成可能であることが証明できます。）

削除する辺のコストの和としてありうる最小値を 998244353 で割った余りを求めてください。 （998244353 で割った余りを最小化するのではないことに注意してください。）

制約
2≤N≤2×10 
5
 
N−1≤M≤min( 
2
N(N−1)
​	
 ,2×10 
5
 )
1≤U 
i
​	
 <V 
i
​	
 ≤N
i

=j ならば (U 
i
​	
 ,V 
i
​	
 )

=(U 
j
​	
 ,V 
j
​	
 )
G は連結
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
U 
1
​	
  V 
1
​	
 
U 
2
​	
  V 
2
​	
 
⋮
U 
M
​	
  V 
M
​	
 
出力
削除する辺のコストの和としてありうる最小値を 998244353 で割った余りを出力せよ。

入力例 1
Copy
5 7
2 3
1 2
1 5
4 5
2 4
3 5
1 3
出力例 1
Copy
22


辺 1,2,4 の 3 本の辺（上図において点線で示されている辺）を削除すると、G の連結成分の個数はちょうど 2 になります。

このとき、削除する辺のコストの和は 2 
1
 +2 
2
 +2 
4
 =22 であり、これが最小です。

入力例 2
Copy
2 1
1 2
出力例 2
Copy
2
入力例 3
Copy
8 16
2 7
5 7
6 8
1 7
4 7
1 3
2 8
5 8
4 8
2 5
3 4
3 8
1 4
1 8
4 6
1 2
出力例 3
Copy
54
"""
from collections import defaultdict

# https://note.nkmk.me/python-union-find/
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


n, m = map(int, input().split())
u = []
v = []
for _ in range(m):
    u_i, v_i = map(int, input().split())
    u.append(u_i - 1)
    v.append(v_i - 1)

graph = UnionFind(n)

ans = 0
group_count = n
for i in range(m - 1, -1, -1):
    if graph.same(u[i], v[i]):
        continue
    if group_count > 2:
        graph.union(u[i], v[i])
        group_count -= 1
    else:
        ans += 1 << (i + 1)

print(ans % 998244353)
