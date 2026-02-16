import sys
from math import log2, ceil

def main():
    input = sys.stdin.readline
    
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Sparse Table for Range Maximum Query
    # sparse_table[k][i] = max of A[i:i+2^k]
    
    if N == 0:
        for _ in range(Q):
            print(0)
        return
    
    LOG = max(1, ceil(log2(N + 1)))
    
    # Initialize sparse table
    sparse_table = [[0] * N for _ in range(LOG + 1)]
    
    # Base case: intervals of length 1
    for i in range(N):
        sparse_table[0][i] = A[i]
    
    # Build sparse table
    for k in range(1, LOG + 1):
        length = 1 << k
        half = 1 << (k - 1)
        for i in range(N - length + 1):
            sparse_table[k][i] = max(sparse_table[k-1][i], sparse_table[k-1][i + half])
    
    # Precompute log2 values
    log_table = [0] * (N + 1)
    for i in range(2, N + 1):
        log_table[i] = log_table[i // 2] + 1
    
    # Answer queries
    results = []
    for _ in range(Q):
        L, R = map(int, input().split())
        # Convert to 0-indexed
        l = L - 1
        r = R - 1
        length = r - l + 1
        k = log_table[length]
        # max of [l, l + 2^k) and [r - 2^k + 1, r + 1)
        ans = max(sparse_table[k][l], sparse_table[k][r - (1 << k) + 1])
        results.append(ans)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
