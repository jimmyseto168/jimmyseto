#1295. Find Numbers with Even Number of Digits
import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if i != 0:
                ln = math.floor(math.log10(i))
                if ln % 2 == 1:
                    res += 1
        return res
