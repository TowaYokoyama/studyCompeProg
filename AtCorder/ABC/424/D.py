"""
AtCorder.ABC.424.D の Docstring
 行 W 列のマス目があり、各マスは白または黒に塗られています。
マス目の上から i 番目 (1≤i≤H) かつ左から j 番目 (1≤j≤W) のマスをマス (i,j) と表すことにします。
マス目の状態は H 個の、. と # のみからなる長さ W の文字列 S 
1
​	
 ,S 
2
​	
 ,…,S 
H
​	
  によって与えられ、
S 
i
​	
  の j 文字目が . のとき、マス (i,j) が白く塗られていることを、# のときマス (i,j) が黒く塗られていることを表します。

高橋君はいくつか（0 個でも良い）の黒く塗られたマスを白に塗り替えることで、 マス目が黒く塗られたマスのみからなる 2×2 の部分を持たないようにしたいです。 より厳密には、次の条件をみたすようにしたいです。

1≤i≤H−1, 1≤j≤W−1 をみたす任意の整数の組 (i,j) について、 マス (i,j), マス (i,j+1), マス (i+1,j), マス (i+1,j+1) のうち 少なくとも 1 つは白く塗られている 。
高橋君が目標を達成するために、白く塗り替える必要のあるマスの個数の最小値を求めてください。

T 個のテストケースが与えられるので、それぞれについて答えを求めてください。

制約
1≤T≤100
2≤H≤7
2≤W≤7
S 
i
​	
  は . と # のみからなる長さ W の文字列
T,H,W は整数
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
 
case 
i
​	
  は i 番目のテストケースを表す。 各テストケースは以下の形式で与えられる。

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
T 行出力せよ。
i 行目 (1≤i≤T) には、i 個目のテストケースの答えを出力せよ。

入力例 1
Copy
2
5 5
####.
##.##
#####
.####
##.#.
2 2
..
..
出力例 1
Copy
3
0
1 つめのテストケースについて、マス目の最初の状態は、下図左のようになっています。
このマス目の黒いマスのうち、例えば下図右の番号が入っている 3 つのマスを白く塗り替えることで、条件をみたすようにできます。



最初の状態から 2 個以下のマスを白く塗ることで条件をみたすようにすることはできないため、3 を 1 行目に出力します。

2 つめのテストケースについて、マス目は最初から条件をみたしています。
よって、0 を 2 行目に出力します。
"""
import sys

# すべての入力を一括で読み込み
input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

it = iter(input_data)
T_cases = int(next(it))

for _ in range(T_cases):
    H = int(next(it))
    W = int(next(it))
    S = [next(it) for _ in range(H)]
    
    # 元の状態をビットマスクに変換 (#=1, .=0)
    row_masks = []
    for i in range(H):
        m = 0
        for j in range(W):
            if S[i][j] == '#':
                m |= (1 << j)
        row_masks.append(m)
    
    # 2x2判定用：横に黒マスが2つ並んでいる位置をビットで特定するリスト
    # (m & (m >> 1)) のビット j が 1 なら、j番目とj+1番目が両方黒
    pair_bits = [m & (m >> 1) for m in range(1 << W)]
    
    # 各行で「選択可能な状態」と「塗り替えコスト」を前計算
    possible_masks_per_row = []
    for i in range(H):
        orig = row_masks[i]
        masks = []
        for m in range(1 << W):
            # 白を黒に変更はできないので、m は orig のサブセットである必要がある
            if (m & ~orig) == 0:
                # 塗り替えた数 = 元の黒(orig) XOR 今の黒(m) の 1 の数
                cost = bin(orig ^ m).count('1')
                masks.append((m, cost, pair_bits[m]))
        possible_masks_per_row.append(masks)
    
    # DP初期化
    inf = 10**9
    dp = [inf] * (1 << W)
    
    # 1行目の初期コストをセット
    for m, cost, p_bit in possible_masks_per_row[0]:
        dp[m] = cost
        
    # 2行目以降の動的計画法
    for i in range(1, H):
        new_dp = [inf] * (1 << W)
        curr_options = possible_masks_per_row[i]
        prev_options = possible_masks_per_row[i-1]
        
        for m_curr, cost_curr, p_curr in curr_options:
            # 前の行の全状態と比較して最小コストを探す
            res = inf
            for m_prev, _, p_prev in prev_options:
                # 前後の行で同じ位置に「横並び黒ペア」があると2x2ができる
                if (p_prev & p_curr) == 0:
                    if dp[m_prev] < res:
                        res = dp[m_prev]
            
            if res != inf:
                new_dp[m_curr] = res + cost_curr
        dp = new_dp
    
    # そのテストケースの最小値を出力
    print(min(dp))