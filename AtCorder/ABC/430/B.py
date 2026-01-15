"""
AtCorder.ABC.430.B の Docstring
N 行 N 列からなるグリッドがあります。グリッドの上から i 行目左から j 列目のマスは、S 
i,j
​	
  が # のとき黒く、. のとき白く塗られています。

このグリッドから縦 M 行横 M 列の領域を取り出して得られるマスの塗られ方は何種類ありますか？

制約
1≤M≤N≤10
N,M は整数
S 
i,j
​	
  は . または #
入力
入力は以下の形式で標準入力から与えられる。

N M
S 
1,1
​	
 …S 
1,N
​	
 
⋮
S 
N,1
​	
 …S 
N,N
​	
 
出力
答えを出力せよ。

入力例 1
Copy
3 2
...
###
#.#
出力例 1
Copy
3
与えられたグリッドの状態は下図左のとおりです。
ここから縦 2 行横 2 列の領域を取り出す方法は下図右のとおり 4 通りあり、マスの塗られ方は 3 種類あります。

図

入力例 2
Copy
10 3
..#.......
.###......
.#.#......
#####.....
#...#.....
......####
......#..#
......#...
......#..#
......####
出力例 2
Copy
36

"""
N,M = map(int,input().split())
S = [list(input()) for _ in range(N)]

patterns = set()

for i in range(N-M+1):
    for j in range(N-M+1):
        block = tuple(
            tuple(S[i+x][j+y] for y in range(M)) 
                  for x in range(M))
        patterns.add(block)
print(len(patterns))