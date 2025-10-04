class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.tree = [0]*(2*self.n)
        for i in range(n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, idx, value):
        pos = self.n + idx
        self.tree[pos] = value
        pos >>= 1
        while pos:
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos+1]
            pos >>= 1

    def range_sum(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l <= r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if not (r & 1):
                res += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

def main():
    arr = [1,3,5,7,9,11]
    st = SegmentTree(arr)
    print("Sum 1..3", st.range_sum(1,3))
    st.update(1,10)
    print("After update arr", [st.range_sum(i,i) for i in range(len(arr))])
    print("Sum 1..3", st.range_sum(1,3))

if __name__ == "__main__":
    main()
