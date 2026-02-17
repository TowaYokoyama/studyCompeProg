"""
1 以上 N 以下の整数からなる集合が M 個あり、順に S 
1
​	
 ,S 
2
​	
 ,…,S 
M
​	
  と呼びます。
S 
i
​	
  は C 
i
​	
  個の整数 a 
i,1
​	
 ,a 
i,2
​	
 ,…,a 
i,C 
i
​	
 
​	
  からなります。

M 個の集合から 1 個以上の集合を選ぶ方法は 2 
M
 −1 通りあります。
このうち、次の条件を満たす選び方は何通りありますか？

1≤x≤N を満たす全ての整数 x に対して、選んだ集合の中に x を含む集合が少なくとも 1 個存在する。
制約
1≤N≤10
1≤M≤10
1≤C 
i
​	
 ≤N
1≤a 
i,1
​	
 <a 
i,2
​	
 <⋯<a 
i,C 
i
​	
 
​	
 ≤N
入力される値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
C 
1
​	
 
a 
1,1
​	
  a 
1,2
​	
  … a 
1,C 
1
​	
 
​	
 
C 
2
​	
 
a 
2,1
​	
  a 
2,2
​	
  … a 
2,C 
2
​	
 
​	
 
⋮
C 
M
​	
 
a 
M,1
​	
  a 
M,2
​	
  … a 
M,C 
M
​	
 
​	
 
出力
問題文の条件を満たす集合の選び方の数を出力せよ。

入力例 1
Copy
3 3
2
1 2
2
1 3
1
2
出力例 1
Copy
3
入力で与えられている集合はそれぞれ S 
1
​	
 ={1,2},S 
2
​	
 ={1,3},S 
3
​	
 ={2} です。
問題文の条件を満たす集合の選び方は次の 3 通りです。

S 
1
​	
 ,S 
2
​	
  を選ぶ。
S 
1
​	
 ,S 
2
​	
 ,S 
3
​	
  を選ぶ。
S 
2
​	
 ,S 
3
​	
  を選ぶ。
入力例 2
Copy
4 2
2
1 2
2
1 3
出力例 2
Copy
0
問題文の条件を満たす選び方が存在しない場合もあります。

入力例 3
Copy
6 6
3
2 3 6
3
2 4 6
2
3 6
3
1 5 6
3
1 3 6
2
1 4
出力例 3
Copy
18

"""
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    masks = []
    for _ in range(M):
        C = int(input().strip())
        arr = list(map(int, input().split()))
        mask = 0
        for a in arr:
            mask |= 1 << (a - 1)  # aは1..Nなので0-indexへ
        masks.append(mask)

    full = (1 << N) - 1
    ans = 0

    # 1個以上選ぶので 1 からスタート（0は空選択）
    for sel in range(1, 1 << M):
        cover = 0
        for i in range(M):
            if sel & (1 << i):
                cover |= masks[i]
        if cover == full:
            ans += 1

    print(ans)

if __name__ == "__main__":
    solve()
