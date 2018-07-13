#-*-coding:utf-8-*-
pets = ['dog','cat','pig','dog','cat','goldfish']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

pets.remove('dog')
print(pets)