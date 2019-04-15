#!/usr/bin/env python3
from sympy import *

x = symbols('x')

def Q(z, d):
    p = (1-x)**(d+1)*sum(n**d*x**n for n in range(d+1))
    r = sum(t[1]*x**t[0][0] for t in Poly(p, x).all_terms() if t[0][0]<(d+1))
    return r.subs(x, z)

if __name__ == '__main__':
    from sys import argv
    z, d = map(int, argv[1:])
    print(Q(z, d))

