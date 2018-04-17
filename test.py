'''
a,b,c=1,2,3
print(a,b,c)
'''

'''
a=int(input("a="))
if a>18:
    print("a>18")
else:
    print("a<=18")
'''
'''
age=int(input("你的年龄是："))
if age>=18:
    print("恭喜你成年了！")
else:
    diff=str(18-age)
    print("要年满18岁才成年，你还差"+diff+"岁！")
'''
'''
import datetime

today=datetime.date.today()
month=int(input("请问你是在哪一个月份出生的："))
day=int(input("请问你的出生日是几号："))
birthday=datetime.date(today.year,month,day)

if birthday<today:
    birthday=datetime.date(today.year+1,month,day)

diff=birthday-today
if diff.days==0:
    print("不会吧，今天是你的生日！")
else:
    print("哇，再过"+str(diff.days)+"天就是你的生日了！")

'''

'''
def factorial(number):  #迭代
    product=1
    for i in range(number):
        product=product*(i+1)
    return product


def factorial(number):   #递归
    if number<=1:
        return 1
    else:
        return number*factorial(number-1)

print(factorial(3))

def fibonacci(n):   #fibonacci数列
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

print(fibonacci(2))
'''
'''
import numpy as np
import matplotlib.pyplot as pt
x=np.arange(0,360)
y=np.sin(x * np.pi / 180.0)
pt.plot(x,y)
pt.xlim(0,360)
pt.ylim(-1.2,1.2)
pt.show()
'''
'''
import random

game_count=0;
all_counts=0;
while True:
    game_count+=1
    guess_counts=0
    answer=random.randint(0,99)
    while True:
        guess=int(input("请猜一个数字（0-99）："))
        guess_counts+=1
        if guess==answer:
            print("恭喜你，猜中了！")
            print("你总共猜了"+str(guess_counts)+"次！")
            all_counts.append(guess_counts)
            break;
        elif guess>answer:
            print("你猜的数字太大了！")
        else:
            print("你猜的数字太小了！")

    onemore=input("你还要再玩一次吗（Y/N）？")
    if onemore != 'Y' and onemore !='y':
        print("欢迎下次再来玩！")
        print("你的成绩如下：")
        print(all_counts)
        print("平均猜中次数"+str(sum(all_counts)/float(len(all_counts))))
        break;
'''
'''
a=38
b=5
print(a/b)
print(float(a/b))
print(float(a)/b)
'''
'''
age=int(input("请输入你的年龄："))
with_parent=input("和父母一起来的吗？（Y/N）")
if age>=18:
    print("可以看限制级电影")
elif age>=12:
    print("可以看辅导级电影")
elif (age>=6 and age<12) and (with_parent=='Y' or with_parent=='y'):
    print("可以看保护级电影")
else:
    print("只能看普通级电影")
'''
'''
#列表list
a_list=[1,3,5,7,9]
print(a_list)
print(a_list[0])

str_list=['p','y','t','h','o','n']
print(str_list)
print(str_list[0])

str_msg="I love python"   #split方法把字符串类型返回为列表
b_list=str_msg.split();
print(b_list)

c_list=list(str_msg)
print(c_list)

k1=['book',10]
k2=['campus',15]
k3=['cook',9]
k4=['python',26]
keywords=[k1,k2,k3,k4]
print(keywords)
print(keywords[2])
print(keywords[2][0])
print(keywords[2][1])

print("python" in k1)
print("python" in k4)
print("python" in keywords)
print(["python",26] in keywords)
print(keywords+k1+k2)

x=list(range(10))
print(x)
y=x[1:7]
print(y)
y=x[1:7:2]
print(y)

msg="Here is the test string"
lst=list(msg)
print(lst)
print(lst.index('e'))
print(lst.count('e'))

#append和extend的区别
lsta=[1,2,3,4]
extb=[5,5,5]
lsta.append(extb)
print(lsta)
lsta.extend(extb)
print(lsta)

#pop的操作
lst=[0,1,2,3,4,5]
lst.append(9)
lst.append('x')
print(lst)
lst.pop()
print(lst)
lst.pop(2)
print(lst)
'''
'''
#元组tuple
tp1=tuple(range(10))
print(tp1)
print(tp1[2])
'''
'''
#字典dict
keywords={}
keywords['book']=10
keywords['campus']=15
keywords['cook']=9
keywords['python']=26
print(keywords['python'])
print(keywords)

week={}
week['Monday']='星期一'
week['Tuesday']='星期二'
week['Wednesday']='星期三'
week['Thursday']='星期四'
week['Friday']='星期五'
week['Saturday']='星期六'
week['Sunday']='星期日'
print(week)
print(week['Friday'])
print(week.keys())
print(week.values())
'''
# 集合set
'''
a={}
print(type(a))
b={1,2,3,4,5}
print(type(b))
print(b)
c=set()
print(type(c))
d={'a':1,'b':2}
print(type(d))

a={1,2,3,4,5}
b={1,3,5,7,9}
print(a & b)
print(a | b)
print(a ^ b)
'''
'''
a={1,2,3}
b={1,2,3}
print(a==b)
print(a is b)

b=a
print(a==b)
print(a is b)

b=a.copy()
print(a==b)
print(a is b)
'''
'''
a={1,2,3}
b=a
print(a)
print(b)
b.add(4)
print(a)
print(b)
print(a is b)
'''
'''
a={1,2,3}
b=a.copy()
b.add(4)
print(a)
print(b)
print(a is b)
'''
'''
a=[1,2,3]
b=a
b.append(4)
print(a)
print(b)
print(a is b)

a='string 1'
b=a
print(a==b)
print(a is b)
b=b.upper()
print(a)
print(b)
'''
# format函数
'''
a=50
b=100
print('{}+{}={}'.format(a,b,a+b))

a=set(range(1,10))
print(a)
b=set(range(5,100,5))
print(b)

c=set(range(1,101))
print("1+2+...+100={}".format(sum(c)))
'''
# python自定义函数
'''
def add2number(a,b):
    return a+b
print(add2number(10,20))

def draw_bar(n,symbol="*"):
    for i in range(1,n+1):
        print(symbol,end="")  #在print后面加end=""或者是，是为了让print输出之后不要换行
    print()

draw_bar(5)
draw_bar(10,'$')

def proc(*args):
    for arg in args:
        print("arg:",arg)

proc(1,2,3)
proc(1,2)
proc("a","b")

def add2number(a,b):
    global d
    c=a+b
    d=a+b
    print("在函数中，(c={},d={})".format(c,d))
    return c

c=10
d=99
print("在调用函数前，(c={},d={})".format(c,d))
print("{}+{}={}".format(2,2,add2number(2+2)))
print("函数调用后，(c={},d={})".format(c,d))

x=range(1,10)
y=map(lambda i:i**3,x)
for i ,value in enumerate(y):
    print("{}^3={}".format(i,value))
'''
# import与自定义模块
'''
import re
fp=open("sample.txt","r")
article=fp.read()
new_article=re.sub("[^a-zA-Z\s]]","",article)
words=new_article.split()
word_counts={}
for word in words:
    if word.upper() in word_counts:
        word_counts[word.upper()]=word_counts[word.upper()]+1
    else:
        word_counts[word.upper()]=1

key_list=list(word_counts.keys())
key_list.sort()
for key in key_list:
    if word_counts[key]>1:
        print("{}:{}".format(key,word_counts[key]))
'''

