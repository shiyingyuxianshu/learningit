import codecs
f = codecs.open('weather_info.txt', 'r','utf-8')



dict_weather = {}
for i in f:
	i = i.split(',')
	dict_weather[i[0]] = i[1].strip()

def weather_help():
	print("\t以下为相关操作说明；\n\t输入城市名，查询该城市的天气；\n\t输入 help，获取帮助文档；\n\t输入 history，获取查询记录；\n\t输入 quit，退出天气查询系统。")

print("输入 help 查询使用方法")
check_history = []
while True:
	user_input = input("请输入指令或您要查询的城市名：")
	if user_input == "help":
		weather_help()
	elif user_input == "history":
		for list_history in check_history:
			print(list_history,dict_weather[list_history])
	elif user_input in dict_weather:
		check_history.append(user_input)
		print(user_input,dict_weather[user_input])
	elif user_input == "quit":
		print("感谢使用，更多精彩内容欢迎关注我的博客！")
		f.close()
		exit()
	else:
		print("你所输入的指令或城市不存在,如需帮助请输入 help ！")