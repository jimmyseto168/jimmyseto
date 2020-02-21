def quick_sort(list): #extra-place
    smaller = []
    bigger = []
    keylist = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] #第一個數為key值
        for i in list:
            if i < key: #比key值小的數
                smaller.append(i)
            elif i > key: #比key值大的數
                bigger.append(i)
            else:
                keylist.append(i)

    smaller = quick_sort(smaller)  #新的數列繼續用上面那個 我們def過的方法
    bigger = quick_sort(bigger)
    return smaller + keylist + bigger
mmmmm = [20,9,100,0,55,3,11,544,86,64,85]
print("大小順序是",quick_sort(mmmmm))
