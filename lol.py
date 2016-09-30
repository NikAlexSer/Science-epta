import math
import random as random_number
#import matplotlib.pyplot as plt
from numpy import array
from sympy import *

pprint(math.sin(math.radians(54)))
x = Symbol('x')
result = 0.0
i = 0.0
while (i <= 2.0):
    result += (pow(-1, (i)) * (pow(x, (2*i)) / factorial(2 * i)))
    i += 1.0
pprint(result)
pprint('\n')
#pprint(result.subs(x, math.radians(54)))