import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def add(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    
    N = int(input_data[idx]); idx += 1
    Q = int(input_data[idx]); idx += 1
    
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = int(input_data[idx]); idx += 1
    
    ft = FenwickTree(N)
    for i in range(1, N + 1):
        ft.add(i, S[i])
    
    results = []
    for _ in range(Q):
        query_type = int(input_data[idx]); idx += 1
        if query_type == 1:
            L = int(input_data[idx]); idx += 1
            R = int(input_data[idx]); idx += 1
            results.append(ft.range_sum(L, R))
        else:
            X = int(input_data[idx]); idx += 1
            V = int(input_data[idx]); idx += 1
            delta = V - S[X]
            S[X] = V
            ft.add(X, delta)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
