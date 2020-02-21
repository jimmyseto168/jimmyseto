常常看到有個檔案叫做__init.py～～  
其實他就是讓Python的編譯器知道資料夾內有函式庫的內容，  
若是沒有這檔案編譯器就不會尋訪這資料夾，而讀者就無法使用Class了  
  
```py
if __name__ == '__main__ :'  
```
上面這段程式碼相信各位新手老手一定都有看過，解釋之前需要有一個觀念就是，  
當你的`py`程式要外包給其他人用，那電腦在讀取時是會從頭開始讀的。  
但通常其他人只需要他的其中一個`function` ，為了解決這個問題. 
__name__ == '__main__' 被創造出來，__name是python內建、隱含的變數  
其意義是「模組名稱」。如果該檔案是被引用，其值會是模組名稱；  
但若該檔案是(透過命令列)直接執行，其值會是 __main__  
若是由其他程序來import時__name__則會是`他的.py`的路徑
<img src = "https://github.com/jimmyseto168/jimmyseto/blob/master/image/Python/nama%20%3D%20main.png" height = 200 weight = 100>. 


資料來源：[__name__ == '__main__'是什麼？](http://blog.castman.net/教學/2018/01/27/python-name-main.html). 
