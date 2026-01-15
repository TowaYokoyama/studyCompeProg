"""
AtCorder.ABC.432.D の Docstring
問題文
無限に広がる二次元グリッドがあります。マス (x,y) の色は、0≤x≤X−1 かつ 0≤y≤Y−1 ならば黒であり、そうでなければ白です。

このグリッドに対して N 個の大嵐が順に発生します。i 回目の大嵐は、文字 C 
i
​	
  と整数 A 
i
​	
 ,B 
i
​	
  で表される法則にしたがって、グリッド上の各マスの色を更新します。

i 回目の大嵐において、大嵐が起きた後のマス (x,y) の色は、

C 
i
​	
  が X の場合、
x<A 
i
​	
  ならば、大嵐が起きる前のマス (x,y+B 
i
​	
 ) の色になる。
x≥A 
i
​	
  ならば、大嵐が起きる前のマス (x,y−B 
i
​	
 ) の色になる。
C 
i
​	
  が Y の場合、
y<A 
i
​	
  ならば、大嵐が起きる前のマス (x+B 
i
​	
 ,y) の色になる。
y≥A 
i
​	
  ならば、大嵐が起きる前のマス (x−B 
i
​	
 ,y) の色になる。
2 つの黒いマス (x 
1
​	
 ,y 
1
​	
 ),(x 
2
​	
 ,y 
2
​	
 ) が隣接しているとは、∣x 
1
​	
 −x 
2
​	
 ∣+∣y 
1
​	
 −y 
2
​	
 ∣=1 が満たされることを指します。また、2 つの黒いマス c 
1
​	
 ,c 
2
​	
  が連結であるとは、隣接する黒いマスへの移動を繰り返すことでマス c 
1
​	
  からマス c 
2
​	
  に移動できることを指します。

空でない黒いマスの集合 S が連結成分であるとは、S が以下の条件を満たすことを指します。

S に属するどの 2 マスも連結である。
S に属さないすべての黒いマスが、S に属するどのマスとも連結でない。
N 個の大嵐がすべて発生した後のグリッドについて、連結成分の個数を求め、各連結成分におけるマスの個数を昇順に出力してください。

制約
N,X,Y は整数
1≤N≤14
1≤X,Y≤10 
8
 
C 
i
​	
  は X または Y
A 
i
​	
 ,B 
i
​	
  は整数
−10 
8
 ≤A 
i
​	
 ,B 
i
​	
 ≤10 
8
 
入力
入力は以下の形式で標準入力から与えられる。

N X Y
C 
1
​	
  A 
1
​	
  B 
1
​	
 
⋮
C 
N
​	
  A 
N
​	
  B 
N
​	
 
出力
2 行出力せよ。

1 行目には、黒いマスからなる連結成分の個数を出力せよ。

2 行目には、各連結成分におけるマスの個数を、空白区切りで昇順に出力せよ。

入力例 1
Copy
2 3 5
X 2 2
Y -1 1
出力例 1
Copy
2
2 13
大嵐によって、グリッドは以下の画像のように変化します(右方向が x 軸の正の向き、上方向が y 軸の正の向き)。



最終的なグリッドにおいて、以下の 2 つの連結成分が存在します。

マス (−1,−2),(0,−2) からなる連結成分。
マス (1,−1),(1,0),(1,1),(1,2),(2,−1),(2,0),(2,1),(2,2),(3,2),(3,3),(3,4),(3,5),(3,6) からなる連結成分。
各連結成分がもつマスの個数は昇順に出力する必要があることに注意してください。

入力例 2
Copy
14 68875272 94216928
X 1630731 32914676
X 17164413 -33684569
X 26798060 5418308
X 34094469 -45675954
X 43889566 34125482
X 56836569 -22217058
X 64045210 27857939
Y -54561094 11587606
Y 93548188 32214521
Y -77361096 25750481
Y 27724899 1810420
Y 80945185 -7871305
Y 14782822 -2565089
Y 54687684 -22884393
出力例 2
Copy
8
21105046168287 22050167303226 33624667752182 223328231190194 441936776830492 1141371400772596 1141702254882183 3464097998105256
出力する値は 32bit 整数に収まらないことがあります。
"""
import sys
sys.setrecursionlimit(10**7)

N, X, Y = map(int, sys.stdin.readline().split())
ops = []
for _ in range(N):
    c, a, b = sys.stdin.readline().split()
    ops.append((c, int(a), int(b)))

xs = set([0, X])
ys = set([0, Y])

for c, a, b in ops:
    if c == 'X':
        xs |= {a, a - b, a + b}
    else:
        ys |= {a, a - b, a + b}

xs = sorted(xs)
ys = sorted(ys)

def inside(x, y):
    return 0 <= x < X and 0 <= y < Y

cells = {}
idx = 0

for i in range(len(xs) - 1):
    for j in range(len(ys) - 1):
        mx = (xs[i] + xs[i+1]) // 2
        my = (ys[j] + ys[j+1]) // 2

        x, y = mx, my
        for c, a, b in reversed(ops):
            if c == 'X':
                if x < a:
                    y += b
                else:
                    y -= b
            else:
                if y < a:
                    x += b
                else:
                    x -= b

        if inside(x, y):
            cells[(i, j)] = idx
            idx += 1

parent = list(range(idx))
area = [0] * idx

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def unite(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a
        area[a] += area[b]

for (i, j), k in cells.items():
    area[k] = (xs[i+1] - xs[i]) * (ys[j+1] - ys[j])

for (i, j), k in cells.items():
    for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni, nj = i + di, j + dj
        if (ni, nj) in cells:
            unite(k, cells[(ni, nj)])

res = {}
for i in range(idx):
    r = find(i)
    res[r] = res.get(r, 0) + area[i]

ans = sorted(res.values())
print(len(ans))
print(*ans)
