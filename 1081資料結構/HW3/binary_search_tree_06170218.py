class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
class Solution(object):
    
    def insert(self, root, val):    
        if root is None:
            root = TreeNode(val)
            return root
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
#查詢
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
    def children_count(self, node):
        a = 0
        if node.left:
            a += 1
        if node.right:
            a += 1
        return a
#刪除     
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
                if root.left != None:
                    root = root.left
                    root.left = None

                if root.right != None:
                    root = root.right
                    root.right = None
            else:
                root = root.left
                root.left = None
                

        
