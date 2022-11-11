from fractions import Fraction

def formatPoint(_input):
    if (_input[0], _input[-1]) == ('(', ')'):
        point = _input[1:-1].split(',')
    else:
        point = _input.split(',')

    point = [i.strip() for i in point]
    
    if '.' in point[0]: point[0] = float(point[0])
    else: point[0] = int(point[0])
    if '.' in point[1]: point[1] = float(point[1])
    else: point[1] = int(point[1])

    return point

def findSlope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return Fraction(Fraction(y2 - y1), Fraction(x2 - x1))

def findYIntercept(point1, point2):
    slope = findSlope(point1, point2)

    return point1[1] - point1[0] * slope

def findEquation(slope, yIntercept):
    equation = 'y = '

    if slope != 1:
        if slope.denominator == 1: equation += f'{slope}x'
        else: equation += f'({slope})x'
    else: equation += 'x'

    if yIntercept != 0:
        equation += f' + {yIntercept}'

    return equation.replace('+ -', '- ')

choice = int(input('''Y = MX + B Calculation Tool
------------------------------
1. Find equation from two points
2. Check if point is on line

Choose one: '''))

if choice == 1:
    point1 = formatPoint(input('\nEnter point one: '))
    point2 = formatPoint(input('Enter point two: '))

    slope = findSlope(point1, point2)
    yIntercept = findYIntercept(point1, point2)
    equation = findEquation(slope, yIntercept)

    print(f'\nSlope: {slope}')
    print(f'Y-intercept: {yIntercept}')
    print(f'Equation: {equation}')

else:
    point = formatPoint(input('\nEnter point: '))
    slope = Fraction(input('Enter slope: '))
    yIntercept = Fraction(input('Enter Y-intercept: '))

    if point[1] == point[0] * slope + yIntercept: print('\nThe point is on the line')
    else: print('\nThe point is not on the line')
