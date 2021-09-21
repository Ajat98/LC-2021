"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
E.g.
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3
"""



class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        highest = 0
        
        """ //Original sloppy solution
        for i in range(len(nums)):
            print(i, nums[i])
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                count = 0
            if count > highest:
                highest = count
                """
        
    
        #Shorter Code Solution, better memory + time performance
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0:
                count = 0
            if count > highest:
                highest = count
        return highest      
            
