"""
英小文字からなる文字列 S が与えられます。

S の各文字を並び替えることでどの隣り合う 2 文字も異なるようにすることが可能か判定し、可能な場合はそのような並び替えを一つ求めてください。

T 個のテストケースが与えられるので、それぞれについて答えを求めてください。

制約
1≤T≤3×10 
5
 
S は英小文字からなる長さ 1 以上 10 
6
  以下の文字列
全てのテストケースにおける S の長さの総和は 10 
6
  以下
入力
入力は以下の形式で標準入力から与えられる。

T
case 
1
​	
 
case 
2
​	
 
⋮
case 
T
​	
 
i 番目 (1≤i≤T) のテストケース case 
i
​	
  は以下の形式で与えられる。

S
出力
各テストケースに対する答えを順に改行区切りで出力せよ。

各テストケースについて、どの隣り合う 2 文字も異なるように S を並び替えることが不可能な場合は No を出力せよ。

可能な場合はそのような並び替えを S 
′
  として以下の形式で出力せよ。

Yes
S 
′
 
条件を満たす S の並び替え方が複数存在する場合、どれを出力しても正答となる。

入力例 1
Copy
3
aiiw
doodoo
aabbababcacababaaba
出力例 1
Copy
Yes
iwai
No
Yes
ababacabababacababa
1 番目のテストケースについて考えます。

iwai は aiiw を並び替えてできる文字列で、どの隣接する 2 文字も異なります。したがって、iwai を出力すると正答となります。

この他にも、wiai や iawi などを出力しても正答となります。
"""
import heapq
from collections import Counter

T = int(input())

for _ in range(T):
    S = input()
    N = len(S)

    cnt = Counter(S)

    mx = max(cnt.values())

    # 不可能判定
    if mx > (N + 1) // 2:
        print("No")
        continue

    # 最大ヒープ
    hq = []

    for c, v in cnt.items():
        heapq.heappush(hq, (-v, c))

    ans = []

    prev = ""

    while hq:
        v1, c1 = heapq.heappop(hq)

        # 直前と違うなら採用
        if c1 != prev:
            ans.append(c1)
            prev = c1

            v1 += 1  # マイナスなので +1

            if v1 != 0:
                heapq.heappush(hq, (v1, c1))

        else:
            # 次点を使う
            v2, c2 = heapq.heappop(hq)

            ans.append(c2)
            prev = c2

            v2 += 1

            if v2 != 0:
                heapq.heappush(hq, (v2, c2))

            heapq.heappush(hq, (v1, c1))

    print("Yes")
    print("".join(ans))