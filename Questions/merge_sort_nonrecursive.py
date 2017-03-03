class Solution(object):
    """docstring for Solution"""
    def __init__(self, arg):
        super(Solution, self).__init__()
        self.ans = arg
        k, N = 1, len(arg)
        while k < N:
            for left in range(0, N-k, 2*k):
                mid = left+k
                right = min(left + 2*k, N)
                self.merge(left, mid, right)
            k *= 2
        return

    def merge(self, left, mid, right):
        if left == right:
            return
        i, j = left, mid
        temp = [self.ans[x] for x in range(left, right)]
        for k in range(left, right):
            if i == mid:
                self.ans[k] = temp[j-left]
                j += 1
            elif j == right:
                self.ans[k] = temp[i-left]
                i += 1
            else:
                if temp[i-left] < temp[j-left]:
                    self.ans[k] = temp[i-left]
                    i += 1
                else:
                    self.ans[k] = temp[j-left]
                    j += 1
        return





arg = [12, 11, 13, 5, 6, 7]
solution = Solution(arg)
print solution.ans