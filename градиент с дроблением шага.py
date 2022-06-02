# f(x) = 2x1^2 + x2^2 + x1x2 + x1 + x2;         x0 = (0; 0)         min = (-0.1429; 0.4286)
import math
import sympy as s
from sympy import *
print('***Метод с дроблением шага***')
print('Ввести первую координату:')
x1 = int(input())
print('Введите вторую координату:')
x2 = int(input())
print('Погрешность:')
eps = float(input())
print('Введите альфа:')
alp = float(input())
print('Введите шаг:')
lam = float(input())

x = Symbol('x', real = True)
y = Symbol('y', real = True)

f = 2*x**2 + y**2 + x*y + x + y

it = 1
while s.sqrt(diff(f, x)**2 + diff(f, y)**2).subs({x: x1, y:x2}) > eps:
    x_1 = x1 - alp * diff(f, x).subs({x: x1, y:x2})
    x_2 = x2 - alp * diff(f, y).subs({x: x1, y:x2})
    alp1 = alp
    while f.subs({x:x_1, y:x_2}) - f.subs({x:x1, y:x2}) > (-1) * alp1 * eps * s.sqrt(diff(f, x)**2 + diff(f, y)**2).subs({x: x1, y:x2}):
        alp1 = alp1 * lam
        x_1 = x1 - alp1 * diff(f, x).subs({x: x1, y:x2})
        x_2 = x2 - alp1 * diff(f, y).subs({x: x1, y:x2})
    it += 1
    x1 = x_1
    x2 = x_2

print(f'Точка минимума: ({x1:.6f},{x2:.6f})')
print('Количество итераций:',it)


