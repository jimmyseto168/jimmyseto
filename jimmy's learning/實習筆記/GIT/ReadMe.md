### 什麼是Git?  
Git為分散式版本控制系統，是為了更好管理Linux內核而開發的。 <br>
Git可以把檔案的狀態作為更新歷史記錄保存起來。 <br>
因此可以把編輯過的檔案復原到以前的狀態，也可以顯示編輯過內容的差異。  
```
ps. 簡單來說就是組群共享檔案最好的方式啦
一個內容追蹤軟體，只在乎檔案內容，不在乎目錄檔案名稱
所以你可以修改新增人家最新上傳的檔案，但不會改到他的檔案 
```
- [x] 知道ＧＩＴ裏的四種物件
- [x] 什麼是SHA1值
- [x] 什麼是commit
- [ ] Commit的時候發生什麼事
- [ ] 什麼是分支
- [ ] 合併跟之時發生什麼事
- [ ] 東西進入git,要砍還不容易

#### 知道ＧＩＴ裡的四種物件
> blob (最底層)
>> 放跟檔案有關的東西  

> tree  （第三層）
>> 放跟目錄有關的東西  

> commit  （第二層）
>> 顧名思義就是放commit啦(commit id 就是放SHA1 Hash值)  

> tag  （最上層）
>> 放跟tag有關的東西  

#### 什麼是SHA1值
使用git hash-object指令會跑出來的那一長串(4135fc4add3332e25acabe1bd.......)由40個16進位字元組成
每個物件都有自己的SHA1值

參考資料： [猴子也能懂GIT](https://backlog.com/git-tutorial/tw/intro/intro1_3.html)   
[人生不能重來，但GIT可以](https://www.youtube.com/watch?v=LgTf7m5B0xA)  
**名詞解釋**  
1.hash值：一種資料結構，例如把 n 個數字儲存在 Hash Table 裡面，<br>那如果要判斷這個數字 A 是不是已經被存在 Hash Table 裡面，  
只要先把這個數字丟進 hash function，就可以直接知道 A 對應到 Hash Table 中哪一格，  
如果希望儲存的 data 可以被排序，那 Hash Table 就會不太好用
