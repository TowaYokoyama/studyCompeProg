# pypyで提出

# 入力の受け取り
H,W,rs,cs=map(int,input().split())
N=int(input())

# defaultdictのインポート
from collections import defaultdict

# 各行ごとの壁マスの列を記録
# 初期値は空のリスト
KabeDR=defaultdict(list)
# 各列ごとの壁マスの行を記録
KabeDC=defaultdict(list)

# [行,列]の順に記録するリスト
RC=[]
# [列,行]の順に記録するリスト
CR=[]

# N回
for i in range(N):
    # 入力の受け取り
    r,c=map(int,input().split())
    # 記録
    RC.append([r,c])
    CR.append([c,r])

# 行の小さい順にソート
RC.sort()
# 列の小さい順にソート
CR.sort()

# r,c：RCの各要素を順に格納
for r,c in RC:
    # 列cのr行目に壁がある
    # ソートしているから行番号の小さい順に記録ができる
    KabeDC[c].append(r)

# 行も同様
for c,r in CR:
    KabeDR[r].append(c)

# 右方向への二分探索
# 今いるマスから右方向で最も近い壁マスの列番号を返す
def NibutanR(NowR,NowC):
    # 長さが0⇔今いる行に壁マスがない場合
    if len(KabeDR[NowR])==0:
        # 一番近い壁の列番号は(W+1)
        return W+1
    # 長さが1以上　かつ　最も大きい(右側にある)壁マスの列番号<今いるマスの列番号
    elif KabeDR[NowR][-1]<NowC:
        # 一番近い壁の列番号は(W+1)
        return W+1
    # 長さが1以上　かつ　今いるマスの列番号<最も小さい(左側にある)壁マスの列番号
    elif NowC<KabeDR[NowR][0]:
        # 一番近い壁の列番号はKabeDR[NowR][0](最も小さい壁マスの列番号)
        return KabeDR[NowR][0]
    
    # 探索範囲の決定
    # 左
    l=0
    # 右
    r=len(KabeDR[NowR])-1

    # 1<(右-左)である間
    while 1<r-l:
        # 中央
        c=(l+r)//2

        # 中央の壁マスの列番号<今いるマスの列番号
        if KabeDR[NowR][c]<NowC:
            # 左=中央と更新
            l=c
        # そうでない場合(今いるマスの列番号<中央の壁マスの列番号)
        else:
            # 右=中央と更新
            r=c
    
    # 今いるマスから右方向で最も近い壁マスの列番号を返す
    return KabeDR[NowR][r]

# 左方向への二分探索
# 今いるマスから左方向で最も近い壁マスの列番号を返す
def NibutanL(NowR,NowC):
    if len(KabeDR[NowR])==0:
        # 一番近い壁の列番号は0
        return 0
    # 長さが1以上　かつ　今いるマスの列番号<最も小さい(左側にある)壁マスの列番号
    elif NowC<KabeDR[NowR][0]:
        # 一番近い壁の列番号は0
        return 0
    # 長さが1以上　かつ　最も大きい(右側にある)壁マスの列番号<今いるマスの列番号
    elif KabeDR[NowR][-1]<NowC:
        # 一番近い壁の列番号はKabeDR[NowR][-1](最も大きい壁マスの列番号)
        return KabeDR[NowR][-1]
    
    # 探索範囲の決定
    # 左
    l=0
    # 右
    r=len(KabeDR[NowR])-1

    # 1<(右-左)である間
    while 1<r-l:
        # 中央
        c=(l+r)//2

        # 中央の壁マスの列番号<今いるマスの列番号
        if KabeDR[NowR][c]<NowC:
            # 左=中央と更新
            l=c
        # そうでない場合(今いるマスの列番号<中央の壁マスの列番号)
        else:
            # 右=中央と更新
            r=c
    
    # 今いるマスから左方向で最も近い壁マスの列番号を返す
    return KabeDR[NowR][l]

