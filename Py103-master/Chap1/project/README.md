

- Ch1 ：完成最小MVP

- 1. 功能实现：

  - 输入城市名，获取该城市的天气情况
  - 输入指令，获取帮助信息（一般使用Help）
  - 输入指令，获取历史查询信息（一般使用history）
  - 输入指令，推出程序

- 1. 最终实现结果：

  ```
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
  ```


- 1. 任务实现资源

     > [weather_info.txt](https://github.com/AIMinder/Py103/blob/master/Chap1/project/weather_info.txt)
     >
     > [yanzhiw](https://github.com/yanzhiw)
     >
     > [summerpenguin](https://github.com/summerpenguin)



## 任务计划

1. 分析任务

   1. 变量（++表示参考其他答案后补充的）

      - UserInput

        - UserInput = raw_input("请输入指令或者您要查询的城市名称：")

          > if UserInput == ？#用户输入的比较，1. 城市信息 2. 历史信息 3. 帮助文档 4.退出命令
          >
          > ​	if UserInput == "quit":
          >
          > ​		break:
          >
          > ​	elif UserInput == "help":
          >
          > ​		print  ("""
          >
          > ​		输入城市名，查询该城市的天气；
          > ​		输入 help，获取帮助文档；
          > ​		输入 history，获取查询历史；
          > ​		输入 quit，退出天气查询系统。		""")

      - file(++)—用于读取weather_info的内容

      - dict(++)用于根据weather内容建立字典，以便检索，其中split方法以“，”分割字符，

      - City变量表示需检索的城市

      - CityOutcome变量表示检索城市的天气情况

      - UserHistory用于呈现历史情况

      - UserHelp用于呈现帮助文档

   2. 流程：

      1. 存储信息（各城市天气资料）
      2. 对用户发出信息（查询历史，天气，帮助，还是退出，可用raw_input()来实现）
      3. 接受用户信息
      4. 根据用户信息进行检索
      5. 将检索信息返回给用户（检索的流程如何实现？）



反思：

1. 从变量、流程的角度分析代码实现过程
2. 先从quit操作和help操作
3.  一开始raw_input的思路，程序运行报错,后[参考同学代码](https://github.com/yanzhiw/Py103/blob/master/Chap1/project/weather_check.py)修改为input（）
4. if—else的思路出现问题，改为if--elif反而正确了
5. [参考同学代码](https://github.com/yanzhiw/Py103/blob/master/Chap1/project/weather_check.py)使用定义函数WeatherHelp的方法完成了help的呈现功能
6. 然后循环功能没有考虑到，代码只实现了一次,因此考虑使用while
7. 思考如何实现读取文件的功能，file()，该过程参考了[summerpenguin](https://github.com/summerpenguin) 的guithub文档，有很完整的注释，也是自己应该学习的优点！