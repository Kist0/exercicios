def func1(x, y):
    return (3*x)**2 + y**2

def func2(x, y):
    return 2*(x**2) + (5*y)**2

def func3(x, y):
    return -100*x + y**3

qtd = int(input())
for i in range(qtd):
    numbrs = input().split()
    x = int(numbrs[0])
    y = int(numbrs[1])
    r = func1(x, y)
    b = func2(x, y)
    c = func3(x, y)

    #print('r={}, b={}, c={}'.format(r, b, c))

    if r > b and r > c:
        print('Rafael ganhou')
    elif b > r and b > c:
        print('Beto ganhou')
    else:
        print('Carlos ganhou')