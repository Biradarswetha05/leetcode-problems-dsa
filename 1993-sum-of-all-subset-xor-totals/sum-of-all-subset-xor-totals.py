class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for mask in range(1<<n):
            x=0
            for i in range(n):
                if mask&(1<<i):
                    x^=nums[i]
            res+=x
        return res
        