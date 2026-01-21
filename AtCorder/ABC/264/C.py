"""
AtCorder.ABC.264.C の Docstring
H 
1
​	
  行 W 
1
​	
  列の行列 A と、H 
2
​	
  行 W 
2
​	
  列の行列 B が与えられます。

1≤i≤H 
1
​	
  かつ 1≤j≤W 
1
​	
  を満たす整数の組 (i,j) について、行列 A の i 行目 j 列目の要素は A 
i,j
​	
  です。
1≤i≤H 
2
​	
  かつ 1≤j≤W 
2
​	
  を満たす整数の組 (i,j) について、行列 B の i 行目 j 列目の要素は B 
i,j
​	
  です。
行列 A に対して、下記の 2 つの操作のうちどちらかを行うことを、好きなだけ（ 0 回でも良い）繰り返すことができます。

A の行を任意に 1 つ選んで削除する。
A の列を任意に 1 つ選んで削除する。
行列 A を行列 B に一致させることができるかどうかを判定して下さい。

制約
1≤H 
2
​	
 ≤H 
1
​	
 ≤10
1≤W 
2
​	
 ≤W 
1
​	
 ≤10
1≤A 
i,j
​	
 ≤10 
9
 
1≤B 
i,j
​	
 ≤10 
9
 
入力中の値はすべて整数
入力
入力は以下の形式で標準入力から与えられる。

H 
1
​	
  W 
1
​	
 
A 
1,1
​	
  A 
1,2
​	
  … A 
1,W 
1
​	
 
​	
 
A 
2,1
​	
  A 
2,2
​	
  … A 
2,W 
1
​	
 
​	
 
⋮
A 
H 
1
​	
 ,1
​	
  A 
H 
1
​	
 ,2
​	
  … A 
H 
1
​	
 ,W 
1
​	
 
​	
 
H 
2
​	
  W 
2
​	
 
B 
1,1
​	
  B 
1,2
​	
  … B 
1,W 
2
​	
 
​	
 
B 
2,1
​	
  B 
2,2
​	
  … B 
2,W 
2
​	
 
​	
 
⋮
B 
H 
2
​	
 ,1
​	
  B 
H 
2
​	
 ,2
​	
  … B 
H 
2
​	
 ,W 
2
​	
 
​	
 
出力
行列 A を行列 B に一致させることができる場合は Yes を、 一致させることができない場合は No を出力せよ。 ジャッジは英小文字と英大文字を厳密に区別することに注意せよ。

入力例 1
Copy
4 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
2 3
6 8 9
16 18 19
出力例 1
Copy
Yes
初期状態の行列 A から 2 列目を削除すると、行列 A は

1 3 4 5
6 8 9 10
11 13 14 15
16 18 19 20
となります。そこからさらに 3 行目を削除すると、行列 A は

1 3 4 5
6 8 9 10
16 18 19 20
となります。そこからさらに 1 行目を削除すると、行列 A は

6 8 9 10
16 18 19 20
となります。そこからさらに 4 列目を削除すると、行列 A は

6 8 9
16 18 19
となります。これは行列 B と一致します。 操作の繰り返しによって行列 A を行列 B に一致させることができるので Yes を出力します。

入力例 2
Copy
3 3
1 1 1
1 1 1
1 1 1
1 1
2
出力例 2
Copy
No
どのように操作を行っても、 行列 A を行列 B に一致させることはできません。 よって、No を出力します。
"""
H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]

H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

# 行の bit 全探索
for row_mask in range(1 << H1):
    # 残す行の数が H2 じゃなければスキップ
    if bin(row_mask).count("1") != H2:
        continue

    rows = []
    for i in range(H1):
        if (row_mask >> i) & 1:
            rows.append(i)

    # 列の bit 全探索
    for col_mask in range(1 << W1):
        # 残す列の数が W2 じゃなければスキップ
        if bin(col_mask).count("1") != W2:
            continue

        cols = []
        for j in range(W1):
            if (col_mask >> j) & 1:
                cols.append(j)

        # A の部分行列が B と一致するかチェック
        ok = True
        for i in range(H2):
            for j in range(W2):
                if A[rows[i]][cols[j]] != B[i][j]:
                    ok = False
                    break
            if not ok:
                break

        if ok:
            print("Yes")
            exit()

print("No")
