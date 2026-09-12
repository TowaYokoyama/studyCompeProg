N, M = map(int, input().split())

dic = {}

for i in range(M):
  a, b = map(int, input().split())
  if a not in dic:
    dic[a] = set([i])
  else:
    dic[a].add(i)
  if b not in dic:
    dic[b] = set([i])
  else:
    dic[b].add(i)

lst = []
for k, v in dic.items():
  lst.append((len(v), k, v))

lst = sorted(lst, reverse=True)

check_all = set(list(range(M)))
ans = 0
x = 0
y = 1
while lst[x][0] >= M // 2:
  check = check_all - lst[x][2]
  if len(check) == 0:
    ans += N-x-1
    x += 1
    y = x + 1
  else:
    if len(check - lst[y][2]) == 0:
      ans += 1
      
    if y < len(lst)-1:
      if lst[x][0] + lst[y+1][0] >= M:
        y += 1
      else:
        x += 1
        y = x + 1
    else:
      x += 1
      y = x + 1
  
  if y >= len(lst):
    break

print(ans)