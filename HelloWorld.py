# num = 10
# print('Guess what I think?')
# answer = int(input())
# result = answer>num
# #注意这个地方的判断条件，大于小于符号要细细考虑
# print('too large?')
# print(result)
# result = answer<num
# print('too small?')
# print(result)
# result = answer==num
# print('equal?')
# print(result)
"""
thisislove = bool(input())
if thisislove:
    print('爱真的需要勇气！')
"""
# num = 10
# print('Guess what I think?')
# answer = int(input())
# if answer > num:
#     print('too large')
# if answer < num:
#     print('too small')
# if answer == num:
#     print('Bingo!')
# a = 1
# while a != 0 :
#     print('Please input')
#     a = int(input())  #注意循环语句的结构结束在哪，与其他语言相比较缺少了大括号作为结束，看清空格位置
# print('Over！')

# num = 10
# print('Guess what I think?')
# result = True
# while result :  #这个地方的语句其实可以直接用个判断语句，例如“result == False”当然此时后面的result的值也需要做相应改变
#     answer = int(input()) #每次都需要来输入进行判断所以必须在循环语句内部
#     if answer > num:
#         print('too large')
#     if answer < num:
#         print('too small')
#     if answer == num:
#         result = False
# print('Bingo!')

# #随机数模块使用样例
# from random import randint  #随机数模块使用，该方式也为模块使用样例
# num = randint(1,50)
# print('Guess what I think?')
# result = True
# while result :  #这个地方的语句其实可以直接用个判断语句，例如“result == False”当然此时后面的result的值也需要做相应改变
#     answer = int(input()) #每次都需要来输入进行判断所以必须在循环语句内部
#     if answer > num:
#         print('too large')
#     if answer < num:
#         print('too small')
#     if answer == num:
#         result = False
# print('Bingo!')

# #高斯求等差数列样例
# sum = 0
# num = 1
# while num<=100 :
#     print("现在加到" + str(num))
#     sum += num
#     print('目前的和为：'+str(sum))
#     num += 1                       #python中无++符号
# print('最终的和为：'+str(sum))

# #逻辑运算
# a = True
# b = not a
# print(b)
# print(not b)
# print(a==b)
# print(a!=b)
# print(a and b)
# print(a or b)
# print(1<2 and b==True)
# for n in range(1,101):  #for循环是递归运算，range函数包括1，不包括101
#     print(n)

# #字符串的使用
# print('He said, \"I\'m yours!\"') #\转译字符，将字符串中本身引号与print函数中引号区别出来
# print('''He said, "I'm yours!"''')#'''  '''三个引号表示字符串中可以任意使用单双引号
# print('\\\_v_//')                   #\转译所需表达的字符串\\_v_//中的第一个\
# print('''
# Stay hungry,
# stay foolish.
#              -- Steve Jobs''')   #'''  '''可以直接表示需要换行的字符串
# print('Stay hungry,\nstay foolish.\n   -- Steve Jobs''')   #\n表示字符串输出换行操作
# print('''
#     *
#     ***
#     *****
#     ***
#     *''')


# #字符串格式化的使用
# num = 12
# print('My age is '+str(num))
# print('My age is %d'%num)   #%可以用来做格式化字符串，表示由%后面的值来替换掉
# print('Price is %f'%12.56)
# print('Price is %.2f'%12.56)#.2f表示取两位小数
# name = 'Crossin'
# print('%s is my name.'%name)

#随机数模块使用样例，增加个提示语句
# from random import randint  #随机数模块使用，该方式也为模块使用样例
# num = randint(1,50)
# print('Guess what I think?')
# result = True
# while result :  #这个地方的语句其实可以直接用个判断语句，例如“result == False”当然此时后面的result的值也需要做相应改变，即为一个标识符
#     answer = int(input()) #每次都需要来输入进行判断所以必须在循环语句内部
#     if answer > num:
#         print('%d is too large'%answer)
#     if answer < num:
#         print('%d is too small'%answer)
#     if answer == num:
#         result = False
# print('Bingo! %d is the right answer!'%answer)