# 流程控制语句
'''
score=int(input("Please input your score:"))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("You fail the test!")

score=int(input("Please input your score:"))
if score >= 60:
    print("You pass the test,and your grade is ",end="")
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("You fail the test!")

a, b = 4, 8
max_number = a
if b > a:
    max_number = b
print(max_number)

a, b = 4, 8
max_number = a if a > b else b
print(max_number)
'''
# 循环语句
# 显示骰子大小，直到出现6为止
'''
import random
x = random.randint(1,6)
print(x)
while x != 6:
    x = random.randint(1,6)
    print(x)

alist = [1,3,5,7]
for x in alist:
    print(x,end="")    

stock = {'book': 10, 'pen': 3, 'eraser': 6, 'ruler': 2}
for key, value in stock.items():
    if value < 5:
        print("({},{})".format(key, value))
'''
# 嵌套循环打印乘法口诀表
'''
for i in range(2,7,4):
    for j in range(1,10):
        print("{}*{}={:>2}  ".format(i, j, i*j), end="")  #{:>2}要求该数值要靠右对齐，并指定只给两个固定的位数显示
        print("{}*{}={:>2}  ".format(i+1, j, (i+1) * j), end="")
        print("{}*{}={:>2}  ".format(i+2, j, (i+2) * j), end="")
        print("{}*{}={:>2}  ".format(i+3, j, (i+3) * j))
    print() #换行

for i in range(2,7,4):
    for j in range(1,10):
        for k in range(i,i+5):
            print("{}*{}={:>2}  ".format(k, j, k*j), end="")
        print()
    print()
'''
# continue与break
'''
for i in range(2,9):
    if i !=2 and i!=6:
        continue
    for j in range(1,10):
        for k in range(i,i+5):
            print("{}*{}={:>2}  ".format(k, j, k * j), end="")
        print()
    print()

import random
while True:
    x = random.randint(1,6)
    print(x)
    if x == 6:
        break
'''
'''
names=['Tom','Richard','Jane']
for i, name in enumerate(names):
    print("No.{}:{}".format(i,name))

def pick(x):
    fruits = ['Apple','Banana','Orange','cherry','Pine Apple','Berry']
    return fruits[x]
alist = [1,4,2,5,0,3,4,4,2]
choices = map(pick,alist)
for choice in choices:
    print(choice)
'''
# 显示介于变量a和b之间的所有质数
'''
import sympy
a, b = 500, 600
numbers = range(a, b)
prime_numbers = filter(sympy.isprime,numbers)
print("Prime numbers({}-{}):".format(a,b))
for prime_number in prime_numbers:
    print(prime_number, end=",")
print()
'''
# 例外处理try/except

