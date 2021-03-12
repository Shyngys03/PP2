class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        prod = 1
        cnt = 0
        for i in s:
            prod *= int(i)
            cnt += int(i)
        return prod - cnt