#循环的嵌套
# for i in range(0,5):
#     print('*',end='') #end参数表示不换行输出，显示结果如图‘*****’
# for i in range(0,5):
#     print('\n*****\n') #\n表示换行输出

# #输出梯形图
# for i in range(1,6):        # *
#     for j in range(0,i) :   # **       （最主要的即为分析出第二个循环中的范围阈值）
#         print('*',end='')   # ***
#     #print('\n')             # ****    (每行行内内容不换行，跳出后要换行，该句也可以为print()这个我猜应该是空了一行)
#     print()                  # *****
# for i in range(0,5):        # *****
#     for j in range(0,5-i):  # ****
#         print("*",end='')   # ***
#     print()                  # **
#     #print('\n')             # *
#
# print('我是第一行！')
# print('我是第二行！')
# print()                      #试验后应该为空一行
# print('我是第四行！')
#
# print("%s's score is %d"%('Mike',89))  #多个字符串需要替换时，可以使用元组（，）来表示，但是必须保证数量与类型匹配
#
# print(bool(-123))
# print(bool(0))
# print(bool('abc'))
# print(bool('False'))
# print(bool(''))
#
# #函数的简单使用
# def sayhello():
#     print('Please input your name!')
#     n = input()
#     print(n +' says hello!')
# sayhello()

#函数的使用为了修改小程序，精简程序，重复使用函数体
# def isEqual(num1,num2):
#     if(num1>num2):
#         print(str(num1)+" is too large!")
#         return False                             #return表示了函数的结束语句，其后面的值为函数体的返回值
#     if (num1 < num2):
#         print(str(num1) + " is too small!")
#         return False                             #该标识符可表示为获取到所想要的即为True，否则即为False
#     if (num1 == num2):
#         print(str(num1) + " is right answer!")
#         return True

##使用if...elif...else语句改写的函数
# def isEqual(num1,num2):
#     if(num1>num2):                                 #if...elif ...else 多个判断语句可以组合，elif可以有多个，但是else只有一个且只能放在最后
#         print(str(num1) + " is too large!")
#         return False
#     elif(num1<num2):                              #if后面的为真执行其后，否则执行elif，其后为真执行其内部语句，否则继续执行else语句
#         print(str(num1) + " is too small!")
#         return False
#     else:
#         print(str(num1) + " is right answer!")
#         return True
#
#
# from random import randint
# ask = randint(1,50)
# print("Guess what I think?")
# result = False
# while result==False:           #当表示符为false时候才能继续循环直到获取到True标识符
#     answer = int(input())
#     result = isEqual(answer,ask)
# print('You are smart!')


