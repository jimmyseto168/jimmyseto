class Solution(object):
    def heapify(self, A, root, length): #創造Ａ陣列、父節點、與Ａ長度
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < length and A[left] > A[largest]: #用if表示。如果子節點存在且大於父節點，則把largest改成left. or right
            largest = left

        if right < length and A[right] > A[largest]:
            largest = right

        if largest != root:                        #如果largest被交換過了，則對調位子
            A[largest], A[root] = A[root],A[largest]
            self.heapify(A, largest, length)


    def heap_sort(self,A):   #主程式，在這裡說陣列長度。
        length = len(A)
        for i in range(length // 2 - 1, -1, -1):
            self.heapify(A, i, length)   #heapify含有子節點的節點，詳情請看附圖。
        for i in range(length - 1, 0, -1):   #與最後一個值對調 
            A[0], A[i] = A[i], A[0]
            self.heapify(A, 0, i)     #默認從第０個位子與i開始對調，i會一直遞減，這樣就像是最後一個值消失了
        return A

test = [2,5,6,446,7,8,9,4,7,9]
output = Solution().heap_sort(test)
print("The Sort is",output)
print( "The length is " ,len(output), ".")
