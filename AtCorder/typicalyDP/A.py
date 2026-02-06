"""
AtCorder.typicalyDP.A の Docstring
Problem Statement
N 問の問題があるコンテストがあり、i 問目の問題の配点は p 
i
​	
  点である。コンテスタントは、この問題の中から何問か解き、解いた問題の配点の合計が得点となる。このコンテストの得点は何通り考えられるか。
Constraints
1≤N≤100
1≤p 
i
​	
 ≤100
Input Format
入力は以下の形式で標準入力から与えられる。
N
p 
1
​	
 p 
2
​	
 ...p 
N
​	
 
Output Format
答えを一行に出力せよ。
Sample Input 1
3
2 3 5
Sample Output 1
7
0, 2, 3, 5, 7, 8, 10 の 7 通りの得点が考えられる。
Sample Input 2
10
1 1 1 1 1 1 1 1 1 1
Sample Output 2
11
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 の 11 通りの得点が考えられる。

"""
N = int(input())
p = list(map(int,input().split()))

max_sum = sum(p)
dp = [False] * (max_sum +1)
dp[0] = True 

for score in p:
    for s in range(max_sum, -1,-1):
        if dp[s]:
            dp[s+score] = True 

print(sum(dp))