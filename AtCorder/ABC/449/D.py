"""
2 次元座標平面があり、座標が (x,y) である格子点は max(∣x∣,∣y∣) が偶数のとき黒、奇数のとき白で塗られています。

L≤x≤R かつ D≤y≤U を満たす整数の組 (x,y) のうち、座標 (x,y) が黒く塗られているものの個数を求めてください。

制約
−10 
6
 ≤L≤R≤10 
6
 
−10 
6
 ≤D≤U≤10 
6
 
入力される値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

L R D U
出力
答えを出力せよ。

入力例 1
Copy
-4 3 1 3
出力例 1
Copy
10


上の図のように、求める答えは 10 となります。

入力例 2
Copy
-14 14 -14 14
出力例 2
Copy
449
"""
l, r, d, u = map(int, input().split())
ans = 0

# |x| > |y|
for x in range(l, r + 1):
    if x % 2 == 0:
        D = max(d, -abs(x) + 1)
        U = min(u, abs(x) - 1)
        C = U - D + 1
        ans += max(C, 0)

# |x| <= |y|
for y in range(d, u + 1):
    if y % 2 == 0:
        L = max(l, -abs(y))
        R = min(r, abs(y))
        C = R - L + 1
        ans += max(C, 0)

print(ans)