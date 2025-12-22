class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n  # n未満の数
        is_prime[0] = is_prime[1] = False  # 0,1は素数でない

#テストケースをn=10やとして、√10＝3.16...位を考慮
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]: #i = 2と3に決まる
                # iの倍数をFalseにしていく
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)

#エラストテネスの篩
