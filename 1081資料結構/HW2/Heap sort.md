 ### 1.Heap Sort流程圖、學習歷程、文字說明


### 2.前言：
**Heap排序法使用堆積樹（Heap tree），樹是一種資料結構<br>
而堆積樹是一個二元樹，每個父節點最多只有兩個子節點。**  
<示意圖>  
<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/父節點.png' height = 300 weight = 100>  

```
堆積樹的父節點若小於子節點，則稱之為最小堆積（Min heap） 
父節點若大於子節點，則稱之為最大堆積（Max heap）  
而同一層的子節點則無需理會其大小關係**
```

### 3.想法＆概念  
第一步：[heapify]創造Ａ陣列、父節點、與Ａ長度、左右點與最大點  
第二步：用if表示。如果子節點存在且大於父節點，則把largest改成left. or right  
如果largest被交換過了，則對調位子  
第三步：[heap_sort]創造陣列Ａ與長度length.   
對含有子節點的節點heapify,創造一個maxheap–>最大的數字在上面。
第四部：與最後一個值對調，然後直接忽略最大的值。繼續用length-1跟0比 (重要概念)  
 

### 4.流程圖  
流程圖1創造Ａ陣列、父節點、與Ａ長度、左右點與最大點   
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/data%20structure%20and%20algorithms/創造Ａ.png" height = 100 weight = 200>  
流程圖2heapify意思(因為很久以前做，所以變數不太一樣，但意思是這樣)  
<img src='https://github.com/jimmyseto168/jimmyseto/blob/master/image/heapify流程圖.png' height = 300 weight = 450>  
流程圖3 陣列Ａ與長度length  
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/data%20structure%20and%20algorithms/heap_sort流程.png" height = 100 weight = 200>. 
流程圖4 因為只需要對父節點做，所以從length//2 -1 開始heapify    
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/data%20structure%20and%20algorithms/建立MaxHeap.png" height = 400 weight = 200>  
流程圖5 與最後一個值對調，然後直接忽略最大的值  
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/data%20structure%20and%20algorithms/MAXHEAP.png" height = 400 weight = 200>  
### 5.實測
**測試1**  
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/data%20structure%20and%20algorithms/heap%20while實測.png" height = 400 weight = 200>   
  
顯示錯誤：KeyboardInterrupt，但我也不太清楚原因，所以還是照之前看到的邏輯來寫    

**測試2**   (用if解法，補上作業格式)  
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/data%20structure%20and%20algorithms/heap完成圖.png" height = 400 weight = 200>  


### 參考資料: [heap sortＣ＋＋寫法](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)
### 參考資料: [geekforgeeks](https://www.geeksforgeeks.org/python-program-for-heap-sort/)
### 參考資料: 老師github


