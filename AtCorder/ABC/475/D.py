"""
問題文
英小文字からなる文字列 S が与えられます。以下の条件を満たす素数 P が存在するなら 1 つ求めてください。

条件： P を先頭に余分な 0 をつけない十進表記で表した文字列を T とする。∣S∣=∣T∣ かつ、全ての 1≤i<j≤∣S∣ に対し、S 
i
​	
 =S 
j
​	
  と T 
i
​	
 =T 
j
​	
  が同値である。

制約
S は英小文字のみからなる長さ 1 以上 7 以下の文字列
入力
入力は以下の形式で標準入力から与えられる。

S
出力
問題文中の条件を満たす素数が存在しないとき -1 と出力せよ。
存在するとき、そのような素数を 1 つ出力せよ。答えが複数ある場合、どれを出力しても正解とみなされる。

入力例 1
Copy
motor
出力例 1
Copy
10607
この他、例えば 40709 などの出力でも正解とみなされます。また、例えば 81817 は条件を満たさないため不正解となります。

入力例 2
Copy
byebye
出力例 2
Copy
-1
条件を満たす素数が存在しないときは -1 と出力してください。

入力例 3
Copy
coconut
出力例 3
Copy
1010237
"""
from itertools import permutations


S = input()
N = len(S)


# 文字を「最初に登場した順」に番号化する
# 例: motor
# m -> 0
# o -> 1
# t -> 2
# r -> 3
char_id = {}

pattern = []

for c in S:
    if c not in char_id:
        char_id[c] = len(char_id)

    pattern.append(char_id[c])


K = len(char_id)


# 素数判定
def is_prime(x):
    if x < 2:
        return False

    if x % 2 == 0:
        return x == 2

    d = 3

    while d * d <= x:
        if x % d == 0:
            return False

        d += 2

    return True


# 長さ1なら 2,3,5,7 のどれかを割り当てればよい
# 10進数の先頭0は禁止だが、これらは全部OK
if N == 1:
    print(2)
    exit()


# 使う数字を決める
# 最大でも10個の数字からK個を選んで並べる
for digits in permutations(range(10), K):

    # 先頭が0だとダメ
    if digits[pattern[0]] == 0:
        continue

    # 数字を作る
    x = 0

    for p in pattern:
        x = x * 10 + digits[p]

    # 2桁以上なら、最後の数字は
    # 1, 3, 7, 9 のどれかでないと素数になれない
    if x % 10 not in (1, 3, 7, 9):
        continue

    # 素数なら答え
    if is_prime(x):
        print(x)
        exit()


# 全部試しても見つからなかった
print(-1)