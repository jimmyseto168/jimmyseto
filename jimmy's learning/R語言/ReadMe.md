想要做什麼？
- [ ] 文字雲
- [ ] 關聯分析(購物籃分析)
- [X]	抓股票數據
- [X] 	爬蟲
- [X]	爬蟲精簡版
- [X]	甘特圖ggplot  
- [X]	美觀版甘特圖	



[R基本](https://joe11051105.gitbooks.io/r_basic/content/)  
[R 筆記寫法](https://knowlab.wordpress.com/2016/12/05/%E4%BB%A5-r-markdown-%E8%BC%95%E9%AC%86%E7%B7%A8%E8%BC%AF%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E5%A0%B1%E5%91%8A%EF%BC%88%E4%B8%8A%EF%BC%89/)  
 
匯入csv檔時使用read.csv()，若檔案並非位於工作環境中，需命名所在位置，如下圖第2-3行指令。read.csv 會自動判斷以" , “隔開的純文字檔。stringsAsFactors = FALSE 時，R就不會將文字類型資料自動轉為factor (categorical data). 若欲匯入純文字檔且以空白隔開數值，則為Tab-delimited file, 可以使用 read.delim()
