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


## 1.merge sort 流程圖、學習歷程、文字說明
```
Divide and Conquer演算形式(跟quick sort 一樣)，利用不斷分割比較後再合併的排序法，時間複雜度是n log(n)  
Divide and Conquer演算法: 把問題先拆解(divide)成子問題，  
並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題.   
```

### 2.前言：雖然還是有參考網站上的想法（我太爛了），<br>但是下面的程式碼是我自己試出來的，希望助教可以給我指教讓我更好
   
   
### 這裡是老師講的概念然後把他大致上寫了下來
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3-1.jpg" weight = 200 height = 600><br>

<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3-3.jpg"  height=600 weight =200>  

### 3.概念跟想法
``` 
第一步  
創造一個function :mergeSort，定義它是把mylist排序的  
第二步  
創造變數i、j、m、mid 
創造陣列left[i]、right[j]還有原本的陣列Ｍ[m]   
(因為要設定left左邊，right右邊 所以設定一個中間值mid = len(mylist)//2     
第三步  
創造一個迴圈  
確認如果i、j沒有超過array長度然後來比較i、j  
如果i大那就是M(m) = L(i)，i++然後m++  **i跳到下一項繼續跟j比較，原本的Ｍ增加一個i**  
如果j大就相反  
第四步  
測試吧 
myList = [54,26,93,17,77,31,44,55,20]  
mergeSort(myList)  
print(myList) 
```
### 4.流程圖

流程圖一  
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW2流程圖1.png" weight = 200 height = 600>  
流程圖二  
<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW2流程圖2.png' weight = 200 height = 400>  


### 5.實測
**測試1** 出來的數值完全沒有變，想了一想發現**要呼叫mergeSort**，跑迴圈才有意義  
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3%20error1.png" weight = 200 height = 600>  
**測試2** 迴圈是跑出來了可是值卻不對（囧），想了很久想不出來，所以就用手寫寫一張看看，  
發現是**i、j比完大小後，沒有在M裡面新增較大的值** 
**所以就多寫一個，如果left、right長度>i、j就補充那個值  **  
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3%20error2.png" weight = 200 height = 600> <br>
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3-2.jpg" weight = 200 height = 600>  <br>
**測試3**:成功！(做完了才發現沒照格式做，所以正確格式附在程式碼裡面，拜託助教不要扣我分ＰＬＳ)  
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3%20.png" weight = 200 height = 600>  <br>


參考資料:[Comparison Sort: Merge Sort(合併排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)  

參考資料： [merge sort in python](https://www.educative.io/edpresso/merge-sort-in-python)  

