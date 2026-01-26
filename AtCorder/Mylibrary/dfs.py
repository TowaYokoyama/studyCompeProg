def dfs():
    stack = []
    stack.append(初期状態)
    visited[初期状態] = True

    while stack:
        state = stack.pop()   # ← ここが違う

        if ゴール判定:
            return True       # DFS は距離を保証しない

        for next_state in 遷移:
            if 未訪問:
                visited[next_state] = True
                stack.append(next_state)

    return False
