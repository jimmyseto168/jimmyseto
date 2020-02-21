# Heap與Merge 的sort比較. 
### 時間複雜度之比較
<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/五種sort的時間複雜度比較.png' height = 300 weight = 600>  

#### 相同:  
最久與最快的都是Ο( n log n)  
#### 不同：  
Heapsort:  
**空間複雜度(Space Complexity)** ：Ο(1) 原地置換(In-Place)  
**穩定性(Stable/Unstable)** ：不穩定(Unstable)     
Mergesort:   
**空間複雜度(Space Complexity)：** Ο(n)  需要暫時性的暫列存放每回合Merge後的結果  
**穩定性(Stable/Unstable)：** 穩定(Stable)  
Merge Sort屬於Divide and Conquer演算法（問題divide成子問題，將子問題的結果conquer）  
Heap Sorty則利用完全二元樹來排序
### 名詞解釋：
```
算法說明：
建立MaxHeap： Ο(n)
執行n-1次Delete Max：(n-1) × Ο(log n) = Ο( n log n)
Ο(n) + Ο( n log n) = Ο( n log n)
  
穩定排序法(stable sorting)，如果鍵值相同之資料，在排序後相對位置與排序前相同時，稱穩定排序。  
【例如】 
排序前：3,5,19,1,3*,10  
排序後：1,3,3*,5,10,19  (因為兩個3, 3*的相對位置在排序前與後皆相同。)  
不穩定排序法(unstable sorting)，如果鍵值相同之資料，在排序後相對位置與排序前不相同時，稱不穩定排序。  
【例如】  
排序前：3,5,19,1,3*,10  
排序後：1,3*,3,5,10,19  (因為兩個3, 3*的相對位置在排序前與後不相同。)  
```


### 參考資料: [穩不穩](http://spaces.isu.edu.tw/upload/18833/3/web/sorting.htm)  
### 參考資料: [演算法介紹](http://notepad.yehyeh.net/Content/Algorithm/Sort/Merge/Merge.php)
