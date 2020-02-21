# my note
# 基礎： [class](https://medium.com/@weilihmen/%E9%97%9C%E6%96%BCpython%E7%9A%84%E9%A1%9E%E5%88%A5-class-%E5%9F%BA%E6%9C%AC%E7%AF%87-5468812c58f2)
# 基礎: [各種排序法](https://www.cnblogs.com/hf8051/p/11442134.html)
參考資料 [顏色字體總總](https://blog.csdn.net/u010177286/article/details/50358720)
老師推薦的除錯方法 用spyder  
畫流程圖工draw.io  
參考資料 ['__name__'介紹](http://blog.castman.net/教學/2018/01/27/python-name-main.html)
### 數列由小到大
```py
def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]  #項目對調
            j += 1
    return arr
    
```
### 知道數值長度
```py
def countBits(n):
    return n.bit_length()
 知道數值長度
 ````


### set mismatch
```python

        
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        holder = [-1] * len(nums) # Value of -1 means unvisited
        
        res = []
        for i in nums:
            if holder[i-1] != -1:
                res.append(i)
            holder[i-1] = i # Mark as visited
            
        res.append(holder.index(-1)+1) # Find remaining unvisited index
        
        return res
```
