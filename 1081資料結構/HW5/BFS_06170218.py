from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
     
    #s = start
    def BFS(self,s):
        #queue被發現的
        #seen被走訪過的
        queue = []
        queue.append(s)
        seen = []
        while (len(queue)>0) :
            #如果數組內有數，把第一個拿出來，再把相鄰節點放到數組
            s = queue.pop(0) 
            #被發現過後，就把數放到seen，表示看過
            seen.append(s)
            #所有節點叫做nodes
            nodes = self.graph[s]
            #一一探訪所有節點，並且把它加到queue裡面
            for w in nodes:
                #設定條件，如果被探訪過了就加入seen
                #沒被探訪過就加入queue裏，再跑迴圈
                if w not in seen and w not in queue:
                        queue.append(w)
        return seen
        
        
    def DFS(self,s):
        stack = []
        stack.append(s)
        seen = []
        
        while (len(stack)>0) :
            #用stack的模式，可以知道他是把最後一個拿出來，意思就是在具有多子節點的節點下，
            #先搜尋到某一條子路的最深處，再逐個回溯前驅節點
            s = stack.pop(-1)
            
            seen.append(s)
            nodes = self.graph[s]
            
            for w in nodes:
                #設定條件，如果被探訪過了就加入seen
                #沒被探訪過就加入queue裏，再跑迴圈
                if w not in seen and w not in stack:
                        stack.append(w)
        return seen
     
    #參考資料：[Python] BFS和DFS算法（第2讲）(https://www.youtube.com/watch?v=bD8RT0ub--0)    