'''
while True:
    try:
        age = int(input("What is you age?"))
        break
    except:
        print("Please enter a number")
if age < 15:
    print("You are too young")

import os
try:
    os.remove('filename')
except:
    print("无法删除指定文件")


import os
try:
    os.remove('filename')
except FileNotFoundError:
    print("无法删除指定文件：找不到文件")
except PermissionError:
    print("无法删除指定文件:文件权限或种类错误")
except:
    print("无法删除指定文件：未知错误")
'''
'''
word = 'help' + 'A'
print(word)
print(word[0])
print(word[0:2])
print(word[2:4])
print(word[:2])
print(word[2:])
print(word[:2]+word[2:])

letters = ['a', 'b', 'c', 'd', 'e']
letters[:] = []
print(letters)

for i in range(5):
    print(i)
for i in range(5,9):
    print(i)
for i in range(0,10,3):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])

print(list(range(5)))

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
        else:
            print(n, 'is a prime number')

#迭代器的两个基本方法：iter() 和 next()

list = [1, 2, 3, 4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))

list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")


import sys

list = [1, 2, 3, 4]
it = iter(list)
while(True):
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

#使用 yield 实现斐波那契数列
import sys

def fibonacci(n):   #生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)     #f是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
'''
'''
#函数

def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Fred")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)

def arithmetic_mean(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(arithmetic_mean(1, 2, 3))

a = [66.5, 333, 333 ,1, 1234.5]
print(a.count(333), a.count(66.5), a.count('x'))
a.insert(2, -1)
print(a)
a.append(333)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

#将列表当做堆栈使用
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())

#将列表当作队列使用
from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

vec = [2, 4, 6]
print([3*x for x in vec])
print([[x, x**2] for x in vec])

import weapon as wp

freshfruit = ['banana', 'loganberry', 'passion fruit']
print([wp.strip() for wp in freshfruit])

vec = [2, 4, 6]
print([3*x for x in vec if x > 3])
print([3*x for x in vec if x < 2])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])

print([str(round(355/113, i)) for i in range(1, 6)])

#将3X4的矩阵列表转换为4X3列表
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print([[row[i] for row in matrix]for i in range(4)])

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

t = (12345, 54321, 'hello!')
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

#字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(list(tel.values()))
print('guido' in tel)
print('jack' not in tel)

#关键字参数dict
a = dict([('sape', 4193), ('guido', 4127), ('jack', 4098)])
print(a)

print({x: x**2 for x in (2, 4, 6)})

print(dict(sape=4139, guido=4127, jack=4098))

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
'''
# 模块
'''
import sys

print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('/n/nThe PYTHONPATH is',sys.path,'/n')
'''
'''
#1
import fibo

print(fibo.fib(100))
print(fibo.fib2(100))
#2
from fibo import fib, fib2

print(fibo.fib(100))
print(fibo.fib2(100))

#3
from fibo import *

print(fibo.fib(100))
print(fibo.fib2(100))
'''
'''
import fibo,sys

print(dir(fibo))
print(dir(sys))

a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
print(dir())
'''
# 输入和输出
'''
s = 'Hello world.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) +',and y is ' + repr(y) + '...'
print(s)
# repr()函数可以转义字符串中的特殊字符
hello = 'hello,world\n'
hellos = repr(hello)
print(hellos)
#repr()的参数可以是 Python 的任何对象

#两种方式输出一个平方与立方的表:
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=" ")
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#str.format() 的基本使用
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}'.format(food = 'spam', adjective = 'absolutely horrible'))

print('The story of {0}, {1}, and {other}'.format('Bill', 'Manfred', other = 'Georg'))

import math
print('The value of PI is approximately {}'.format(math.pi))
print('The value of PI is approximately {!r}'.format(math.pi))
print('The value of PI is approximately {0:.3f}'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
'''
# 读和写文件
'''
f = open('/Users/wsw/test/test1.txt', 'r')
print(f.read())
print(f.readline())
print(f.readline())
print(f.readlines())
'''
'''
f = open('/Users/wsw/test/test1.txt', 'w')
f.write('This is a test.')
#print(f.write('This is a test.'))
'''
'''
f = open('/Users/wsw/test/test1.txt', 'w')
value = ('the answer', 42)
s = str(value)
f.write(s)
#print(f.write(s))
'''
'''
f = open('/Users/wsw/test/test1.txt', 'rb+')
f.write(b'0123456789abcdef')
#print(f.write(b'0123456789abcdef'))
f.seek(5)
#print(f.seek(5))
f.read(1)
#print(f.read(1))
f.close()
print(f.closed)
'''
'''
import pickle

data1 = {'a': [1, 2.0, 3, 4+6j], 'b': ('string', u'Unicode string'), 'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pk1', 'wb')

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)

output.close()
'''

