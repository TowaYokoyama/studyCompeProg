import sys
from collections import deque

# 入力の読み込み
input = sys.stdin.read().split()
if not input:
    exit()

n = int(input[0])
m = int(input[1])
s = input[2:]

# 方向の定義 (x, y)
dx4 = [1, -1, 0, 0]
dy4 = [0, 0, 1, -1]

# 訪問フラグ: 5 * n * m の配列 (0で初期化)
# 状態: 5 * (x * m + y) + direction
# direction: 0-3は移動中、4は停止状態
fl = [0] * (5 * n * m)
q = deque()

# 初期状態: (1, 1) の位置で停止状態(4)からスタート
start_idx = 5 * (1 * m + 1) + 4
fl[start_idx] = 1
q.append(start_idx)

while q:
    od = q.popleft()
    
    # インデックスから状態を復元
    pos_idx = od // 5
    x = pos_idx // m
    y = pos_idx % m
    d = od % 5

    if d == 4:
        # 停止状態からの移動開始
        for i in range(4):
            nx, ny = x + dx4[i], y + dy4[i]
            # 範囲外チェックは元のコードに準じて省略（周囲が壁前提）
            if s[nx][ny] == '.':
                nid = 5 * (nx * m + ny) + i
                if fl[nid] == 0:
                    fl[nid] = 1
                    q.append(nid)
    else:
        # 直進中
        nx, ny = x + dx4[d], y + dy4[d]
        if s[nx][ny] == '.':
            # そのまま進める場合
            nid = 5 * (nx * m + ny) + d
            if fl[nid] == 0:
                fl[nid] = 1
                q.append(nid)
        else:
            # 岩に当たって停止する場合
            nid = 5 * (x * m + y) + 4
            if fl[nid] == 0:
                fl[nid] = 1
                q.append(nid)

# 到達可能なマスの合計を計算
res = 0
for i in range(n * m):
    # 5つの状態（4方向の通過 or 停止）のうち、どれか1つでも到達していればカウント
    if any(fl[5 * i + j] for j in range(5)):
        res += 1

print(res)