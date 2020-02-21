# Dijkstra與Kruskal流程圖
## Dijkstra
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW6/443369.jpg)
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW6/443370_1.jpg)
## Kruskal
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW6/443371.jpg)
# 程式碼學習歷程
原理我都會了，但寫成程式碼實在太難了，超乎我現在的上限，所以我只有寫基本的，其他都寫pass
以下是我的學習歷程

```py =
class Graph():
    
    def __init(self,vertices):
        self.V = vertices
        self.graph = []
        # Initialize the adjacency matrix with zeros
        self.graph_matrix = [[0 for column in range(vertices)]
                             for row in range(vertices)]
    def addEdge(self,u,v,w):
        pass
    def Dijkstra(self,s):
        pass
    def Kruskal(self):
        pass


```
# Dijkstra、Kruskal原理說明

## Dijkstra

其基本原理是：每次新擴展一個距離最短的點，更新與其相鄰的點的距離。當所有邊權都為正時，由於不會存在一個距離更短的沒擴展過的點，

所以這個點的距離永遠不會再被改變，因而保證了演算法的正確性。不過根據這個原理，

用Dijkstra求最短路的圖不能有負權邊，因為擴展到負權邊的時候會產生更短的距離，有可能就破壞了已經

更新的點距離不會改變的性質。

Dijkstra演算法的輸入包含了一個有權重的有向圖G，以及G中的一個來源頂點S。 我們以V表示G中所有頂點的集合。  

每一個圖中的邊，都是兩個頂點所形成的有序元素對。(u,v)表示從頂點u到v有路徑相連。 我們以E所有邊的集合，而邊的權重則由權重函數w: E → [0, ∞]定義。  

因此，w(u,v)就是從頂點u到頂點v的非負花費值(cost)。 邊的花費可以想像成兩個頂點之間的距離。任兩點間路徑的花費值，就是該路徑上所有邊的花費值總和。   

已知有V中有頂點s及t，Dijkstra演算法可以找到s到t的最低花費路徑(i.e. 最短路徑)。 這個演算法也可以在一個圖中，  

找到從一個頂點s到任何其他頂點的最短路徑。  

![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW6/螢幕快照%202020-01-03%20下午8.21.39.png)如圖所示

## Kruskal
Kruskal演算法是一種用來尋找最小生成樹的演算法，目的是找出可連結所有點且具最小權重總和的樹  

步驟1–>把所有的邊依照權重從小排到大  
步驟二–>由最小權重的邊開始，在維持不導致環情況發生的條件下，把邊加入最小生成樹的集合內。  
直到所有邊都被檢查過停止。  
![](https://i.imgur.com/dXpIrlS.gif) 如圖所示  

參考資料：[https://www.youtube.com/watch?v=uRfSsu4zYW0](https://www.youtube.com/watch?v=uRfSsu4zYW0)  
參考資料：[https://www.youtube.com/watch?v=9wV1VxlfBlI](https://www.youtube.com/watch?v=9wV1VxlfBlI)  
參考資料：[https://www.youtube.com/watch?v=NLp9C7AvJhk](https://www.youtube.com/watch?v=NLp9C7AvJhk)  
參考資料：[https://www.itread01.com/content/1548612012.html](https://www.itread01.com/content/1548612012.html)  
參考資料：[http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html](http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html)  
