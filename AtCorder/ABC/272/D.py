# 入力の受け取り
N,M=map(int,input().split())

# 方向の記録
d=[]

# a=-10^3(より少し小さめ)~10^3(より少し大きめ)
for a in range(-10**3-10,10**3+10):
    # b=-10^3(より少し小さめ)~10^3(より少し大きめ)
    for b in range(-10**3-10,10**3+10):
        # a^2+b^2=Mならば
        if a**2+b**2==M:
            # (a,b)方向へ進める
            d.append([a,b])

# マス目(初期値は「-1」)
Grid=[[-1]*(N+1) for i in range(N+1)]

# (1)スタート地点(1,1)に「0」を書き込む
Grid[1][1]=0

# dequeのインポート
from collections import deque
# キューを用意
que=deque()
# (2)キューにスタート地点(1,1)を追加
que.append([1,1])

# (5)キューが空でなければ(3)へ戻る
while 0<len(que):
    # (3)キューから座標を取り出し(今いる行、今いる列)、書かれている数字を確認
    # キューから座標を取り出し
    NowG,NowR=que.popleft()
    # 今いるマスの数字
    Num=Grid[NowG][NowR]

    # (4)今いるマスから進めるマスについてまだ数字が書き込まれていなければ「今いるマスの数字+1」を書き込み、キューへ追加する
    # dから行方向、列方向の増加量を取り出し
    # Gd,Rd：dの各要素を順に格納
    for Gd,Rd in d:
        # 1≤NowG+Gd≤N(今いるマスから行方向にGd進んだマスがマス目の範囲内)
        # かつ
        # 1≤NowR+Rd≤N(今いるマスから列方向にRd進んだマスがマス目の範囲内)
        if 1<=NowG+Gd<=N and 1<=NowR+Rd<=N:
            # まだ数字が書き込まれていなければ(-1ならば)
            if Grid[NowG+Gd][NowR+Rd]==-1:
                # 「今いるマスの数字+1」を書き込む
                Grid[NowG+Gd][NowR+Rd]=Num+1
                # キューに追加
                que.append([NowG+Gd,NowR+Rd])

# G=1~N
for G in range(1,N+1):
    # G行目の1列目以降を出力(「*」をつけるとカッコなしで出力できる)
    print(*Grid[G][1:])
