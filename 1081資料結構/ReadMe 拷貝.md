# jimmyseto 的資料結構筆記>___< 

 目前就讀巨資學院  
 因為修了data structures and algorithms這門課而開始進入github世界  
 裡面記載著一些程式碼and解釋  
 先看pseudocode然後暸解他的邏輯再用自己熟悉的code寫出來
 也是我學習的過程  
 
 \*這是我顆顆顆
 
 <img src='image/P_20190623_182626_vHDR_Auto.jpg' height=200 weight =200> 
 
 
 ## 心得
 **這學期修了這門課，有種誤上賊船的感覺，讓我知道原來工程師的世界比我想像的複雜許多，不過經過一學期，<p>  
 我感覺到了明顯的進步，雖然可能還是跟不上老師的腳步，但我已經很滿足了，期中的時候好幾次真的想退選了 <p>   
 ，但都想著撐一下就過了，沒想到學期末那麼快就到來了，很慶幸我還活著（？我是想說很高興我撐住了，也很 <p>   
 感謝老師跟助教的訓練，讓我知道我是多麽的爛多麼的需要磨練，很記得老師在課堂講了一段話：「真的不要太 <p>   
 自滿，牆外的世界還有很多高手，你在我眼裡只不過是一個在愚昧山丘而沾沾自喜的人。」讓我再次體會自己的  <p>  
 渺小，總結就是蔡老師的課是真的有學到東西的課，蠻推薦學弟妹來修的。**  

## 課堂筆記

