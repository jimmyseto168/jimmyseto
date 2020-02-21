#1221. Split a String in Balanced Strings
#分割出來的L跟R長度相等，output為可以分割幾次
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        output = 0
    
        for i in s :
            if i == 'R' :
                r += 1
            else :
                r -= 1
            
            if r == 0 :
                output += 1
        return output
