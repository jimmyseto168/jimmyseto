`程式碼`
class solution (object):
    def mergeSort(self,mylist):
        if len(mylist) > 1:
            mid = len(mylist) // 2
            left = mylist[ :mid]
            right = mylist[mid: ]
            i = 0
            j = 0
            m = 0
            self.mergeSort(left)
            self.mergeSort(right)
        
            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    mylist[m] = left[i]
                    i+=1
                    m+=1
                else:
                    mylist[m]  = right[j]
                    j+=1
                    m+=1
                
            while i < len(left):
                mylist[m] = left[i]
                i += 1
                m += 1

            while j < len(right):
                mylist[m]=right[j]
                j += 1
                m += 1
        return mylist

mylist = [1,2,7,3,9,6,46,56,77,10,0,4,98]
print("結果是 : ",solution().mergeSort(mylist))

