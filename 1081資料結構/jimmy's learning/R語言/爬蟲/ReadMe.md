### 先來個比較~麻煩~詳細的方法
[簡單方法按這邊唷](https://github.com/jimmyseto168/jimmyseto/tree/master/jimmy's%20learning/R語言/爬蟲精簡版)
```R
install.packages("httr") #取得網頁原始碼的工具
install.packages("jsonlite") #處理json格式文件的套件
install.packages("xml2")
install.packages("rvest") #HTML原始碼解析套件
install.packages("stringr")
install.packages("dplyr")
install.packages("ggplot2")



library(httr) #取得網頁原始碼的工具
library(jsonlite)
library(xml2)
library(rvest)
library(stringr)
library(dplyr)
library(ggplot2)
doc <- GET("https://rent.591.com.tw/index.php?module=search&action=rslist&is_new_list=1&type=1&searchtype=1®ion=0&listview=txt&firstRow=40&totalRows=54040")
content(doc,"text") #用content功能觀察網頁內容
df <- fromJSON(content(doc,"text"))

rent_data <- df[["main"]]

rent_html <- read_html(rent_data)
name <- html_nodes(rent_html, ".address")#找尋特定資料節點
name <- html_attr(name, "title") # 節點中需要的部分，title

#用一樣的步驟抓取縣市、行政區、租屋面積及資金
county <- html_nodes(rent_html, ".txt-sh-section")
county <- html_text(county)

town <- html_nodes(rent_html,".txt-sh-section")
town <- html_text(town)

area <- html_nodes(rent_html,".area")
area <- html_text(area)

price <- html_nodes(rent_html,".price .fc-org")
price <- html_text(price)

#把最後所有資料存到一個DataFrame格式檔案中
rent_df <- data.frame(
  county = county,
  town = town,
  name = name,
  area = area,
  price = price
)

View(rent_df)

#把爬好的資料存成ＣＳＶ
write.table(rent_df,file = "/Users/jimmy/rent_df.CSV",sep = ",",row.names = FALSE)

#讀入上面存好的 csv (test)
rent_df2 <- read.csv("/Users/jimmy/rent_df.CSV")
View(rent_df2)
```
