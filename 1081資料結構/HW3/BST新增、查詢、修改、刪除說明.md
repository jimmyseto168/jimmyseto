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
