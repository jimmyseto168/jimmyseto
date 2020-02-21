
``` R
install.packages("gapminder")
library(httr)
library(jsonlite)
library(xml2)
library(rvest)
library(stringr)
library(dplyr)
library(ggplot2)
library(magrittr)
library(gapminder)
read_html("https://udn.com/news/breaknews/1/0#breaknews")
doc <- read_html("https://udn.com/news/breaknews/1/0#breaknews")

doc %>% html_nodes(".dt")
date <- doc %>% html_nodes(".dt") %>% html_text()
#html_nodes找尋特定資料節點
#html_text結點中需要的部分

doc %>% html_nodes(".view")
watchTimes<- doc %>% html_nodes(".view") %>% html_text()

as.numeric(watchTimes)
str(watchTimes)
watchTimes = as.numeric(watchTimes)
str(watchTimes)

work <- data.frame(
  date = date,
  watchTimes = watchTimes
)
View(work)
#-------#
p <- ggplot(data=work, aes(x = date, y = watchTimes)) +  geom_bar(stat="identity")
p
```
