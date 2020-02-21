``` R
install.packages("quantmod")
library(quantmod)  #股市套件
par(family='STKaiti')
search()
#台灣加權股價指數
#http://www.twse.com.tw/zh/
#"^TWII"
par(family="STKaiti")# 先設定可以plot出中文
getSymbols("^TWII",from= "2007-1-1")  #要的
summary(TWII)
chart_Series(TWII)
tail(TWII,1)  #資料往上數第一個（test）
head(TWII,1)  #第一個(test)

#證交所首頁—產品與服務—分類查詢結果
STK <- `1101.TW`
get(getSymbols("STK",from="2018-1-1"))
chartSeries(`STK`,theme = "white") #


dailyReturn <- dailyReturn(STK)
plot(dailyReturn)
plot(density.default(x = dailyReturn))
plot(density.default(x = dailyReturn),xlim= c(-0.05,0.05))#限定某區間
hist(dailyReturn,xlim = c(-0.05,0.05))
tail(dailyReturn,1)


hist(dailyReturn,xlim = c(-0.05,0.05))
abline(v = 0.01008832,col = "red",lwd = 6)#畫出一條直線(test)

last_dailyReturn <- as.numeric(tail(dailyReturn,1))
class(last_dailyReturn)
hist(dailyReturn,xlim= c(-0.05,0.05))
abline(v = last_dailyReturn,col = "red",lwd = 6)#畫出一條直線

hist(dailyReturn,xlim= c(-0.05,0.05),main = "1101股票日報酬率直方圖")

colnames(STK)
colnames(STK)[4]

hist(dailyReturn,xlim= c(-0.05,0.05),main = paste(colnames(STK)[4],"股票日報酬率直方圖"))
abline(v = last_dailyReturn,col = "red",lwd = 6) #畫出一條直線，是最新的報酬率

duration = "2019-01-01::2019-10-03" #設定期間
STK <- STK[duration]
chartSeries(STK,theme = "white")

dailyReturn(STK)
weeklyReturn(STK)
monthlyReturn(STK)
quarterlyReturn(STK)
annualReturn(STK)
yearlyReturn(STK)

summary(dailyReturn) #檢視日報酬率摘要
head(dailyReturn)

grep(-0.06,dailyReturn) #尋找日報酬率，特殊的
dailyReturn[241]
dailyReturn[242] #驗證下一天日報率為正或負

###
str(STK) #查看原始結構
STK1 <- as.matrix(STK) #轉成矩陣
str(STK1)
TimeCharacter <- rownames(STK1)  #將日期存成字元格式
TimeSeries = strptime(TimeCharacter,"%Y-%m-%d" #將timecharater時間設定為年/月/日
                      ,tz = Sys.timezone()) #台灣時區

closecharacter <- as.character(STK$STK.Close)
Price <- as.numeric(closecharacter)
View(Price)

PL_Chart <- data.frame(Price,TimeSeries#將數字向量及日期轉成data
                       ,stringsAsFactors = FALSE) #保留原始

View(PL_Chart)
```

<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/R/螢幕快照%202019-10-27%20下午8.54.41.png' weight=400 heught = 200>

``` R
#==========================================================
#install.packages("ggplot2")
install.packages("RColorBrewer")
library(ggplot2)
library(RColorBrewer)
search()
##畫出分線圖
#＋的意思是還要再加後面的東東
ggplot(PL_Chart,#data.frame的資料
       aes(x=TimeSeries,y=Price))+#x軸日期y軸價格
  geom_line()+#折線圖
  theme_bw()+#框格
  theme(panel.grid.major.x = element_blank()#刪除主要直網格
        ,panel.grid.minor.x = element_blank()#刪除次要直網格
        ,panel.grid.major.y = element_line(colour = "blue")
        ,panel.grid.minor.y = element_line(colour = "blue",linetype = "dashed"))+
  #上面在更改網格內的線
  xlab("time")+ylab("price")+
  theme(axis.title.x = element_text(face = "italic",colour = "darkred",size = 14))+ #調整X軸標題為斜體、深紅色，'大小為14
  theme(axis.title.y = element_text(angle = 90,face = "italic",colour = "darkred",size = 14))+ #angle在轉角度   
  ggtitle(paste(
    colnames(STK)[4],head(TimeCharacter,1),"至"
    ,tail(TimeCharacter,1),"每日走勢圖"))
theme(plot.title = element_text(face = "italic",colour = "red"
                                ,hjust = 0.5,size = 20))+ #hjust把標題置中
  theme(axis.text.x = element_text(face = "italic",size = 20))+ #改X軸的字
  theme(axis.text.y = element_text(face = "italic",size = 20))  #改Y軸的字
```
<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/R/螢幕快照%202019-10-27%20下午8.51.56.png' weight = 600 height = 600>
