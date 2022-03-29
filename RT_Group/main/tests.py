from itertools import product, permutations


def factorial(x):
    print('start x', x)
    z = x

    def result(z):
        if z == 0:
            print(z, 'if')
        else:
            print((factorial(x) + factorial(x)), 'else', x)
            z -= z

    result(z)

def is_odd(x):
    print(factorial(x), x)


factorial(6)
