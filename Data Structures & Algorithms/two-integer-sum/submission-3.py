"""
we can have a hashmap with value to index
for each element in the array, compute the difference between target and that element.
if that difference is in the hashmap, return index from the hashmap and i
else, store the index into the hashmap

return 

"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[n] = i

        return