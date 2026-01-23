"""
AtCorder.ABC.272.B の Docstring
1,2,…,N の番号がついた N 人の人がいます。

M 回の舞踏会が行われました。 i (1≤i≤M) 回目の舞踏会には k 
i
​	
  人が参加し、参加した人は人 x 
i,1
​	
 ,x 
i,2
​	
 ,…,x 
i,k 
i
​	
 
​	
  でした。

どの二人も少なくとも 1 回同じ舞踏会に参加したか判定してください。

制約
2≤N≤100
1≤M≤100
2≤k 
i
​	
 ≤N
1≤x 
i,1
​	
 <x 
i,2
​	
 <…<x 
i,k 
i
​	
 
​	
 ≤N
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N M
k 
1
​	
  x 
1,1
​	
  x 
1,2
​	
  … x 
1,k 
1
​	
 
​	
 
⋮
k 
M
​	
  x 
M,1
​	
  x 
M,2
​	
  … x 
M,k 
M
​	
 
​	
 
出力
どの二人も少なくとも 1 回同じ舞踏会に参加した場合 Yes を、そうでない場合 No を出力せよ。

入力例 1
Copy
3 3
2 1 2
2 2 3
2 1 3
出力例 1
Copy
Yes
人 1 と人 2 は共に 1 回目の舞踏会に参加しています。

人 2 と人 3 は共に 2 回目の舞踏会に参加しています。

人 1 と人 3 は共に 3 回目の舞踏会に参加しています。

以上よりどの二人も少なくとも 1 回同じ舞踏会に参加したので、答えは Yes です。

入力例 2
Copy
4 2
3 1 2 4
3 2 3 4
出力例 2
Copy
No
人 1 と人 3 は 1 回も同じ舞踏会に参加していないので、答えは No です。


"""
N, M = map(int, input().split())

events = []
for _ in range(M):
    row = list(map(int, input().split()))
    events.append(set(row[1:]))

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        ok = False
        for e in events:
            if i in e and j in e:
                ok = True
                break
        if not ok:
            print("No")
            exit()

print("Yes")
