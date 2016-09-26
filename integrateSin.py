import math
import random as random_number
import matplotlib.pyplot as plt
from numpy import array
from sympy import *


def leftAngles(a, b, n):
    result = 0
    i = 0
    h = (b - a) / n  # шаг сетки
    while i <= n-1:
        result += sin(a + h*i)
        i += 1
    result *= h
    return result


def rightAngles(a, b, n):
    result = 0
    i = 1
    h = (b - a) / n  # шаг сетки
    while i <= n:
        result += sin(a + i*h)
        i += 1
    result *= h
    return result


def middleAngles(a, b, n):
    result = 0
    i = 1
    h = (b - a) / n     # шаг сетки
    while i <= n:
        result += sin(a + i * h - h/2)
        i += 1
    result *= h
    return result


def trapezian(a, b, n):
    result = 0
    i = 1
    h = (b-a)/n
    while i <= n-1:
        result *= sin(a + i*h)
        i += 1
    result += (sin(b)) / 2
    result += (sin(a)) / 2
    result *= h
    R = (-pow(h, 3)/12) * (-cos(a) + cos(b))
    result += R
    return result


def tailor(a, b, n):
    resultA = 0.0
    resultB = 0.0
    result = 0.0
    i = 0
    # m =
    A = (b-a)/2
    while i <= n:
        result += (sin(A + i*pi/2) / factorial(i)) * pow((x - A), i)
        i += 1
    i = 0
    while i <= n:
        resultB += (pow(sin(A), i) / factorial(i)) * pow((b - A), i)
        i += 1
    #pprint(resultA)
    #pprint(resultB)
    #result += resultB - resultA
    return result

y = Symbol('y')
z = Symbol('z')
x = Symbol('x')
f = Function('f')
g = sin(x)
dif = g.diff()
pprint(integrate(f(x), x))
pprint('Производная второго порядка %s' % dif.diff())
pprint('%s = %s' % (f(x), g))


pprint('Введите количесвто отрезков')
n = int(input())
pprint('Введите нижнюю границу')
lowInter = float(input())      # нижняя граница
pprint('Введите верхнюю границу')
highInter = float(input())  # верхняя граница

res = middleAngles(lowInter, highInter, n)
pprint('Средние прямоугольники: %.8f' % res)

res = leftAngles(lowInter, highInter, n)
pprint('Левые прямоуголбники %.8f' % res)

res = rightAngles(lowInter, highInter, n)
pprint('Правые прямоугольбники %.8f' % res)

res = trapezian(lowInter, highInter, n)
pprint('Метод трапеций %.8f' % res)

res = integrate(tailor(lowInter, highInter, n), (x, lowInter, highInter))
pprint(tailor(lowInter, highInter, n))
print(tailor(lowInter, highInter, n))
pprint('\n')
pprint('\n')
pprint('\n')
pprint(res)