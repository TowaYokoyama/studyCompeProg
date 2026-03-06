import sys
from bisect import bisect_left
def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    W, H = int(input_data[idx]), int(input_data[idx+1]); idx += 2
    N = int(input_data[idx]); idx += 1
    strawberries = []
    for _ in range(N):
        p, q = int(input_data[idx]), int(input_data[idx+1]); idx += 2
        strawberries.append((p, q))
    A = int(input_data[idx]); idx += 1
    a_cuts = [int(input_data[idx+i]) for i in range(A)]; idx += A
    B = int(input_data[idx]); idx += 1
    b_cuts = [int(input_data[idx+i]) for i in range(B)]; idx += B
    # ピースの境界列を作る（最後にW, Hを追加）
    a_bounds = a_cuts + [W]   # x方向の境界
    b_bounds = b_cuts + [H]   # y方向の境界
    # 連想配列: {ピースID -> イチゴ数}
    piece_count = {}
    for p, q in strawberries:
        # 二分探索でピースIDを特定
        X = bisect_left(a_bounds, p)
        Y = bisect_left(b_bounds, q)
        piece_id = (X, Y)
        piece_count[piece_id] = piece_count.get(piece_id, 0) + 1
    total_pieces = (A + 1) * (B + 1)
    pieces_with_strawberry = len(piece_count)
    M = max(piece_count.values())  # 最大値
    if pieces_with_strawberry == total_pieces:
        # 全ピースにイチゴあり → 最小値はmapの最小
        m = min(piece_count.values())
    else:
        # イチゴなしピースが存在 → 最小値は0
        m = 0
    print(m, M)
solve()