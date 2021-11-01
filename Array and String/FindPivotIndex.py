"""
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, 0
        
        for i in range(len(nums)):
            
            #find sum to right
            right = sum(nums[i+1:len(nums)]) #need i+1 to not include current index
            #print(right, i)
                
            #find sum from left
            left = sum(nums[0:i])
            #print(left, i)
                
            if right == left:
                return i
            else:
                right, left = 0, 0
                
        #Case where right == left is never true        
        return -1
            
            
