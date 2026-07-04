"""
問題文
整数 N と o と x からなる長さ N の文字列 S が与えられます。

長さ N の整数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
N
​	
 ) があります。はじめ A=(1,2,…,N) です。

A に対して k=1,2,…,N の順に以下の操作を行います：

S 
k
​	
 = o である場合、A の先頭 k 項を反転する。具体的には、A を (A 
k
​	
 ,A 
k−1
​	
 ,…,A 
1
​	
 ,A 
k+1
​	
 ,A 
k+2
​	
 ,…,A 
N
​	
 ) に置き換える。
S 
k
​	
 = x である場合は何もしない。
全ての操作を終えた後の A を求めてください。

制約
2≤N≤5×10 
5
 
N は整数
S は o と x からなる長さ N の文字列
入力
入力は以下の形式で標準入力から与えられる。

N
S
出力
全ての操作を終えた後の A の各要素を空白区切りで出力せよ。

入力例 1
Copy
5
ooxoo
出力例 1
Copy
5 2 1 3 4
A は各操作で以下のように変化します：

k=1 のとき：A の先頭 1 項を反転する。A=(1,2,3,4,5) になる。
k=2 のとき：A の先頭 2 項を反転する。A=(2,1,3,4,5) になる。
k=3 のとき：何もしない。
k=4 のとき：A の先頭 4 項を反転する。A=(4,3,1,2,5) になる。
k=5 のとき：A の先頭 5 項を反転する。A=(5,2,1,3,4) になる。
全ての操作を終えた後の A は A=(5,2,1,3,4) です。

入力例 2
Copy
7
ooooooo
出力例 2
Copy
7 5 3 1 2 4 6
入力例 3
Copy
15
xooxoxoxoxoxxoo
出力例 3
Copy
15 11 10 7 6 3 1 2 4 5 8 9 12 13 14
"""

"""
kがあったとしたら、S「k」が⭕️でより小さい先頭にいれていくって感じ？
かと思ったら❌の時は、リストとかに持っておかないとダメ
"""
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]

    dq = deque()
    rev = False  # True なら「論理的な並び」は dq を反転したもの

    for k in range(1, n + 1):
        if not rev:
            dq.append(k)      # 論理的な右端に追加 = 実際の右端に追加
        else:
            dq.appendleft(k)  # 論理的な右端に追加 = 実際の左端に追加

        if s[k - 1] == 'o':
            rev = not rev      # 全体反転は「反転フラグ」を切り替えるだけでOK

    if rev:
        result = list(dq)[::-1]
    else:
        result = list(dq)

    sys.stdout.write(' '.join(map(str, result)) + '\n')

if __name__ == '__main__':
    main()