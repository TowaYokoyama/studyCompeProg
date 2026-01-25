class SegTree:
    def __init__(self, arr):
        n = len(arr)
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.seg = [0] * (2 * self.size)

        for i in range(n):
            self.seg[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.seg[i] = self.seg[i * 2] + self.seg[i * 2 + 1]

    def update(self, i, v):
        i += self.size
        self.seg[i] = v
        while i > 1:
            i //= 2
            self.seg[i] = self.seg[i * 2] + self.seg[i * 2 + 1]

    def query(self, l, r):
        l += self.size
        r += self.size
        s = 0
        while l < r:
            if l & 1:
                s += self.seg[l]
                l += 1
            if r & 1:
                r -= 1
                s += self.seg[r]
            l //= 2
            r //= 2
        return s
