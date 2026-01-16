"""
AtCorder.ABC.426.A の Docstring
問題文
ある OS のバージョンは古い順に "Ocelot", "Serval", "Lynx" です。
バージョン X がバージョン Y 以降のバージョンであるか判定してください。
なお、バージョン X 自身もバージョン X 以降のバージョンであるものとします。

制約
X,Y は "Ocelot", "Serval", "Lynx" のいずれか (引用符を含まない)
入力
入力は以下の形式で標準入力から与えられる。

X Y
出力
バージョン X がバージョン Y 以降のバージョンであれば Yes 、そうでなければ No と出力せよ。

入力例 1
Copy
Serval Ocelot
出力例 1
Copy
Yes
バージョン Serval はバージョン Ocelot 以降のバージョンです。そのため、 Yes と出力します。

入力例 2
Copy
Serval Lynx
出力例 2
Copy
No
バージョン Serval はバージョン Lynx 以降のバージョンではありません。そのため、 No と出力します。

入力例 3
Copy
Ocelot Ocelot
出力例 3
Copy
Yes
バージョン Ocelot 自身もバージョン Ocelot 以降のバージョンです。そのため、 Yes と出力します。
"""
X,Y = input().split()
list =["Ocelot" ,"Serval" ,"Lynx"]

if X ==  "Lynx":
    print("Yes")
elif X == "Serval" and Y == "Serval" or Y == "Ocelot":
    print("Yes")
elif X == "Ocelot" and Y == "Ocelot":
    print("Yes")

else:
    print("No")        
