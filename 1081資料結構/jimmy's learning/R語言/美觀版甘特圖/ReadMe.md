**成果**
<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/R/螢幕快照%202019-10-27%20下午8.50.33.png' weight = 800 height = 800>


**獻上程式碼**
``` R
#ggplot2 美觀版甘特圖
install.packages("showtext")
install.packages("grid")
install.packages("scales")
install.packages("Cairo")
par(family='STKaiti')

library("lubridate")
library("ggplot2")
library("ggmap")
#library("showtext")
library("grid")
library("scales")
#library("Cairo")

search()
Item1 <- c("1證交所參訪籌備\n(交易所聽簡報)"    #文字集合
           ,"2股票報酬直方圖籌備\n (自動化報酬率檢視)"
           ,"3股票價格走勢圖籌備\n(自動化呈現ＤＩＹ圖表)"
           ,"4股市計畫甘特圖\n(投資策略ＤＩＹ開發)")  #\n是自動換行

Planned_Start_Date <- c("2019/09/01","2019/09/30","2019/10/7","2019/10/17")
Planned_Finish_Date <- c("2019/09/26","2019/10/03","2019/10/17","2019/10/31")

Actual_Start_Date <- c("2019/09/01","2019/09/30","2019/10/7","2019/10/17")
Actual_Finish_Date <- c("2019/09/26","2019/10/03","2019/10/17","2019/10/31")

mydata <- data.frame(Item1
                     ,Planned_Start_Date
                     ,Planned_Finish_Date
                     ,Actual_Start_Date
                     ,Actual_Finish_Date
                     ,stringsAsFactors = FALSE
                     )

str(mydata) #檢查格式知道他目前是字元格式chr，要改成日期格式

mydata$Planned_Start_Date <- ymd(mydata$Planned_Start_Date)  #設定為日期格式
mydata$Planned_Finish_Date <- ymd(mydata$Planned_Finish_Date)
mydata$Actual_Start_Date <- ymd(mydata$Actual_Start_Date)
mydata$Actual_Finish_Date <- ymd(mydata$Actual_Finish_Date)

---------------------------------------------------------
datebreaks <- seq(as.Date("2019-09-01"),as.Date("2019-10-31"),by = "1 days")  
#一天一天  日其格式相關功能
time <- as.Date("2019-10-24")
---------------------------------------------------------

dev.new()
ggplot(mydata)+
  theme(text=element_text(family="STKaiti"))+    #原来的图形对象
  geom_linerange(data = mydata,aes(x = Item1 #進度的項目
                                   ,ymin = Planned_Start_Date #預測的起始日
                                   ,ymax = Planned_Finish_Date) #預測的結束日
                                   ,size = 10 ,color = "#BFBFBF" , alpha = 0.8)+
                                     #alpha = 透明度
  geom_linerange(data = mydata,aes(x = Item1 #進度的項目
                                  ,ymin = Planned_Start_Date #預測的起始日
                                  ,ymax = Planned_Finish_Date) #預測的結束日
                                  ,size = 7 ,color = "#085264" , alpha = 0.8)+
  scale_x_discrete(limits = sort(Item1,decreasing = F))+ #流程項目降階牌
  scale_y_date(position = "top") + #y軸排序方式 top bottom right
  coord_flip() + #縱衡轉換
  ggtitle(paste("股票投資策略進度圖"
                ,mydata$Planned_Start_Date[1]
                ,"to"
                ,mydata$Planned_Finish_Date[4]))+ 
  theme(
    plot.title = element_text(face = "italic",colour = "red",hjust = 0.5,size = 20),
                              #hjust0.5置中
    axis.title = element_blank(), #x軸標題取消
    axis.ticks.y = element_blank(), #y軸刻度取消
    panel.grid.major.y = element_line(color = "#FFB666",linetype = 5),#
    panel.background = element_rect(fill = "white"), #背景白色
    axis.text = element_text(colour = "black",size = 10,face= "italic"),
    axis.line.x = element_line() #x軸畫直線
    )
  
  ```
  
  
