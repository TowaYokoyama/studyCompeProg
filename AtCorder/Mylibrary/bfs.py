from collections import deque

def bfs():
    queue = deque()
    queue.append(初期状態)
    visited[初期状態] = True

    while queue:
        state = queue.popleft()

        if ゴール判定:
            return 距離

        for 次の状態 in 遷移:
            if 未訪問:
                visited = True
                queue.append(次の状態)

    return -1
