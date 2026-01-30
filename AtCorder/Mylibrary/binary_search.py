from bisect import bisect_left, bisect_right

# =====================
# 基本ユーティリティ
# =====================

def lower_bound(a, x):
    """
    a: 昇順ソート済み配列
    x: 探す値
    return: a[i] >= x となる最小の i
    """
    return bisect_left(a, x)

def upper_bound(a, x):
    """
    a[i] > x となる最小の i
    """
    return bisect_right(a, x)

def exists(a, x):
    """
    x が配列 a に存在するか
    """
    i = bisect_left(a, x)
    return i < len(a) and a[i] == x

def count_equal(a, x):
    """
    x の個数
    """
    return bisect_right(a, x) - bisect_left(a, x)
