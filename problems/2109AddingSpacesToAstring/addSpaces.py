from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index, result = 0, []
        
        for space in spaces:
            result.append(s[index:space])
            index = space
        
        result.append(s[index:])
        return " ".join(result)
        

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
sol = Solution()
print(sol.addSpaces(s, spaces))