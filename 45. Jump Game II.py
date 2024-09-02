'''
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].
'''
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        pos=nums[0]
        n=len(nums)
        step=0
        for i in range(n):
            if i>step:
                return False
            step=max(step,nums[i])
        return pos
        
        
            
res=Solution()
nums = [2, 3, 1, 1, 4]  #output=2
# nums=[3, 2, 1, 0, 4]  #output=2
ans=res.canJump(nums)
print(ans)