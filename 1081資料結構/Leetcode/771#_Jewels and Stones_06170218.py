#771. Jewels and Stones

#Your input:J = "aA",S = "aAAbbbb"
#Output:3
#Expected:3
#檢查S裡有跟J一樣的寶石，並且算出數量



class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in S:
            if i in J:
                count = count + 1
        return count
