"""
AtCorder.ABC.250.D の Docstring

問題文
以下の条件を満たす整数 k を「 250 に似た数」と呼びます。

k が素数 p<q を使って k=p×q 
3
  と表される。
N 以下の「 250 に似た数」は全部でいくつありますか？

制約
N は 1 以上 10 
18
  以下の整数
入力
入力は以下の形式で標準入力から与えられる。

N
出力
答えを整数として出力せよ。

入力例 1
Copy
250
出力例 1
Copy
2
54=2×3 
3
  なので、「 250 に似た数」です。
250=2×5 
3
  なので、「 250 に似た数」です。
250 以下の「 250 に似た数」は、以上の 2 つです。

入力例 2
Copy
1
出力例 2
Copy
0
入力例 3
Copy
123456789012345
出力例 3
Copy
226863

"""
N = int(input())
LIMIT = 10**6

#エラトステネスの篩で素数全部列挙
is_prime = [True] * (LIMIT + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(LIMIT**0.5) + 1):
    if is_prime[i]:
        step = i 
        start = i * i 
        for j in range(start, LIMIT + 1, step):
            is_prime[j] = False
            
primes = [i for i in range(LIMIT + 1) if is_prime[i]]

#二分探索:primeの中でx以下の個数を返す
def upper_bound(arr,x ):
    lo,hi = 0,len(arr)
    while lo<hi:
        mid = (lo+hi)//2
        if arr[mid]<=x:
            lo = mid+1
        else:
            hi = mid
    return lo


ans = 0

for i, q in enumerate(primes):
    q3 = q * q * q
    if q3 > N:
        break 
    
    max_p = N // q3 # p*q^3 <= N を満たす最大の p
    if max_p < 2:
        continue

    # p < q も必要なので上限を縮める
    bound = min(max_p, q - 1)

    # bound 以下の素数の個数
    cnt = upper_bound(primes, bound)

    # ただし p は q より小さい必要があるので、qの位置(i)より前まで
    # primes は昇順なので q の前には i 個の素数がある
    if cnt > i:
        cnt = i

    ans += cnt

print(ans)