"""
AtCorder.ABC.265.C の Docstring
問題文
縦 H マス、横 W マスのグリッドがあります。上から i 行目、左から j 列目のマスを (i,j) と表します。
(i,j) には文字 G 
i,j
​	
  が書きこまれています。ここで G 
i,j
​	
  は U, D, L, R のいずれかです。

あなたは (1,1) にいます。あなたは移動することができなくなるまで次の操作を繰り返します。

あなたは現在 (i,j) にいるとする。
G 
i,j
​	
  が U であり、かつ i

=1 ならば (i−1,j) へ移動する。
G 
i,j
​	
  が D であり、かつ i

=H ならば (i+1,j) へ移動する。
G 
i,j
​	
  が L であり、かつ j

=1 ならば (i,j−1) へ移動する。
G 
i,j
​	
  が R であり、かつ j

=W ならば (i,j+1) へ移動する。
それ以外の場合、あなたは移動することができない。
操作を終了した時点であなたがいるマスを出力してください。
ただし、あなたが操作を終了することなく無限に移動し続ける場合は -1 を出力してください。

制約
1≤H,W≤500
G 
i,j
​	
  は U, D, L, R のいずれかである。
H,W は整数である。
入力
入力は以下の形式で標準入力から与えられる。

H W
G 
1,1
​	
 G 
1,2
​	
 …G 
1,W
​	
 
G 
2,1
​	
 G 
2,2
​	
 …G 
2,W
​	
 
⋮
G 
H,1
​	
 G 
H,2
​	
 …G 
H,W
​	
 
出力
操作を終了した時点であなたが (i,j) にいる場合は次の形式で出力せよ。

i j
また、無限に動き続ける場合は -1 を出力せよ。

入力例 1
Copy
2 3
RDU
LRU
出力例 1
Copy
1 3
あなたは (1,1)→(1,2)→(2,2)→(2,3)→(1,3) の順に動いたあとに操作を終了します。よって答えは (1,3) です。

入力例 2
Copy
2 3
RRD
ULL
出力例 2
Copy
-1
あなたは (1,1)→(1,2)→(1,3)→(2,3)→(2,2)→(2,1)→(1,1)→(1,2)→… というように無限に動き続けます。この場合は -1 を出力します。

入力例 3
Copy
9 44
RRDDDDRRRDDDRRRRRRDDDRDDDDRDDRDDDDDDRRDRRRRR
RRRDLRDRDLLLLRDRRLLLDDRDLLLRDDDLLLDRRLLLLLDD
DRDLRLDRDLRDRLDRLRDDLDDLRDRLDRLDDRLRRLRRRDRR
DDLRRDLDDLDDRLDDLDRDDRDDDDRLRRLRDDRRRLDRDRDD
RDLRRDLRDLLLLRRDLRDRRDRRRDLRDDLLLLDDDLLLLRDR
RDLLLLLRDLRDRLDDLDDRDRRDRLDRRRLDDDLDDDRDDLDR
RDLRRDLDDLRDRLRDLDDDLDDRLDRDRDLDRDLDDLRRDLRR
RDLDRRLDRLLLLDRDRLLLRDDLLLLLRDRLLLRRRRLLLDDR
RRRRDRDDRRRDDRDDDRRRDRDRDRDRRRRRRDDDRDDDDRRR
出力例 3
Copy
9 5

"""
H,W = map(int,input().split())
g = [list(input())for _ in range(H)]

dirs = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

x, y = 0, 0   # 今いる場所（0-index）
visited = [[False]*W for _ in range(H)]


while True:
    if visited[x][y] == True:
        print(-1)
        exit()
    visited[x][y] = True
    
    di,dj = dirs[g[x][y]]
    nx,ny = di+x,dj+y
    
    if not (0 <= nx < H and 0 <= ny < W):
        print(x+1, y+1)
        break
    
    x,y = nx,ny

         