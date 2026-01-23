A, B = map(int, input().split())
print(A | B)
A, B = map(int, input().split())
ans = 0

# 1点問題
if A % 2 == 1 or B % 2 == 1:
    ans += 1

# 2点問題
if (A // 2) % 2 == 1 or (B // 2) % 2 == 1:
    ans += 2

# 4点問題
if (A // 4) % 2 == 1 or (B // 4) % 2 == 1:
    ans += 4

print(ans)
