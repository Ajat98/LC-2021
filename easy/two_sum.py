"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

E.g.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
  
        #Slow runtime solution
#         for i in range(len(nums)):
#             for x in range(len(nums)):
#                 if (target - nums[i]) == nums[x] and (x != i):
#                     return (i, x)
#                 #print(i, nums[i], x, nums[x])
        
        #Optimal Solution O(n)
        d = {}
        for i, x in enumerate(nums):
            z = target - x #target - x gives us the value we need to find, if this value is in our dict, we simple return i, and the index stored in d[z]
            if z in d:
                return (d[z], i)
            else:
                d[x] = i
