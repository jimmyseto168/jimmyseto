# BST
### 新增(insert):
設一個root
兩種方案1.== None return root, 2.如果大於等於要增加的值時，則在root左邊新增一個node，反之則右
裡面寫一個遞迴：如果發現子節點已經存在，則root = 子節點->加在子節點底下

### 查詢(search):
查詢到的話，return他的位置，查詢不到就return not found

### 刪除(delete):
寫一個children_count，計算子節點數量，都有不同的用處
0個：直接刪除
1個右邊：刪除節點，補右邊
1個左邊：刪除節點，補左邊
2個：刪除節點，並且把左邊補起來

### 修改(modify):
while search的到這個數：
則執行
delete要刪除的數字
insert要增加的數字
然後就可以把全部都刪除也全部都增加了

# 流程圖、學習歷程、原理

```py
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
        
    def insert(self, root, val):   
        #如果root為空值，則none
        if root is None:
            root = TreeNode(val)
            return root
        #分兩種情況，當root大於等於要增加的值時，則在root左邊新增一個node，反之則右
        #注意：如果發現子節點已經存在，則root = 子節點->加在子節點底下
        else:
            if root.val >= val:
                if root.left != None:
                    root.left = self.insert(root.left, val)                    
                else:
                    root.left = TreeNode(val)
                    return root.left
                
            elif root.val < val:
                if root.right != None:
                    root.right = self.insert(root.right, val)
                    
                else:
                    root.right = TreeNode(val)    
                    return root.right
```
流程圖：  
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3/insert.png)  
實測（最終）：  
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3/螢幕快照%202019-11-22%20下午9.07.21.png)  

```py
#查詢
#主要核心概念就是當target找到他的位子時，就傳送他的位置
#寫迴圈去跟root比大小，比較小就移下去，然後root也會跑下去再繼續比直到等於
    def search(self,root,target):
        if root is None:
            return None
        else:
            if root.val == target:
                return root
            else:
                if root.val > target:
                    if root.left is not None:
                        return self.search(root.left, target)
                    else:
                        return str(target) + " not found"
                elif root.val < target:   
                    if root.right is not None:
                        return self.search(root.right, target)
                    else:
                        return str(target) + " not found" 


```
流程圖：  
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3/search.png)  
實測：  
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3/螢幕快照%202019-11-22%20下午9.07.47.png)  
```py
    #計算子節點個數
    def children_count(self, node):
        a = 0
        if node.left:
            a += 1
        if node.right:
            a += 1
        return a
    
    # 刪除分三種規則
    #1.無子：可以直接刪掉 
    def delete(self, root,target):
        x = self.children_count(root)
        if root is None: 
            root = TreeNode(val)
            return root
        if target < root.val: 
            root.left = self.delete(root.left, target)  
        elif target > root.val: 
            root.right = self.delete(root.right, target) 
        else: 
            if x == 0:
                root  = None
        #1 child
            elif x == 1:
            #看子節點在左還是右  
            #root改成他的子節點，就可以移除了
                if root.left != None:
                    root = root.left
                    root.left = None

                if root.right != None:
                    root = root.right
                    root.right = None
        #2 child
        #我自己定義是左邊移上來
            else:
                root = root.left
                root.left = None
           
```
![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3/delete.png)  

![](https://github.com/jimmyseto168/jimmyseto/blob/master/image/HW3/螢幕快照%202019-11-22%20下午9.08.21.png)  
學習歷程  
參考了很多網站，學習歷程大概多到爆炸了吧  
但是最後寫不太出來，所以就東拿一點西拿一點  
參考資料： [Data Structures in Python: Stack -- The Stack Data Structure](https://www.youtube.com/watch?v=lVFnq4zbs-g&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV)  
[Binary Search Tree (BST): Deletion Function](https://www.youtube.com/watch?v=Zaf8EOVa72I&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7&index=6)  
[資料結構 - 二元搜索樹(Binary Search Tree)](https://emn178.pixnet.net/blog/post/94574434)  
[Python - Tree Traversal Algorithms](https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm)  
