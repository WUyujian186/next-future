#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����꽨
���ڣ�2019.11.14
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    if name=='ʯͷ':
	    return(0)
    elif name=='����':
	    return(4)
    elif name=='ֽ':
	    return(2)
    elif name=='����':
	    return(3)
    elif name=='ʷ����':
	    return(1)
      #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    if number in range(0,4):
        if number ==0:
	        return('ʯͷ')
        elif number == 4:
	        return('����')
        elif number == 2:
	        return('ֽ')
        elif number == 3:
	        return('����')
        elif number == 1:
	        return('ʷ����')
    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """

print("��ӭʹ��RPSLS��Ϸ")
print("����������ѡ��")
player_choice = (input())   # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
print("--------")    # ���"-------- "���зָ�
print("����ѡ��Ϊ��%s"%player_choice)
player_choice_number = name_to_number(player_choice)    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

comp_number = random.randrange(0,4)    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

comp_choic = number_to_name(comp_number)   # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

print("�������ѡ��Ϊ��%s"%comp_choic)    # ����Ļ����ʾ�����ѡ����������

if player_choice_number-comp_number==-4 or player_choice_number-comp_number==-3 or player_choice_number-comp_number==1 or player_choice_number-comp_number==2:
	print("��Ӯ��")
elif player_choice_number-comp_number==-2 or player_choice_number-comp_number==-1 or player_choice_number-comp_number==3 or player_choice_number-comp_number==4:
	print("����Ӯ��")
elif player_choice_number-comp_number==0:
	print("���ͼ��������һ����")
else:
	print("Error: No Correct Name")    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# ~ # �Գ�����в���
# ~ print("��ӭʹ��RPSLS��Ϸ")
# ~ print("----------------")
# ~ print("����������ѡ��:")
# ~ choice_name=input()
# ~ rpsls(choice_name)




