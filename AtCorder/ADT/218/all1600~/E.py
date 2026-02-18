"""
AtCorder.ADT.218.all1600~.E の Docstring
1,2,…,N がちょうど 3 回ずつ現れる長さ 3N の数列 A=(A 
1
​	
 ,A 
2
​	
 ,…,A 
3N
​	
 ) が与えられます。

i=1,2,…,N について、A の中にある i のうち真ん中にあるものの添字を f(i) と定めます。 1,2,…,N を f(i) の昇順に並べ替えてください。

f(i) の定義は厳密には以下の通りです。

A 
j
​	
 =i を満たす j が j=α,β,γ (α<β<γ) であるとする。このとき、f(i)=β である。
制約
1≤N≤10 
5
 
1≤A 
j
​	
 ≤N
i=1,2,…,N それぞれについて、A の中に i はちょうど 3 回現れる
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
A 
1
​	
  A 
2
​	
  … A 
3N
​	
 
出力
1,2,…,N を f(i) の昇順に並べ替えてできる長さ N の数列を空白区切りで出力せよ。

入力例 1
Copy
3
1 1 3 2 3 2 2 3 1
出力例 1
Copy
1 3 2
A の中にある 1 は A 
1
​	
 ,A 
2
​	
 ,A 
9
​	
  なので、f(1)=2 です。
A の中にある 2 は A 
4
​	
 ,A 
6
​	
 ,A 
7
​	
  なので、f(2)=6 です。
A の中にある 3 は A 
3
​	
 ,A 
5
​	
 ,A 
8
​	
  なので、f(3)=5 です。
よって、f(1)<f(3)<f(2) であるため 1,3,2 の順に出力します。

入力例 2
Copy
1
1 1 1
出力例 2
Copy
1
入力例 3
Copy
4
2 3 4 3 4 1 3 1 1 4 2 2
出力例 3
Copy
3 4 1 2

"""
import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    A = list(map(int, input().split()))

    cnt = [0] * (N + 1)   # cnt[i] = i を何回見たか
    f = [0] * (N + 1)     # f[i] = 2回目に出た位置(1-indexed)

    for idx, x in enumerate(A, start=1):  # idx は 1..3N
        cnt[x] += 1
        if cnt[x] == 2:
            f[x] = idx

    pairs = [(f[i], i) for i in range(1, N + 1)]
    pairs.sort()  # f(i) 昇順

    ans = [str(i) for _, i in pairs]
    print(" ".join(ans))

if __name__ == "__main__":
    main()
