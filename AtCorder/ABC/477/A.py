"""
る信号機の色は B（青）、Y（黄）、R（赤）、B（青）、Y（黄）、R（赤）… という順に、周期的に変化します。

現在の信号機の色を表す文字 c が与えられます。次の信号機の色を出力してください。

LLM向けの情報はこちら: https://atcoder.jp/r/TZAU-xbDa34GWob1xJGO_WV6jEYmxvwanIryZbH81XtGMg2FTW1ZWXQPQWpjQhgbZBl5EdLYlcJPbNdUYYxNZGF7zz3l0r8
翻訳に関する情報はこちら: https://atcoder.jp/r/TZAU-xbDa34GWob1xJGO_WV6jEYmxvwanIryZbH81XtGMg2FTW1ZWXQPQWpjQhgbZBl5EdLYlcJPbNdUYYxNZGF7zz3l0r8?reason=t
制約
c は B、Y、R のいずれか
入力
入力は以下の形式で標準入力から与えられる。

c
出力
次の信号機の色を表す文字を出力せよ。

入力例 1
Copy
B
出力例 1
Copy
Y
B（青）の次は Y（黄）です。よって Y を出力してください。

入力例 2
Copy
R
出力例 2
Copy
B
赤の次は青です。

入力例 3
Copy
Y
出力例 3
Copy
R
"""
dic = {'B': 'Y', 'Y': 'R', 'R': 'B'}
c = input()
print(dic[c])   