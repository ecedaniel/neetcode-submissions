"""
Valid Anagram,

If length of s and t are different, return false

create a hashmap, which maps character to count

For i in range(len(s)):
increment count for that character in string s
increment count for that character in string t

for c in hashmap
if count of string s is not equal to count of string t, return False

return true

time complexity: O(n)
space complexity: O(n)


"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if len(s) != len(t): return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True