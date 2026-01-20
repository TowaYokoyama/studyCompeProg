"""
AtCorder.ABC.421.D の Docstring
無限に広いグリッドがあります。グリッドのあるマスはマス (0,0) と名前がついています。

マス (0,0) から下に r マス、右に c マスの移動した位置にあるマスをマス (r,c) と呼びます。
ここで、「下に r マス移動する」は r が負のときは「上に ∣r∣ マス移動する」ことを表し、「右に c マス移動する」は c が負のときには「左に ∣c∣ マス移動する」ことを表すものとします。

具体的には、マス (0,0) の周辺にあるマスは以下のようになります。

図

最初、高橋君はマス (R 
t
​	
 ,C 
t
​	
 ) に、青木君はマス (R 
a
​	
 ,C 
a
​	
 ) にいます。二人はそれぞれ U,D,L,R からなる長さ N の文字列 S,T に従って N 回移動を行います。
各 i について、高橋君と青木君の i 回目の移動は同時に行われます。具体的には、高橋君は S の i 文字目が U のとき上、D のとき下、L のとき左、R のとき右へ 1 マス移動し、青木君は T の i 文字目によって同様に移動します。

N 回の移動の中で、移動直後に高橋君と青木君が同じマスにいた回数を求めてください。

ただし、N は非常に大きいため S,T は ((S 
1
′
​	
 ,A 
1
​	
 ),…(S 
M
′
​	
 ,A 
M
​	
 )),((T 
1
′
​	
 ,B 
1
​	
 ),…,(T 
L
′
​	
 ,B 
L
​	
 )) の形で与えられ、 S は「文字 S 
1
′
​	
  を A 
1
​	
  個、…、文字 S 
M
′
​	
  を A 
M
​	
  個」をこの順に連結した文字列であり、T も同様です。

制約
−10 
9
 ≤R 
t
​	
 ,C 
t
​	
 ,R 
a
​	
 ,C 
a
​	
 ≤10 
9
 
1≤N≤10 
14
 
1≤M,L≤10 
5
 
S 
i
′
​	
 ,T 
i
′
​	
  は U, D, L, R のいずれか
1≤A 
i
​	
 ,B 
i
​	
 ≤10 
9
 
A 
1
​	
 +⋯+A 
M
​	
 =B 
1
​	
 +⋯+B 
L
​	
 =N
与えられる数値は全て整数
入力
入力は以下の形式で標準入力から与えられる。

R 
t
​	
  C 
t
​	
  R 
a
​	
  C 
a
​	
 
N M L
S 
1
′
​	
  A 
1
​	
 
⋮
S 
M
′
​	
  A 
M
​	
 
T 
1
′
​	
  B 
1
​	
 
⋮
T 
L
′
​	
  B 
L
​	
 
出力
答えを出力せよ。

入力例 1
Copy
0 0 4 2
3 2 1
R 2
D 1
U 3
出力例 1
Copy
1
このケースでは S= RRD、T= UUU であり、移動は次のように行われます。

最初、高橋君はマス (0,0) に、青木君はマス (4,2) にいる。
1 回目の移動後、高橋君はマス (0,1)、青木君はマス (3,2) にいる。
2 回目の移動後、高橋君はマス (0,2)、青木君はマス (2,2) にいる。
3 回目の移動後、高橋君はマス (1,2)、青木君はマス (1,2) にいる。
よって、高橋君と青木君が移動直後に同じマスにいた回数は 1 です。

入力例 2
Copy
1000000000 1000000000 -1000000000 -1000000000
3000000000 3 3
L 1000000000
U 1000000000
U 1000000000
D 1000000000
R 1000000000
U 1000000000
出力例 2
Copy
1000000001
2000000000 回目の移動から 3000000000 回目の移動までの 1000000001 回で高橋君と青木君は移動直後に同じマスにいます。

入力例 3
Copy
3 3 3 2
1 1 1
L 1
R 1
出力例 3
Copy
0
入力例 4
Copy
0 0 0 0
1 1 1
L 1
R 1
出力例 4
Copy
0

"""
r_t,c_t,r_a,c_a = map(int,input().split())
# 方向を座標変化量に変換する辞書
d = {'U':(-1, 0),'D':(1, 0),'L':(0, -1),'R':(0, 1)}
n,m,l = map(int,input().split())
s_a_m = [] # 高橋君の移動指示
for _ in range(m):
    s, a = input().split()
    s_a_m.append((s, int(a)))
