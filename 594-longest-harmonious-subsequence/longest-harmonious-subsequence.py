class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        res = 0
        for k in count:
            if k + 1 in count:
                res = max(res, count[k] + count[k + 1])
        return res
        