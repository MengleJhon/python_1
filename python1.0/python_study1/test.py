# print('{a} a word in {b}.'.format(a = 'with',b = 'came'))
# print('{0} a word in {1}.'.format('with','came'))
# print('{} a word in {}.'.format('with','came'))
#
# a = [15,True]
# print(a[-1])
#
# print(5,'word')
# print('hello' in a)
#
# for a in 'hello':
#     print(a)

# 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         print('{} X {} = {}'.format(i,j,i*j))

# g到kg转换函数
# def g_to_kg(g):
#     return str(g/1000) + 'kg'
#
# print(g_to_kg(1345))

# 计算矩形长边长
# def pythagorean_theorem(a,b):
#     return 'The right triangle third side\'s lenth is {}'.format((a**2 + b**2)**(1/2))
#
# print(pythagorean_theorem(3,3))

# 打印1~100内的偶数
# def even_print():
#     for i in range(1,101):
#         if i % 2 == 0:
#             print(i)
#
# even_print()

# 创建10个文本
# def text_creation():
#     path = 'C:/Users/LX/Desktop/'
#     for name in range(1,11):
#         # with open(path + str(name) + '.txt','w') as text:
#         text = open(path + str(name) + '.txt','w')
#         text.write(str(name))
#         text.close()
#
# text_creation()
# print('Done')

# 复利公式
# def invest(amount,rate,time):
#     print('principal amount:{}'.format(amount))
#     for t in range(1,time + 1):
#         amount = amount * (1 + rate)
#         print('year {}: ${}'.format(t,amount))
#
# invest(100,.05,8)
# invest(2000,.025,5)

# 数据结构
a = [1,2,3]
# a[1] = 5
# print(a)
#
# del a[0:1]
# print(a)

b = [4,5,6,7,8]
print(zip(a,b))
print(list(zip(a,b)))
print(*zip(a,b))
print(list(zip(*zip(a,b))))


c = [j + 1 for j in range(1,10)]
print(c)
d = [n for n in range(1,10) if n % 2 == 0]
print(d)
e = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
print(e)

f = {i:i + 1 for i in range(4)}
print(f)
g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(g)

letters = ['a','b','c','d','e','f','g']
for num,letter in enumerate(letters):
    print(letter,'is',num + 1)
print(list(enumerate(letters)))

