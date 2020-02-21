## numpy是什麼

```
NumPy是Python語言的一個擴充程式庫。支援高階大量的維度陣列與矩陣  
運算，此外也針對陣列運算提供大量的數學函式函式庫，下面有個例子  
直接在python裡面打list + list ，python 會不知道怎麼辦，  
所以會在第一個list後面直接加上一個list，而numpy就是直接兩個李斯特相加  
```  

### 如圖
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/Python/numpy.png" height = 400 weight = 200>  

` 然後numpy也可以print出布林值，只要輸入print() `

<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/Python/numpy%20print.png' height = 300 weight = 200>

## 以下是我在維基百科找的基本運用模式

### 建立陣列
<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/Python/numpy基本運算.png' height = 600 weight = 200>  

### 線性代數
<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/Python/numpy線性代數.png' height = 600 weight = 200> 



> 平均
```py
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))
```

> 中位數
```py
# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))
```
> 標準差
```py
# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))
```
> 相關係數
```py
# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))
```
