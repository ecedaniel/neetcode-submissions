# have a result array
# compute prefix and store them in result array
# [1, 2, 4, 6]
# prefix: start at 1 and then update by multipliying to ith element of nums
# [1, 1, 2, 8]
# postfix: start at 1 and then update by multiplying to the ith element of nums
# note that we have to start from the last element
# [48 24 6 1]
# and then multiply the prefix array and postfix array
# time: O(n) memory: O[n]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result