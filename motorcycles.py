motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)
print('The last motorcycle I owned was a ' + popped_motorcycle.title() + '.')

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

motorcycles = ['honda','yamaha','dageda','suzuki','ducati']
motorcycles.sort()
print(motorcycles)
motorcycles = ['honda','yamaha','dageda','suzuki','ducati']
motorcycles.sort(reverse = True)
print(motorcycles)

motorcycles = ['honda','yamaha','dageda','suzuki','ducati']
print('Here is the original list:')
print(motorcycles)
print('\nHere is the sorted list:')
print(sorted(motorcycles))
print('\nHere is the reverse sorted list:')
print(sorted(motorcycles,reverse = True))
print('\nHere is the original list again:')
print(motorcycles)

motorcycles = ['honda','yamaha','dageda','suzuki','ducati']
print(motorcycles)
motorcycles.reverse()
print(motorcycles)

motorcycles = ['honda','yamaha','dageda','suzuki','ducati']
print(len(motorcycles))

motorcycles = ['honda','yamaha','dageda','suzuki','ducati']
print(motorcycles[1])
print(motorcycles[-1])
print(motorcycles[-2].title())
print(motorcycles[-3])
