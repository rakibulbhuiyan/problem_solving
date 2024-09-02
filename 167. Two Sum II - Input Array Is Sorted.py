'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
 find two numbers such that they add up to a specific target number. 
 Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2]
 of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            total=numbers[i]+numbers[j]
            if total==target:
                return [i+1,j+1]
            elif total>target:
                j -=1
            else:
                i+=1
            
        
        



numbers = [1,2,3,4,4,9,56,90]
target = 8

res=Solution()
result=res.twoSum(numbers,target)
print(result)
 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]


'''for i in range(n):
            for j in range(i+1,n):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]'''