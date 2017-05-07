#coding：utf-8
#使程序可以接受中文的输入
#python3中已经在unicode做了改进，已经不需要在标注

"""
多行标注：

基础实现过程
$ python demo_1w_task.py
请输入指令或者您要查询的城市名称：北京
北京的天气状况为：晴
请输入指令或者您要查询的城市名称：贵港
北京的天气状况为：小雨
请输入指令或者您要查询的城市名称：help
		
		输入城市名，查询该城市的天气；
		输入 help，获取帮助文档；
		输入 history，获取查询历史；
		输入 quit，退出天气查询系统。
		
请输入指令或者您要查询的城市名称：history
北京 晴

贵港 小雨

请输入指令或者您要查询的城市名称：quit
$ 

"""
'''
def UserHelp():
	print ("""
		输入城市名，查询该城市的天气；
		输入 help，获取帮助文档；
		输入 history，获取查询历史；
		输入 quit，退出天气查询系统。
		""")
'''
print ("欢迎来到东濠天气预报！！！祝您天天好心情！")
#打印程序可以接受中文的输入

file = open("weather_info.txt","r")
#为变量file赋值，其值为“以只读方式开启weather_info.txt文件”

dict = {}
#开始制作字典，字典名为dict，
#从file变量中逐行读取数据
#首先，对每行的字符串使用strip（）命令，移除头尾的空格
#再使用split（）命令，以“，”为指定分隔符，对字符串进行切片，分割成列表
#之后，每行字符串中“，”之前的字符赋值为变量key，“，”之后的字符赋值为变量value
#使用字典读取变量key，即可调用同行的变量value
for line in file:
	City, CityCome = line.strip().split(',')
	dict[City] = (CityCome)


while True:
	UserInput = input ("请输入指令或者您要查询的城市名称：")

	file1 = open('history.txt','a')
#将变量file赋值为open函数，指定打开文件history.txt并追加内容
	file1.write(UserInput)
#将变量UserInput写入变量file
	file1.close
#关闭变量file所映射的文档

	UserHistory = open('history.txt')
#将变量record赋值为open函数，指定打开文件history.txt

	if UserInput == "quit":
		exit()

	elif UserInput == "help":
		print ("""
		输入城市名，查询该城市的天气；
		输入 help，获取帮助文档；
		输入 history，获取查询历史；
		输入 quit，退出天气查询系统。
		""")
		'''
		代替方案：UserHelp()
		'''

	elif UserInput == "history":
		print (UserHistory.read())
		UserHistory.close()

	elif UserInput in dict:
		print (dict.get(UserInput))

	else:
		print ("指令输入错误或者东濠这边探测不到外太空天气情况，争取完善，可重新输入")
