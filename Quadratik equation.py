print(' a*x**2+b*x+c=0')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
discr = b ** 2 - 4*a*c
print('Discriminant = ' + str(discr))
if discr < 0:
    print('No')
elif discr == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))
