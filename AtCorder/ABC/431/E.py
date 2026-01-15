""""
問題文
H 行 W 列のマス目があります。 上から i 行目、左から j 列目のマスをマス (i,j) と呼ぶことにします。各マスには鏡が高々 1 枚置いてあります。

高橋君はマス (1,1) の左側、青木くんはマス (H,W) の右側に立っています。高橋君は懐中電灯を持っており、マス (1,1) の左側から右に向かって光を入れています。ここで、懐中電灯の光は拡散せず、まっすぐに進む光線であるとします。

高橋君の目標は、マス目にある鏡を利用して懐中電灯の光を青木君に届けることです。

鏡の置き方は次の 3 種類あります。光が鏡に当たると、鏡の置き方に応じて光の進む向きが変わります。それぞれの鏡の置き方について、光が入る方向に対する出る方向は下図のようになります。

タイプ A （鏡は置かれていない）


タイプ B （左上と右下を結ぶ対角線上に鏡が置かれている）


タイプ C （右上と左下を結ぶ対角線上に鏡が置かれている）


マス目の鏡の置き方は H 個の長さ W の文字列 S 
1
​	
 ,S 
2
​	
 ,…,S 
H
​	
  で表されます。S 
i
​	
  の j 文字目が A のときマス (i,j) はタイプ A、B のときマス (i,j) はタイプ B、C のときマス (i,j) はタイプ C です。

高橋君は、青木君に光を届けるために以下の操作を好きな回数行うことができます。

あるマスを 1 つ選び、そのマスの鏡の置き方を別のタイプに変更する
青木君に光を届けるためには最低何回操作を行う必要があるか求めてください。

T 個のテストケースが与えられるので、それぞれについて答えを求めてください。

制約
1≤T
1≤H,W
HW≤2×10 
5
 
S 
i
​	
  は A, B, C からなる長さ W の文字列
T,H,W は整数
全てのテストケースに対する HW の総和は 2×10 
5
  以下
入力
入力は以下の形式で標準入力から与えられる。

T
case 
1
​	
 
case 
2
​	
 
⋮
case 
T
​	
 
各テストケースは以下の形式で与えられる。

H W
S 
1
​	
 
S 
2
​	
 
⋮
S 
H
​	
 
出力
T 行出力せよ。i 行目には i 番目のテストケースに対する答えを出力せよ。

入力例 1
Copy
4
3 4
ABCB
CACC
BCBA
2 2
CB
AA
1 10
BCBCBCBCBC
10 10
CCAABACAAA
CCCBACACCA
BACAABCBBA
ACCCAACCCA
CCAAAACCBA
AACBBACCAA
BCCCACBBAB
CBBCAACCCC
CBBCCBCBCA
BBACABBACC
出力例 1
Copy
0
2
10
5
1 つ目のテストケースについて、操作を行わなくても青木君に光を届けることができます。



2 つ目のテストケースについて、マス (1,1) の鏡の置き方をタイプ A に、マス (2,2) の鏡の置き方をタイプ B に変更することで、下図のように青木君に光を届けることができます。1 回以下の操作で青木君に光を届けることはできないので、答えは 2 です。
"""
import sys
from collections import deque

def solve_case(H, W, S):
    # dir: 0=UP, 1=RIGHT, 2=DOWN, 3=LEFT
    # Type A: straight
    # Type B: "\" mirror (top-left to bottom-right)
    # Type C: "/" mirror (top-right to bottom-left)

    # mapping[type][dir_in] = dir_out
    A_map = [0, 1, 2, 3]
    B_map = [3, 2, 1, 0]  # UP->LEFT, RIGHT->DOWN, DOWN->RIGHT, LEFT->UP
    C_map = [1, 0, 3, 2]  # UP->RIGHT, RIGHT->UP, DOWN->LEFT, LEFT->DOWN
    maps = {
        'A': A_map,
        'B': B_map,
        'C': C_map,
    }
    types = ['A', 'B', 'C']

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n_cells = H * W
    INF = 10**18
    dist = [INF] * (n_cells * 4)

    def idx(i, j, d):
        return ((i * W + j) * 4 + d)

    start = idx(0, 0, 1)  # enter (1,1) from left, moving RIGHT
    dist[start] = 0
    dq = deque([start])

    ans = INF

    while dq:
        v = dq.popleft()
        cur = dist[v]
        if cur >= ans:
            continue

        cell = v // 4
        d_in = v % 4
        i = cell // W
        j = cell % W

        original = S[i][j]

        for t in types:
            add = 0 if t == original else 1
            d_out = maps[t][d_in]
            ni = i + dx[d_out]
            nj = j + dy[d_out]
            ncost = cur + add

            # leaving the grid
            if not (0 <= ni < H and 0 <= nj < W):
                # success iff we exit to the right of (H-1, W-1)
                if i == H - 1 and j == W - 1 and d_out == 1:
                    if ncost < ans:
                        ans = ncost
                continue

            u = idx(ni, nj, d_out)
            if ncost < dist[u]:
                dist[u] = ncost
                if add == 0:
                    dq.appendleft(u)
                else:
                    dq.append(u)

    return ans

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    out = []
    for _ in range(T):
        H, W = map(int, input().split())
        S = [input().strip() for _ in range(H)]
        out.append(str(solve_case(H, W, S)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
