**前言：因為要markdown沒有表格功能，所以用ＨＴＭＬ格式來嵌入**

參考資料 [合併表格](https://www.itread01.com/content/1546072236.html)  
參考資料 [表格設計](https://blog.zfanw.com/markdown-and-table/)



#### 成品長這樣嘻嘻
<table>
    <tr>
        <td colspan = "8" align="center">我的時間分配 </td>
    </tr>
    <tr>
      <td>  </td>
      <td>禮拜一</td>
      <td>禮拜二</td>
      <td>禮拜三</td>
      <td>禮拜四</td>
      <td>禮拜五</td>
      <td>禮拜六</td>
      <td>禮拜日</td>
    </tr>
  <tr>
    <td>1</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td rowspan = "2">通俗文學<br>（通識）</td>
    <td rowspan = "12" colspan = "2">做報告<br> <br>寫作業<br> <br>準備問題</td>
    
   </tr>
  <tr>
    <td>2</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    </tr>
   <tr>
    <td>3</td>
    <td rowspan="2">心理學<br>（通識）</td>
    <td rowspan="2">資料結構<br>＆演算法（雙）</td>
    <td rowspan = "3">巨資分析</td>
    <td rowspan = "5">自學時間ya</td>
    <td rowspan = "2">資料結構＆<br>演算法</td>

   </tr>
  <tr>
    <td>4</td>
    </tr>
  <tr>
    <td>E</td>
    <td></td>
    <td rowspan = "3">視覺化解析</td>
    <td></td>
    </tr>
  <tr>
    <td>5</td>
    <td></td>
    <td></td>
    <td rowspan = "5">自學時間</td>
    </tr>
  <tr>
    <td>6</td>
    <td></td>
    <td rowspan = "6">中研院實習<br>(希望啦><)</td>
    </tr>
   <tr>
    <td>7</td>
    <td rowspan = "3">產品設計<br>心理學</td>
    <td rowspan = "3">自學時間</td>
    <td rowspan = "3">電子化企業</td>
    </tr>
   <tr>
    <td>8</td>
    </tr>
   <tr>
    <td>9</td>
    </tr>
   <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td rowspan = "2">金融應用程<br>式設計</td>
    <td></td>
    </tr>
   <tr>
    <td>B</td>    
    <td></td>
    <td></td>
    <td></td>
    </tr>

</table>


**技術總結：** 
 * width：控制 table 的寬度  
 * border：控制 table 邊框的粗細  
 * background：控制背景圖片  
 * colspan：控制儲存格橫跨幾個欄位  
 * rowspan：控制儲存格垂直跨幾個欄位. 

```html
程式碼
<table>
    <tr>
        <td colspan = "8" align="center">我的時間分配 </td>
    </tr>
    <tr>
      <td>  </td>
      <td>禮拜一</td>
      <td>禮拜二</td>
      <td>禮拜三</td>
      <td>禮拜四</td>
      <td>禮拜五</td>
      <td>禮拜六</td>
      <td>禮拜日</td>
    </tr>
  <tr>
    <td>1</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td rowspan = "2">通俗文學<br>（通識）</td>
    <td rowspan = "12" colspan = "2">做報告<br> <br>寫作業<br> <br>準備問題</td>
    
   </tr>
  <tr>
    <td>2</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    </tr>
   <tr>
    <td>3</td>
    <td rowspan="2">心理學<br>（通識）</td>
    <td rowspan="2">資料結構<br>＆演算法（雙）</td>
    <td rowspan = "3">巨資分析</td>
    <td rowspan = "5">自學時間ya</td>
    <td rowspan = "2">資料結構＆<br>演算法</td>

   </tr>
  <tr>
    <td>4</td>
    </tr>
  <tr>
    <td>E</td>
    <td></td>
    <td rowspan = "3">視覺化解析</td>
    <td></td>
    </tr>
  <tr>
    <td>5</td>
    <td></td>
    <td></td>
    <td rowspan = "5">自學時間</td>
    </tr>
  <tr>
    <td>6</td>
    <td></td>
    <td rowspan = "6">中研院實習<br>(希望啦><)</td>
    </tr>
   <tr>
    <td>7</td>
    <td rowspan = "3">產品設計<br>心理學</td>
    <td rowspan = "3">自學時間</td>
    <td rowspan = "3">電子化企業</td>
    </tr>
   <tr>
    <td>8</td>
    </tr>
   <tr>
    <td>9</td>
    </tr>
   <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td rowspan = "2">金融應用程<br>式設計</td>
    <td></td>
    </tr>
   <tr>
    <td>B</td>    
    <td></td>
    <td></td>
    <td></td>
    </tr>

</table>


```
