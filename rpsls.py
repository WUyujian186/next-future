#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：邬雨建
日期：2019.11.14
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


    if name=='石头':
	    return(0)
    elif name=='剪刀':
	    return(4)
    elif name=='纸':
	    return(2)
    elif name=='蜥蜴':
	    return(3)
    elif name=='史波克':
	    return(1)
      #编写执行代码,代码完成后将pass删除


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果
    if number in range(0,4):
        if number ==0:
	        return('石头')
        elif number == 4:
	        return('剪刀')
        elif number == 2:
	        return('纸')
        elif number == 3:
	        return('蜥蜴')
        elif number == 1:
	        return('史波克')
    #编写执行代码,代码完成后将pass删除


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """

print("欢迎使用RPSLS游戏")
print("请输入您的选择：")
player_choice = (input())   # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
print("--------")    # 输出"-------- "进行分割
print("您的选择为：%s"%player_choice)
player_choice_number = name_to_number(player_choice)    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

comp_number = random.randrange(0,4)    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

comp_choic = number_to_name(comp_number)   # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

print("计算机的选择为：%s"%comp_choic)    # 在屏幕上显示计算机选择的随机对象

if player_choice_number-comp_number==-4 or player_choice_number-comp_number==-3 or player_choice_number-comp_number==1 or player_choice_number-comp_number==2:
	print("你赢了")
elif player_choice_number-comp_number==-2 or player_choice_number-comp_number==-1 or player_choice_number-comp_number==3 or player_choice_number-comp_number==4:
	print("机器赢了")
elif player_choice_number-comp_number==0:
	print("您和计算机出的一样呢")
else:
	print("Error: No Correct Name")    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    #根据以上提示编写执行代码，代码完成后删除掉pass


# ~ # 对程序进行测试
# ~ print("欢迎使用RPSLS游戏")
# ~ print("----------------")
# ~ print("请输入您的选择:")
# ~ choice_name=input()
# ~ rpsls(choice_name)




