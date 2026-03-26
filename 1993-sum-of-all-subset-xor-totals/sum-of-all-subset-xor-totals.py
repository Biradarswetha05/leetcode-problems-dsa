class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        x=0
        for v in nums:
            x|=v
        return x*(1<<(len(nums)-1))
        