# #多个if语句的嵌套使用
# print('Please input x')
# x=int(input())
# print('Please input y')
# y=int(input())
# if(y>0):
#     if(x>0):
#         print('该点坐标为（%d，%d），其位于第一象限！'%(x,y))
#     elif(x<0):
#         print('该点坐标为（%d，%d），其位于第二象限！'%(x,y))
#     else:
#         print('该点坐标为（%d，%d），其位于Y轴上半轴！' % (x, y)) #划分类型进行判断时要统一多考虑下，不要重复缺失
# elif(y<0):
#     if(x<0):
#         print('该点坐标为（%d，%d），其位于第三象限！'%(x,y))
#     elif(x>0):
#         print('该点坐标为（%d，%d），其位于第四象限！'%(x,y))
#     else:
#         print('该点坐标为（%d，%d），其位于Y轴下半轴！' % (x, y))
# elif(y==0):
#     if(x<0):
#         print('该点坐标为（%d，%d），其位于X轴左半轴！' % (x, y))
#     elif(x>0):
#         print('该点坐标为（%d，%d），其位于X轴右半轴！' % (x, y))
#     else:
#         print('该点坐标为（%d，%d），其位于坐标原点！' % (x, y))
#
#
# #list列表类型，表示处理一组有序项目的数据结构
# I = [365,'HelloWorld!',0.56,True,False]    #list数据结构定义方式为[]，该内部可以混有各类型数据结构
# print('List列表内容为：',I)
# print('List中的第一项值为：'+str(I[0]))#list结构中取某个值格式为List[i]，i从0开始计数
# I[1] = 'HelloWorld!你好！'            #list结构中修改某项的值，直接赋值给该项即可，此时list内容即发生改变
# I.append(1024)                          #list中append方法给list最后增加一项，该方法无返回值，但会改变list结构
# print('List列表内容为：',I)
# del I[3]                               #删除list中某个项目
# print('List列表内容为：',I)
# print('List中的最后一项值为：'+str(I[-1]))#list结构中取某个值格式为List[i]，i从0开始计数，也可以为负数，-1表示最后一项，-3表示倒数第三项
# print('List中的倒数第三项值为：'+str(I[-3]))
# L = I[1:3]                                #list结构中的切片，即为以[]为操作符，里面包含一对数字，中间以:隔开，
# print('L列表内容为：',L)                 # 冒号前的数表示开始位置，冒号后的数表示结束位置，包含开头不含结尾，仍然是从0开始计数
# M = I[:4]                                 #冒号前不指定数字，表示从0开始
# print('M列表内容为：',M)
# N = I[2:]
# print('N列表内容为：',N)                  #冒号后未指定数字，表示一直到最后一个元素
# O = I[:]                                   #冒号前后均无指定数字，表示list的一个拷贝
# print('O列表内容为：',O)
# for i in I:
#     print(i)
# print('Over!')

# #点球小游戏，即为球员以“左中右”三个方向射门，守门员也以“左中右”三个方向守门，方向一致即为防守成功否则即为进球，
# # 在这里射门球员为主动方需提供射门方向，守门员根据自己判断完成守门即为随机性
# Direction = ['Left', 'Center', 'Right']
# print('YOU kicked: ', Direction)
# person = input()
# from random import choice             #random的choice方法表示从一列有序项目中随机取到某项
# com = choice(Direction)
# if com != person:
#     print("Goal!Congratulation!")
# else:
#     print("God had abandoned you!")

#点球小游戏升级版，进行5轮比赛，每轮比赛分为你进攻与你守门，每进一球加1分即为进攻方才有机会得分
from random import choice
score_com = 0
score_you = 0
direction = ['Left','Center','Right']

#定义了一个函数表示方向不一致时候，进攻方得分，返回值为True表示得分，返回值为False表示未得分
def isScore(direction_off,direction_def):  #direction_off,direction_def分别表示攻门方向与守门方向
       if(direction_off != direction_def):
          return True
       else:
          return False

#该程序的主体部分，分为每轮你进攻与你防守，每轮转换角色后统计一次得分
for i in range(5):
    print('===Round %d ! You Kick!==='%(i+1))
    print('Choose one side to shoot:')
    print(direction)
    dir_you = input()
    dir_com = choice(direction)
    print('Computor saved :%s'%dir_com)
    if(isScore(dir_you,dir_com)):
        score_you +=1
        print("You Goal!")
    else:
        print('You had been saved!')
    print('Score: %d(you)-%d(com)'%(score_you,score_com))

    print('===Round %d ! Com Kick!==='%(i+1))
    print('Choose one side to save:')
    print(direction)
    dir_you = input()
    dir_com = choice(direction)
    print('Computor shot :%s' % dir_com)
    if (isScore(dir_com, dir_you)):
        score_com += 1
        print("Com Goal!")
    else:
        print('You had saved!')
    print('Score: %d(you)-%d(com)' % (score_you, score_com))
print('After 5 round, you got %d,com got %d! '%(score_you,score_com))
