s = input()

n = len(s)
ans = 0
for i in range(n):
    diff = 0
    k = 0
    while 0 <= i - k and i + k < n:
        if s[i - k] != s[i + k]:
            diff += 1

        if diff <= 1:
            ans += 1
            k += 1
        else:
            break

    diff = 0
    left = i - 1
    right = i
    while 0 <= left and right < n:
        if s[left] != s[right]:
            diff += 1

        if diff <= 1:
            ans += 1
            left -= 1
            right += 1
        else:
            break

print(ans)
