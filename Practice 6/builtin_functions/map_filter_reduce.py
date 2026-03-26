from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() squares each number
squared = list(map(lambda x: x**2, numbers))
print(squared)

# filter() keeps only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# reduce() sums numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)