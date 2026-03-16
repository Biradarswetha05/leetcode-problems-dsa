class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=0
        rmax=0
        left=0
        w=0
        right=len(height)-1
        while left<right:
            if height[left]<height[right]:
                w+=max(0,lmax-height[left])
                lmax=max(lmax,height[left])
                left+=1
            else:
                w+=max(0,rmax-height[right])
                rmax=max(rmax,height[right])
                right-=1
        return w
        