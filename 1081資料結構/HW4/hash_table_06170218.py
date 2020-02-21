from Crypto.Hash import MD5



class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity
     
    
    #把字串以UTF-8形式轉成10進位編碼
    def MD5encode(self,key):
        h = MD5.new()
        h.update(key.encode('UTF-8'))
        x = int(h.hexdigest(),16)
        return x
        
    #新增
    def add(self, key: int) -> None:
        #10進位編碼再判斷餘數
        a = self.MD5encode(key) % self.capacity
        node = self.data[a]

        while node != None:
            #直到node == None，則加入要加入的數
            if node.val  == key:
                return
            node = node.next
        new_node = ListNode(key)
        
        new_node.next = self.data[a]
        self.data[a] = new_node
    #移除：
    def remove(self, key: int) -> None:
        a = self.MD5encode(key) % self.capacity
        node = self.data[a]
        b = None
        while node :
            #如果node值==key，則現在這個節點被下個節點取代
            if node != None and node.val == key:
                self.data[a] = node.next
                return
            b = node
            node = node.next     

            
    #存在        
    def contains(self, key):
        
        a = self.MD5encode(key) % self.capacity
        node = self.data[a]
        #node一直往下找，直到找到key為止return true
        while node:
            if node.val == key:
                return True
            node = node.next
        return False


