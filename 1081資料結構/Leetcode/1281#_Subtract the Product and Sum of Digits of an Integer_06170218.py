#1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a,b = 0,1
        for i in str(n):
            a += int(i)
            b *= int(i)
        return b-a
        
