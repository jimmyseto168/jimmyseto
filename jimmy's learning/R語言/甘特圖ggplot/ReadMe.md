**成品：**
<img src = 'https://github.com/jimmyseto168/jimmyseto/blob/master/image/R/螢幕快照%202019-10-27%20下午8.45.33.png' weight = 800 height = 800>

**程式碼**
``` R
install.packages("plan")
library("plan")

g <- new("gantt")
g <- ganttAddTask(g,description = "coursework")#大項目
g <- ganttAddTask(g,description = "visual analysis",start = "2019-09-09",end="2020-01-06",done = 0)
g <- ganttAddTask(g,description = "data structure algorithm",start = "2019-09-09",end="2020-01-06",done = 0)
g <- ganttAddTask(g,description = "Optimization theory",start = "2019-09-10",end="2020-01-10",done = 0)
g <- ganttAddTask(g,description = "financial application",start = "2019-09-10",end="2020-01-07",done = 0)
g <- ganttAddTask(g,description = "manageruial math",start = "2019-09-11",end="2020-01-08",done = 0)
g <- ganttAddTask(g,description = "sport")
g <- ganttAddTask(g,description = "dance",start = "2019-11-24",end="2019-11-25",done = 0)
g <- ganttAddTask(g,description = "college high",start = "2019-12-30",end="2019-12-31",done = 0)
g <- ganttAddTask(g,description = "NorthTaiwanDance",start = "2019-12-28",end="2019-12-29",done = 0)
g <- ganttAddTask(g,description = "date")
g <- ganttAddTask(g,description = "Yangmingshan",start = "2019-03-29",end="2019-03-30",done = 0)
g <- ganttAddTask(g,description = "sleep",start = "2019-03-29",end="2023-01-06",done = 0)
g <- ganttAddTask(g,description = "cat coffee shop",start = "2019-09-13",end="2019-09-15",done = 0)
#par(family='STKaiti')
ifelse(is.na(g[["start"]]),2,1)
a <- ifelse(is.na(g[["start"]]),2,1)
dev.new()
plot(g,ylab=list(font=a),main="My Schedule")

```
