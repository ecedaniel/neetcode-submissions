# Make a hashmap that maps a number and index of an array
# We can compute the difference between the target and ith element of the array and see if it is
# in our hashmap
# if it exists, return the index inside hashmap and the current index
# else put the element in the hashmap
# 32 bit => max size = 2^32 - 1 ~~ 4 billion
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i
        return
        