def can_achieve_min_load(A, K, min_load):
    """
    各トラックの積載量が少なくともmin_load以上となるように
    K台以下のトラックで配達できるかを判定する
    """
    truck_count = 1
    current_load = 0
    
    for weight in A:
        current_load += weight
        # 現在のトラックの積載量がmin_load以上になったら次のトラックへ
        if current_load >= min_load:
            truck_count += 1
            current_load = 0
    
    # 最後のトラックがmin_load未満でも、それ以前でK台使い切っていればOK
    # truck_countは「次のトラック」としてカウントしているので、実際に使ったトラック数はtruck_count-1
    # ただし、current_load > 0 の場合は最後のトラックも使っている
    
    # 別のアプローチ：K台で分割できるか
    # min_load以上の区間をK個作れるか
    segments = 0
    current_load = 0
    
    for weight in A:
        current_load += weight
        if current_load >= min_load:
            segments += 1
            current_load = 0
    
    return segments >= K


def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    total_sum = sum(A)
    
    # 二分探索
    # left: 達成可能な最小値の下限
    # right: 達成可能な最小値の上限
    left = 0
    right = total_sum // K + 1
    
    while right - left > 1:
        mid = (left + right) // 2
        if can_achieve_min_load(A, K, mid):
            left = mid
        else:
            right = mid
    
    print(left)


solve()