# Python中的类
'''
class MyClass:
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()  # 实例化类

# 访问类中的属性和方法
print("MyClass类的属性i为：", x.i)
print("MyClass类的方法f输出为：", x.f())


def _init_(self):
    self.data = []


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


class People:
    name = ''  # 定义基本属性
    age = 0
    _weight = 0  # 定义私有属性

    def __init__(self, n, a, w):  # 定义构造方法
        self.name = n
        self.age = a
        self._weight = w

    def speak(self):
        print("%s说: 我%d岁。" % (self.name, self.age))


p = People('W3Cschool', 10, 30)
p.speak()


# 类的继承
# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)  # 调用父类的构造函数
        self.grade = g

    def speak(self):
        print("%s说：我%d岁了，我在读%d年级" % (self.name, self.age, self.grade))


s = Student('ken', 10, 60, 3)
s.speak()


# 另一个类，多重继承之前的准备
class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫%s,我是一个演说家，我演讲的主题是%s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample("Tim", 25, 80, 4, "python")
test.speak()


# 方法重写
class Parent:  # 父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 子类
    def myMethod(self):
        print('调用子类方法')


c = Child()   #子类实例
c.myMethod()  #子类调用重写方法



class JustCounter:
    __secretCount = 0  # 私有变量 （双下划线）
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)  #报错，实例不能访问私有变量



# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
'''
'''
import os
print(os.getcwd())  #返回当前的工作目录
#print(dir(os))
#print(help(os))

import sys
print(sys.argv)

import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1998, 8, 1)
age = now - birthday
print(age.days)

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))
'''