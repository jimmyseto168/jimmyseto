# Hash Table 原理
----
- Hash Table:把資料放到Table裡面，並根據(Key)值直接查詢在內存存儲位置的資料結構。  
通過計算一個(key)值的函數，將所需查詢的數據映射到表中一個位置來查詢記錄，這加快了查找速度。
- 如何計算:  
利用ＭＤ5這個密碼雜湊函式，將資料（如一段文字）運算變為另一固定長度值  

# 學習歷程
----
1. 先寫一個把字串轉成md5格式的function  
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW4/螢幕快照%202019-12-06%20下午8.42.13.png)  
2. add: 設a = (key)值轉化過後除以我們index(a)的個數(＝5)所以必定為0,1,2,3,4  
   假設加入1裡面，則把新加入的值(new_node)加到data裡面  
   ![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW4/螢幕快照%202019-12-06%20下午8.56.05.png)  
3. remove: 如果node值==key，則現在這個節點被下個節點取代  
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW4/螢幕快照%202019-12-06%20下午8.56.14.png)  
4. contains: node一直往下找，直到找到key為止return true,沒找到則return False  
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW4/螢幕快照%202019-12-06%20下午9.08.06.png)  



# 流程圖
----
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW4/MD5.png)





參考資料：[Hash Table Infro()](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)  
參考資料：老師上課影片. 
