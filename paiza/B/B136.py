"""
B136 の Docstring

N H W
sy sx
s
c_{1,1} c_{1,2} ... c_{1,W}
c_{2,1} c_{2,2} ... c_{2,W}
...
c_{H,1} c_{H,2} ... c_{H,W}


e_1
e_2
...
e_N

3 3 3
2 1
FRB
3 6 2
0 4 1
5 0 7


3
6
4

"""
N,H,W = map(int, input().split())
sy, sx = map(int, input().split())
s = input()
c = [list(map(int,input().split())) for _ in range(H)]
y,x = sy-1,sx-1 #今のポジション
#１文字ずつでループ
for cmd in s:
    if cmd == 'F':
        y -=1
    elif cmd == 'B':
        y +=1
    elif cmd == 'L':
        x -=1
    elif cmd == 'R':
        x +=1
        print(c[y][x])