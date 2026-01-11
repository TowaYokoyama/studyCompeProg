"""
N 種類のクッキーがそれぞれ 10 
100
  枚あります。 i 種類目のクッキーの 1 枚あたりの美味しさは A 
i
​	
  です。

これらのクッキーから合計で K 枚を選びます。クッキーの選び方は、選んだクッキーの種類の多重集合が一致するときかつその時に限り同じとみなします。

全ての選び方 ( 
K
N+K−1
​	
 ) 通りそれぞれについて、選んだクッキーの美味しさの和を考えます。これらを大きな値から順に重複を込めて S 
1
​	
 ,S 
2
​	
 ,… とするとき、S 
1
​	
 ,…,S 
X
​	
  を求めてください。

制約
1≤N≤50
1≤K≤10 
5
 
1≤X≤min(10 
5
 ,( 
K
N+K−1
​	
 ))
−10 
9
 ≤A 
i
​	
 ≤10 
9
 
入力は全て整数
入力
入力は以下の形式で標準入力から与えられる。

N K X
A 
1
​	
  … A 
N
​	
 
出力
K 枚選んだクッキーの美味しさの和として考えられる値を、大きなものから順に重複を込めて S 
1
​	
 ,S 
2
​	
 ,… とするとき、S 
1
​	
 ,…,S 
X
​	
  をこの順に改行区切りで出力せよ。

入力例 1
Copy
2 4 3
20 10
出力例 1
Copy
80
70
60
クッキーを 4 枚選ぶ方法は、「 1 種類目を k 枚、 2 種類目を 4−k 枚」(0≤k≤4) の 5 通りあり、選んだクッキーの美味しさの和はそれぞれ 80,70,60,50,40 となります。

入力例 2
Copy
3 100000 5
-1 -1 -1
出力例 2
Copy
-100000
-100000
-100000
-100000
-100000
異なるクッキーの選び方で美味しさの和が同じになることもあります。

入力例 3
Copy
9 14142 13
31 41 59 26 53 58 97 93 23
出力例 3
Copy
1371774
1371770
1371766
1371762
1371758
1371754
1371750
1371746
1371742
1371738
1371736
1371735
1371734
"""
import sys
import heapq
import bisect

input = sys.stdin.readline

def comb_multiset(n: int, r: int, cap: int) -> int:
    """
    重複組合せ: C(n+r-1, r-1)
    n: 選ぶ枚数, r: 種類数
    cap: これ以上は切り上げ（X までしか要らないので）
    """
    if r <= 1:
        return 1
    k = r - 1
    res = 1
    # res = Π_{i=1..k} (n+i)/i
    for i in range(1, k + 1):
        res = res * (n + i) // i
        if res > cap:
            return cap
    return res

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    # 同じ値ごとに圧縮: values[], counts[]
    values = []
    counts = []
    for a in A:
        if not values or values[-1] != a:
            values.append(a)
            counts.append(1)
        else:
            counts[-1] += 1

    v0 = values[0]
    c0 = counts[0]
    base = v0 * K

    # 値が全部同じなら、和は常に base（ただし重複あり）
    if len(values) == 1:
        mult = comb_multiset(K, N, X)  # 全タイプ数 N
        t = min(X, mult)
        out = "\n".join([str(base)] * t)
        sys.stdout.write(out + ("\n" if t > 0 else ""))
        return

    # 置き換えコスト（差分）: w_j = v0 - v_j (j>=1)
    weights = [v0 - values[j] for j in range(1, len(values))]
    group_counts = counts[1:]  # 各グループの種類数

    D = len(weights)  # 置き換え先グループ数 (= distinct values - 1)

    # Dijkstra的に「コスト最小の置き換え方」から列挙
    # state = (d1, d2, ..., dD) それぞれのグループから何枚取ったか
    start = (0,) * D
    pq = [(0, start)]
    seen = {start}

    remain = X
    ans_lines = []

    CAP = X  # 組合せ数は X 以上は全部 X で切り上げれば十分

    while pq and remain > 0:
        cost, state = heapq.heappop(pq)
        d = sum(state)
        if d > K:
            continue

        # この状態の「和」
        s = base - cost

        # この状態が作る “同じ和の重複回数（選び方の数）”
        # k0 = K-d を最大値グループに割り当て、各グループ内での分配は重複組合せ
        mult = comb_multiset(K - d, c0, CAP)
        if mult > 0:
            for dj, cj in zip(state, group_counts):
                mult = min(CAP, mult * comb_multiset(dj, cj, CAP))
                if mult >= CAP:
                    break

        # 出力（X で打ち切り）
        take = min(remain, mult)
        if take > 0:
            ans_lines.extend([str(s)] * take)
            remain -= take

        # 近傍（まだ枚数を増やせるなら、どれか1グループに+1）
        if d < K:
            for i in range(D):
                ns = list(state)
                ns[i] += 1
                ns = tuple(ns)
                if ns in seen:
                    continue
                seen.add(ns)
                heapq.heappush(pq, (cost + weights[i], ns))

    sys.stdout.write("\n".join(ans_lines) + ("\n" if ans_lines else ""))

if __name__ == "__main__":
    main()
