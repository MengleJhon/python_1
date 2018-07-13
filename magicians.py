magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
    print(magician.title() + ', that was a great trick!\n')
print('Thank you!')

for value in range(1,5):
    print(value)
for value in range(1,5,2):
    print(value)
for value in range(1,5,3):
    print(value)

numbers = list(range(1,5))
print(numbers)

squares = []
for value in range(1,11,2):
    square = value**2
    squares.append(square)
    # squares.append(value**3)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value**2 for value in range(1,11,2)]
print(squares)

magicians = ['alice','david','carolina','blice','cavid','darolina']
print(magicians)
print(magicians[1:5])
print(magicians[:5])
print(magicians[1:])
print(magicians[-3:])

defens = [1,5,4,2,3]
defens.sort(reverse = True)
print(defens)
print(defens[:2])
for defen in defens[:2]:
    print(defen)

magicians = ['alice','david','carolina','blice','cavid','darolina']
for magician in magicians[:3]:
    print(magician.title())

magicians = ['alice','david','carolina','blice','cavid','darolina']
another_magicians = magicians[:]
print(magicians)
print(another_magicians)

magicians = ['alice','david','carolina','blice','cavid','darolina']
another_magicians = magicians[:]
magicians.append('huawei')
another_magicians.append('xiaomi')
print(magicians)
print(another_magicians)

magicians = ['alice','david','carolina','blice','cavid','darolina']
another_magicians = magicians
magicians.append('huawei')
another_magicians.append('xiaomi')
print(magicians)
print(another_magicians)

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (400,100)
for dimension in dimensions:
    print(dimension)


