#Calculator

#Import math module and pi
from math import pi

#Define functions for each shape
def square(s):
    area = s * s
    return area
def rectangle(l, w):
    area = l * w
    return area 
def triangle(h, b):
    area = (h * b) / 2
    return area
def circle(r):
    area = pi * r * r
    return area

#Intro
print('=============================')
print('      AREA CALCULATOR       ')
print('=============================')

#Menu 
print('\n1. Square')
print('2. Rectangle')
print('3. Triangle')
print('4. Circle')

#Input
wich_shape = int(input('\nWich shape: '))

#If statements to call the functions
if wich_shape == 1:
    side = float(input('Side: '))
    print(f'The area is  {square(side)}')
elif wich_shape == 2:
    length = float(input('Length: '))
    width = float(input('Width: '))
    print(f'The area is  {rectangle(length, width)}')
elif wich_shape == 3:
    height = float(input('Height: '))
    base = float(input('Base: '))
    print(f'The area is  {triangle(height, base)}')
elif wich_shape == 4:
    radius = float(input('Radius: '))
    print(f'The area is  {circle(radius)}')
else:
    print('Invalid option')