# 下方向への二分探索
# 今いるマスから右方向で最も近い壁マスの行番号を返す
def NibutanD(NowR,NowC):
    # 長さが0⇔今いる行に壁マスがない場合
    if len(KabeDC[NowC])==0:
        # 一番近い壁の行番号は(H+1)
        return H+1
    # 長さが1以上　かつ　最も大きい(下側にある)壁マスの行番号<今いる行
    elif KabeDC[NowC][-1]<NowR:
        # 一番近い壁の行番号は(H+1)
        return H+1
    # 長さが1以上　かつ　今いるマスの行番号<最も小さい(上側にある)壁マスの行番号
    elif NowR<KabeDC[NowC][0]:
        # 一番近い壁の列番号はKabeDC[NowC][0](最も小さい壁マスの行番号)
        return KabeDC[NowC][0]    
    
    # 探索範囲の決定
    # 左
    l=0
    # 右
    r=len(KabeDC[NowC])-1

    # 1<(右-左)である間
    while 1<r-l:
        # 中央
        c=(l+r)//2

        # 中央の壁マスの行番号<今いるマスの行番号
        if KabeDC[NowC][c]<NowR:
            # 左=中央と更新
            l=c
        # そうでない場合(今いるマスの行番号<中央の壁マスの行番号)
        else:
            # 右=中央と更新
            r=c
    
    # 今いるマスから右方向で最も近い壁マスの行番号を返す
    return KabeDC[NowC][r]

# 上方向への二分探索
# 今いるマスから上方向で最も近い壁マスの行番号を返す
def NibutanU(NowR,NowC):
    # 長さが0⇔今いる行に壁マスがない場合
    if len(KabeDC[NowC])==0:
        # 一番近い壁の行番号は0
        return 0
    # 長さが1以上　かつ　今いるマスの行番号<最も小さい(上側にある)壁マスの行番号
    elif NowR<KabeDC[NowC][0]:
        # 一番近い壁の行番号は0
        return 0
    # 長さが1以上　かつ　最も大きい(下側にある)壁マスの行番号<今いるマスの行番号
    elif KabeDC[NowC][-1]<NowR:
        # 一番近い壁の行番号はKabeDC[NowC][-1](最も大きい壁マスの行番号)
        return KabeDC[NowC][-1]

    # 探索範囲の決定
    # 左
    l=0
    # 右
    r=len(KabeDC[NowC])-1

    # 1<(右-左)である間
    while 1<r-l:
        # 中央
        c=(l+r)//2

        # 中央の壁マスの行番号<今いるマスの行番号
        if KabeDC[NowC][c]<NowR:
            # 左=中央と更新
            l=c
        # そうでない場合(今いるマスの行番号<中央の壁マスの行番号)
        else:
            # 右=中央と更新
            r=c
    
    # 今いるマスから上方向で最も近い壁マスの行番号を返す
    return KabeDC[NowC][l]

# 今いる行、列
NowR,NowC=rs,cs

# 入力の受け取り
Q=int(input())

# Q回
for i in range(Q):
    # 入力の受け取り
    d,l=map(str,input().split())
    # 整数へ変換
    l=int(l)

    # 右へ進む場合
    if d=="R":
        # 今いるマスから右方向で最も近い壁マスの列番号
        KabeC=NibutanR(NowR,NowC)
        # l右へ進んだ時の列番号<壁マスの列番号なら
        if NowC+l<KabeC:
            # 進む
            NowC+=l
        # そうでなければ
        else:
            # 壁マスの手前まで進む
            NowC=KabeC-1
    
    # 左へ進む場合
    elif d=="L":
        # 今いるマスから左方向で最も近い壁マスの列番号
        KabeC=NibutanL(NowR,NowC)
        # 壁マスの列番号<l左へ進んだ時の列番号なら
        if KabeC<NowC-l:
            # 進む
            NowC-=l
        # そうでなければ
        else:
            # 壁マスの手前まで進む
            NowC=KabeC+1

    # 下方向へ進む場合
    elif d=="D":
        # 今いるマスから下方向で最も近い壁マスの行番号
        KabeR=NibutanD(NowR,NowC)
        # l下へ進んだ時の行番号<壁マスの行番号なら
        if NowR+l<KabeR:
            # 進む
            NowR+=l
        # そうでなければ
        else:
            # 壁マスの手前まで進む
            NowR=KabeR-1

    # 上方向へ進む場合
    elif d=="U":
        # 今いるマスから上方向で最も近い壁マスの行番号
        KabeR=NibutanU(NowR,NowC)
        # 壁マスの行番号<l上へ進んだ時の行番号なら
        if KabeR<NowR-l:
            # 進む
            NowR-=l
        # そうでなければ
        else:
            # 壁マスの手前まで進む
            NowR=KabeR+1

    # 今いるマスを出力
    print(NowR,NowC)

