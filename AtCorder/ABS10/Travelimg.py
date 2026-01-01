"""
AtCorder.ABS10.Travelimg の Docstring
問題文
シカのAtCoDeerくんは二次元平面上で旅行をしようとしています。 AtCoDeerくんの旅行プランでは、時刻 0 に 点 (0,0) を出発し、 1 以上 N 以下の各 i に対し、時刻 t 
i
​	
  に 点 (x 
i
​	
 ,y 
i
​	
 ) を訪れる予定です。

AtCoDeerくんが時刻 t に 点 (x,y) にいる時、 時刻 t+1 には 点 (x+1,y), (x−1,y), (x,y+1), (x,y−1) のうちいずれかに存在することができます。 その場にとどまることは出来ないことに注意してください。 AtCoDeerくんの旅行プランが実行可能かどうか判定してください。

制約
1 ≤ N ≤ 10 
5
 
0 ≤ x 
i
​	
  ≤ 10 
5
 
0 ≤ y 
i
​	
  ≤ 10 
5
 
1 ≤ t 
i
​	
  ≤ 10 
5
 
t 
i
​	
  < t 
i+1
​	
  (1 ≤ i ≤ N−1)
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N
t 
1
​	
  x 
1
​	
  y 
1
​	
 
t 
2
​	
  x 
2
​	
  y 
2
​	
 
:
t 
N
​	
  x 
N
​	
  y 
N
​	
 
出力
旅行プランが実行可能ならYesを、不可能ならNoを出力してください。

入力例 1
Copy
2
3 1 2
6 1 1
出力例 1
Copy
Yes
例えば、(0,0), (0,1), (1,1), (1,2), (1,1), (1,0), (1,1) と移動すればよいです。

入力例 2
Copy
1
2 100 100
出力例 2
Copy
No
(0,0) にいる状態から 2 秒後に (100,100) にいるのは不可能です。

入力例 3
Copy
2
5 1 1
100 1 1
出力例 3
Copy
No

"""
# 入力を受け取る
N = int(input())
txys = [tuple(map(int, input().split())) for _ in range(N)]

# 初期位置・時刻
current_t, current_x, current_y = 0, 0, 0

# 各予定についてチェック
for t, x, y in txys:
    dt = t - current_t
    dist = abs(x - current_x) + abs(y - current_y)

    # 移動不可能なら即終了
    if dist > dt or (dt - dist) % 2 != 0:
        print("No")
        exit()

    # 次の基準点を更新
    current_t, current_x, current_y = t, x, y

# 全て通過できたら
print("Yes")