t_b_l = [] # 青木君の移動指示
for _ in range(l):
    t, b = input().split()
    t_b_l.append((t, int(b)))

# 現在処理中の移動指示のインデックス
t_cnt,a_cnt = 0,0
# 現在の移動指示で残りの移動回数
zan_t,zan_a = s_a_m[0][1],t_b_l[0][1]
# 現在の移動方向
dir_t,dir_a = d[s_a_m[0][0]],d[t_b_l[0][0]]
# 現在の座標
r_t_now, c_t_now, r_a_now, c_a_now = r_t, c_t, r_a, c_a 
ans = 0

# どちらかの移動指示がなくなるまでループ
while t_cnt < m and a_cnt < l:
    # 共通して進める移動回数
    k = min(zan_t, zan_a) 
    
    # 青木君から高橋君への相対座標 (青木君 - 高橋君)
    diff_r_now, diff_c_now = r_a_now - r_t_now, c_a_now - c_t_now
    # 青木君から高橋君への相対移動方向 (青木君の方向 - 高橋君の方向)
    # 1回の移動で相対座標がどれだけ変化するか
    diff_dir_r, diff_dir_c = dir_a[0] - dir_t[0], dir_a[1] - dir_t[1]

    # ケース1: 相対移動方向がゼロ (両者が同じ方向へ同じ速さで進む)
    if diff_dir_r == 0 and diff_dir_c == 0:
        # 初期座標が一致していれば、ブロック全体で衝突し続ける
        if diff_r_now == 0 and diff_c_now == 0:
            ans += k
    # ケース2: 縦方向のみに相対移動がある (横方向の相対移動はなし)
    elif diff_dir_r == 0:
        # 縦方向の座標差がゼロで、横方向の相対移動で衝突する場合
        if diff_r_now == 0 and (-diff_c_now) % diff_dir_c == 0:
            # 衝突するまでの移動回数を計算
            # -diff_c_now は t回目の移動で青木君が目標とする相対C座標
            # diff_dir_c は 1回の移動での相対C座標の変化量
            # 例: diff_c_now=4, diff_dir_c=2 なら 4/2 = 2回後に衝突
            collision_time = (-diff_c_now) // diff_dir_c
            # 衝突がブロック内で発生し、かつ1回以上の移動後である場合
            if 1 <= collision_time <= k:
                ans += 1
    # ケース3: 横方向のみに相対移動がある (縦方向の相対移動はなし)
    elif diff_dir_c == 0:
        # 横方向の座標差がゼロで、縦方向の相対移動で衝突する場合
        if diff_c_now == 0 and (-diff_r_now) % diff_dir_r == 0:
            collision_time = (-diff_r_now) // diff_dir_r
            if 1 <= collision_time <= k:
                ans += 1
    # ケース4: 両方の軸方向に相対移動がある
    # 衝突するためには、縦と横の衝突までの移動回数が一致する必要がある
    # また、それぞれの軸で割り切れる必要がある
    elif (-diff_r_now) % diff_dir_r == 0 and (-diff_c_now) % diff_dir_c == 0:
        collision_time_r = (-diff_r_now) // diff_dir_r
        collision_time_c = (-diff_c_now) // diff_dir_c
        # 縦と横の衝突時間が一致し、かつブロック内で衝突する場合
        if collision_time_r == collision_time_c and 1 <= collision_time_c <= k:
            ans += 1


    # k回移動後の座標を更新
    r_t_now += dir_t[0] * k
    c_t_now += dir_t[1] * k
    r_a_now += dir_a[0] * k
    c_a_now += dir_a[1] * k

    # 残りの移動回数を更新
    zan_t -= k
    zan_a -= k
    
    # 高橋君の移動指示が完了した場合、次の指示に進む
    if zan_t == 0:
        t_cnt += 1
        if t_cnt < m:
            dir_t = d[s_a_m[t_cnt][0]]
            zan_t = s_a_m[t_cnt][1]
    # 青木君の移動指示が完了した場合、次の指示に進む
    if zan_a == 0:
        a_cnt += 1
        if a_cnt < l:
            dir_a = d[t_b_l[a_cnt][0]]
            zan_a = t_b_l[a_cnt][1]

print(ans)

