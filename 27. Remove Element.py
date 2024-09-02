'''Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.'''

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pos=0
        n=len(nums)
        for  i in range(n):
            if nums[i] != val:
                nums[pos]=nums[i]
                pos +=1
                print(pos)
        print(pos)
        return pos

nums = [3,2,2,3,1]
val = 3
obj=Solution()
result=obj.removeElement(nums,val)
print(result)





