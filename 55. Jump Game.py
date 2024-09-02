class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        current_pos=0
        long_jump=0
        step=0
        for i in range(n-1):
            long_jump=max(long_jump,i+nums[i])
            if i==current_pos:
                step +=1
                current_pos=long_jump
            if current_pos>=n-1:
                break
        return step
            
nums = [2, 3, 1, 1, 4]
# nums=[3, 2, 1, 0, 4]
res=Solution()
ans=res.canJump(nums)
print(ans)