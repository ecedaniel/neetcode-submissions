"""
for a given array nums, we can compute the prefix for each element in array nums and 
store it in output array.

and then, compute the postfix starting from the right most element, and multiply with 
what is already stored in the output array.

return result

time complexity is O(2n) => O(n) 
Space complexiy is O(1) assuming output array does not count as a memory.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
