numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']

# enumerate() for index and value)
for i, num in enumerate(numbers):
    print(i, num)

# zip() to pair numbers and letters
for num, letter in zip(numbers, letters):
    print(num, letter)

# Type checking and conversions
x = "123"
y = 456
print("Type of x:", type(x))
print("Type of y:", type(y))

# Convert string to integer
x_int = int(x)
print("After conversion, type of x_int:", type(x_int))