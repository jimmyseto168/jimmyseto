## BFS與DFS流程圖
### BFS
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW5.md/435300.jpg)

### DFS
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW5.md/435299.jpg)
## 程式碼學習歷程
### BFS
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW5.md/螢幕快照%202019-12-19%20下午3.06.00.png)

### DFS
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW5.md/螢幕快照%202019-12-20%20上午10.17.10.png)

### 成品
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW5.md/螢幕快照%202019-12-20%20上午10.17.16.png)
## BFS與DFS原理與比較
### BFS原理
- 定義

BFS (Breadth-First-Search) ——廣度優先搜尋,是從根節點開始，遍歷完畢整張圖，不考慮結果所在的位置，無論如何都要遍歷完畢整張地圖才終止。按照就 近原則進行，距離原點相同的節點的訪問順序是相近的。

當在無權地圖中尋找最短的路徑的時候，不用出現大小比較

因為尋找自起點開始，只要找到了某一個點，他一定是目前相同步數中距離起點最近的

因為每一步都是從同一個節點開始 ，按照節點出現的順序（queue記錄）去尋找的，所以先出現的點，一定比後出現的點距離原點近。

BFS使用　’queue‘　來進行儲存未被檢測的節點，利用佇列的先進先出的特點來按照寬度訪問查詢等待計算的節點。

BFS　實現路徑記錄，可以每一次儲存遍歷節點的父節點，這樣的話，在輸出的時候就可以遍歷回溯到上一節點，從而實現路徑輸出。

### DFS原理

- 定義

DFS (Depth-First-Search)——深度優先搜尋，是從根節點開始，逐個訪問每一條路徑，對於具有多子節點的節點而言，先搜尋到某一條子路的最深處，再逐個 回溯前驅節點。

DFS 使用stack儲存未被檢測的節點，節點按照深度優先的次序被訪問並依次被壓入stack中，並以相反的次序出stack進行新的檢測。

DFS使用 stack 這一種資料結構來儲存未訪問的節點。

### BFS與DFS比較

DFS使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用DFS來實現相關問題。反之，在求最短路問題時，DFS需要反覆經過同樣的狀態，所以此時使用BFS為好。  
  
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW5.md/螢幕快照%202019-12-19%20下午4.58.01.png)  
參考資料：[https://www.itread01.com/content/1541297601.html](https://www.itread01.com/content/1541297601.html)  
參考資料：[https://codertw.com/程式語言/102866/#outline__1](https://codertw.com/程式語言/102866/#outline__1)  
參考資料：[https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)  
參考資料：[https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)  
參考資料:老師ppt
