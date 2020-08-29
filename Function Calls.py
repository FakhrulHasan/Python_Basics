def square(number):
    return number ** 2


def sub(number1, number2):
    return number1 - number2


print(square(3))
print(sub(6, 4))
print(sub(5, 9))


print(square(3) + 2)
print(sub(square(3), square(1 + 1)))

xyz = square(5)
print(xyz)
z = "hello world"
y = "welcome!"
a = (len(z) + len(y))
print(a)
