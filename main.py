def divide(x, y):
    return x / y
def multiple (x,y):
    return x * y

def subtraction (x, y):
    return x - y
if __name__ == '__main__':

    print((divide(multiple(subtraction(123454678, 1,),1 ),123454676)))


a = int(input())
#-----------------------------------------------------------------------------------------------------------------------
#                               № 1
def arithmetic(x, y, z):
    if z == "+":
        return (x + y)
    elif z == "-":
        return (x - y)
    elif z == "*":
        return (x * y)
    elif z == "/":
        return (x / y)
    else:
        return ("Неизвестная ошибка")

if __name__ == '__main__':

    print(arithmetic(2, 3, '+'))
    print(arithmetic(2, 2, '*'))
    print(arithmetic(4, 2, '-'))
    print(arithmetic(4, 2, '/'))
    print(arithmetic(4, 2, 0))
#-----------------------------------------------------------------------------------------------------------------------
#                                 № 2
def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#-----------------------------------------------------------------------------------------------------------------------
#                                № 3
def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5

    k = (p, s, d)

    return k


print(square(16))
#-----------------------------------------------------------------------------------------------------------------------
#                                  № 4
n = int(input(10))
m = int(input(1000))
y = int(input(5))

def bank(n, m, y):
        nal = n
        year = y
def money():
    if year >0:
        nal = n*1.1+m
        year = year -1
        return money()
    else:
        return nal

    print(nal)
#-----------------------------------------------------------------------------------------------------------------------
#                                № 5
from cmath import sqrt


def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    if number == 0 or number == 1:
        return False
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:
            return False
    return True

n = int(input('56: '))
print(is_prime(n))