### week 2  
- linked-List  
[linked-List:intro](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/68747470733a2f2f692e696d6775722e636f6d2f315163347548442e706e67.png)
array需要一整塊連續的記憶體空間，刪除需要整塊做調整
lined-list可以由一個一個空間拼湊起來，這樣刪除的話，就不用整塊調整
影片裡面有新增，假如我要新增2，nodeA = Node(2)，nodeA.next=nodeB，也就是nodeA -> nodeB
還有走訪當current.next!=none時，count就+1，不再+的話代表是最後一個，那就可以知道長度了
除了上述兩個功能，還有刪除和查詢兩個功能可以操作  
### week 3  
- Stack & Queue  
[堆疊-stack](https://medium.com/@lufor129/資料結構複習-六-堆疊-stack-348d3db7bbc1)  
堆疊可以被認為是有約束力的線性表，插入和刪除接操作於top頂點位置。現實生活中也常常能遇到堆疊的例子  
，例如餐廳的盤子疊，洗盤子時必定是從上面開始洗，放盤子也是從上面開始放，這種操作方式稱為後入先出  
(Last In First Out)，LIFO。  

### week 4   

- Set 資料結構 : 循序儲存  
要表達一個集合，可以直觀的用一條一維的 int 陣列：將集合裡的所有元素，依序放進陣列中。再用一個變數，記錄元素總數。  
- Set 資料結構 : 索引儲存  
另外一種表達集合的方法，是用一條一維的 bool 陣列：集合裡若有 x 這個元素，就讓 array[x] 這個位置為 true ，否則為 false 。  

它的壞處就是數值有界限、受陣列大小影響。但是，以這種資料結構，做聯集、交集、差集之類的運算，則會比較快，時間複雜度為 O( 陣列大小 ) 。

- Set 資料結構 : Hash Table  
int hash( 一筆資料 ) {return 一個數值 ;}  

一筆資料重新表示成一個數值。該數值稱作雜湊值。  

資料庫的觀點：資料進行索引，以利管理。密碼學的觀點：資料進行編碼，以求隱蔽。  

理想情況是相同資料有著相同雜湊值、相異資料有著相異雜湊值，如此就能直接使用雜湊值來分辨資料。  

可以直接使用 STL 的 hash 。  
- Insertion Sort  
[Insertion Sort](https://github.com/jimmyseto168/jimmyseto/tree/master/Leetcode/147_insertion%20Sort_06170218) 
[小殘的程式光廊](https://emn178.pixnet.net/blog/post/93791164)  
插入排序法(Insertion Sort)是排序演算法的一種，他是一種簡單容易理解的排序演算法，其概念是利用另一個數列來存放已排序部分，逐一取出未排序數列中元素，從已排序數列由後往前找到適當的位置插入。運算流程如下：

從未排序數列取出一元素。
由後往前和已排序數列元素比較，直到遇到不大於自己的元素並插入此元素之後；若都沒有則插入在最前面。
重複以上動作直到未排序數列全部處理完成。  
- Quick-Sort:  
跟前一個資料比較，比自己大就再往前比，比自己小就可以插入，平均時間複雜度高，且不穩定  
[Quick-Sort](https://github.com/jimmyseto168/jimmyseto/tree/master/HW1)   
[Comparison Sort: Quick Sort(快速排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html)
### week 5  
雙十節。  <br>
### week 6  

- Heap Sort 
[HW2](https://github.com/jimmyseto168/jimmyseto/tree/master/HW2)  

[Comparison Sort: Heap Sort(堆積排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)   

- Merge Sort  
[HW2](https://github.com/jimmyseto168/jimmyseto/tree/master/HW2)
[Merge Sort](http://notepad.yehyeh.net/Content/Algorithm/Sort/Merge/Merge.php)
[Comparison Sort:merge sort](http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)
### week 8  

- Binary Tree 
最廣義的樹(Tree)對於樹上的node之child數目沒有限制，因此，每個node可以有多個child。  
若限制node只能有兩個child，等價於「樹上的每一個node之degree皆為2」，此即稱為Binary Tree(二元樹)
[binary tree](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)
[Binary Search tree](https://github.com/jimmyseto168/jimmyseto/blob/master/HW3)  
### week 9  
- Binary Search Tree  
之前class TreeNode包含了指向child的pointer、指向parent的pointer，以及一個char data來儲存字母。  
那麼要使用`chardata`進行「比大小」就必須而外自行定義規則，例如：「照字母順序排序，字母越前面值越大；  
若第一個字相同，則依序往下比較；若姓名中所有字母之順序皆相同則...」等等，已經有點麻煩，更別說是`node ` 
所攜帶的資料項目比`chardata`更複雜的情況，也許是一個姓名、一組帳戶資料、一本照片集、一組科學數據等等。
[Binary Search tree : intro](http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html)
[Binary Search tree](https://github.com/jimmyseto168/jimmyseto/blob/master/HW3) 
### week 10  
- Red Black Tree  
### week 11  
- Hash Table   
  - Hash Table:把資料放到Table裡面，並根據(Key)值直接查詢在內存存儲位置的資料結構。   
通過計算一個(key)值的函數，將所需查詢的數據映射到表中一個位置來查詢記錄，這加快了查找速度。  
  - 如何計算:  
利用ＭＤ5這個密碼雜湊函式，將資料（如一段文字）運算變為另一固定長度值  
1. 先寫一個把字串轉成md5格式的function  
2. add: 設a = (key)值轉化過後除以我們index(a)的個數(＝5)所以必定為0,1,2,3,4   
   假設加入1裡面，則把新加入的值(new_node)加到data裡面   
3. remove: 如果node值==key，則現在這個節點被下個節點取代   
4. contains: node一直往下找，直到找到key為止return true,沒找到則return False   
[HW4](https://github.com/jimmyseto168/jimmyseto/tree/master/HW4)
### week 12  
- Breadth-First Search  
Breadth-First-Search是從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置，無論如何都要遍  
歷完畢整張地圖才終止。按照就 近原則進行，距離原點相同的節點的訪問順序是相近的。  
當在無權地圖中尋找最短的路徑的時候，不用出現大小比較  
因為尋找自起點開始，只要找到了某一個點，他一定是目前相同步數中距離起點最近的  
因為每一步都是從同一個節點開始 ，按照節點出現的順序（queue記錄）去尋找的，所以先出現的點，一定比後出現的點距離原點近。  
BFS使用　’queue‘　來進行儲存未被檢測的節點，利用佇列的先進先出的特點來按照寬度訪問查詢等待計算的節點。  
BFS　實現路徑記錄，可以每一次儲存遍歷節點的父節點，這樣的話，在輸出的時候就可以遍歷回溯到上一節點，從而實現路徑輸出。  
[https://www.itread01.com/content/1541297601.html](https://www.itread01.com/content/1541297601.html)  
[https://codertw.com/程式語言/102866/#outline__1](https://codertw.com/程式語言/102866/#outline__1)  
[https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)  
[https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)  
### week 13. 
- Depth-First Search  
Depth-First-Search是從根節點開始，逐個訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個 回溯前驅節點。  
DFS 使用stack儲存未被檢測的節點，節點按照深度優先的次序被訪問並依次被壓入stack中，並以相反的次序出stack進行新的檢測。  
DFS使用 stack 這一種資料結構來儲存未訪問的節點。  
[https://www.itread01.com/content/1541297601.html](https://www.itread01.com/content/1541297601.html)  
[https://codertw.com/程式語言/102866/#outline__1](https://codertw.com/程式語言/102866/#outline__1)  
[https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)  
[https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)
### week 14  
- Minimum Spanning Tree - Kruskal  
Kruskal演算法是一種用來尋找最小生成樹的演算法，目的是找出可連結所有點且具最小權重總和的樹   
步驟1–>把所有的邊依照權重從小排到大   
步驟二–>由最小權重的邊開始，在維持不導致環情況發生的條件下，把邊加入最小生成樹的集合內。   
直到所有邊都被檢查過停止。  

參考資料：[https://www.youtube.com/watch?v=uRfSsu4zYW0](https://www.youtube.com/watch?v=uRfSsu4zYW0)  
參考資料：[https://www.youtube.com/watch?v=9wV1VxlfBlI](https://www.youtube.com/watch?v=9wV1VxlfBlI)  
參考資料：[https://www.youtube.com/watch?v=NLp9C7AvJhk](https://www.youtube.com/watch?v=NLp9C7AvJhk)  
參考資料：[https://www.itread01.com/content/1548612012.html](https://www.itread01.com/content/1548612012.html)  
參考資料：[http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html](http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html)  

### week 15  
- Shortest Path - Dijkstra  
其基本原理是：每次新擴展一個距離最短的點，更新與其相鄰的點的距離。當所有邊權都為正時，由於不會存在一個距離更短的沒擴展過的點，  
所以這個點的距離永遠不會再被改變，因而保證了演算法的正確性。不過根據這個原理，  
用Dijkstra求最短路的圖不能有負權邊，因為擴展到負權邊的時候會產生更短的距離，有可能就破壞了已經  
更新的點距離不會改變的性質。  
Dijkstra演算法的輸入包含了一個有權重的有向圖G，以及G中的一個來源頂點S。 我們以V表示G中所有頂點的集合。    
每一個圖中的邊，都是兩個頂點所形成的有序元素對。(u,v)表示從頂點u到v有路徑相連。 我們以E所有邊的集合，而邊的權重則由權重函數w: E → [0, ∞]定義。    
因此，w(u,v)就是從頂點u到頂點v的非負花費值(cost)。 邊的花費可以想像成兩個頂點之間的距離。任兩點間路徑的花費值，就是該路徑上所有邊的花費值總和。     
已知有V中有頂點s及t，Dijkstra演算法可以找到s到t的最低花費路徑(i.e. 最短路徑)。 這個演算法也可以在一個圖中，    
找到從一個頂點s到任何其他頂點的最短路徑。   


### week 16

Overview
### week 17

Final

### week 18

放假
回家投票~~~

## 課堂作業

HW1: [Quick Sort](https://github.com/jimmyseto168/jimmyseto/tree/master/HW1)  <p>
HW2: [merge_sort](https://github.com/jimmyseto168/jimmyseto/tree/master/HW2)  <p>
HW2: [heap_sort](https://github.com/jimmyseto168/jimmyseto/tree/master/HW2)  <p>
HW3: [BST](https://github.com/jimmyseto168/jimmyseto/tree/master/HW3)  <p>
HW4: [hash_table](https://github.com/jimmyseto168/jimmyseto/tree/master/HW4)  <p>
HW5: [DFS&BFS](https://github.com/jimmyseto168/jimmyseto/tree/master/HW5)  <p>
HW6: [Dijkstra & Kruskal](https://github.com/jimmyseto168/jimmyseto/tree/master/HW6)  <p>
 
 ## 自學
  * [R語言](https://github.com/jimmyseto168/jimmyseto/tree/master/jimmy's%20learning/R語言)
