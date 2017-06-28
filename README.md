# 使用wxpy爬取需求信息发送微信

## 技术栈：

python3.6 + pip3 + wxpy + wechat_sender + urllib + bs4 +pymysql

## 下载 (运行`python3.6 `)
##### 如果安装报错，请用pip安装指定模块，对于的wxpy的学习，请github自行搜索

 	git clone https://github.com/Topthinking/wxPython.git
	
 	cd wxPython

 	python main.py
 	
## 2017年6月25日
```
初次提交,本地数据进行斗鱼主播的直播情况查询
```
## 2017年6月27日
```
1.使用pymysql来动态捕获查询数据
2.同时扩展了库与库之间的关系，待优化...
```
## 2017年6月28日
```
1.数据的增删改查
2.回复格式为 dy:[名称]:[房间号]:[别名] 即可完成添加或者修改，
例如回复: dy:yyf:58428:rua , 
结果就是更新rua别名，那么就可以回复rua获取房间号58428的直播情况
可以回复多个别名，他们以英文的逗号隔开，比如 dy:yyf:58428:rua,胖头鱼
```
## 说明

>  本项目主要学习Python爬虫，配合微信发送爬取信息，使得学习不会那么枯燥

>  如果觉得不错的话，您可以点右上角 "Star" 支持一下 谢谢！ ^_^

>  如有问题请直接在 Issues 中提，或者您发现问题并有非常好的解决方案，欢迎 PR 👍

### 扫描二维码，验证信息输入'top'
![](https://github.com/Topthinking/wxPython/blob/master/doc/top.jpg)

# 效果截图
<img src="https://github.com/Topthinking/wxPython/blob/master/doc/show.png" width="760" height="350"/> 

# 词汇截图
<img src="https://github.com/Topthinking/wxPython/blob/master/doc/word.png" width="760" height="350"/>