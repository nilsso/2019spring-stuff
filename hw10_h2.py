#!/usr/bin/env python3
from sympy import symbols, Poly

x = symbols('x')

def terms(p, x):
    for t in Poly(p, x).all_terms():
        yield t[0][0], t[1]

# If $sum_{n\ge 0}n^d z^n=\frac{Q_d(z)}{{(1-z)}^{d+1}}$
# then $Q_d(z)={(1-z)}^{d+1}\cdot sum_{n\ge 0}n^d z^n$
#
# @param z Value to evaluate $Q_d(z)$ at.
# @param d Degree.
# @return $Q_d(z)$ evaluated with parameters $z$ and $d$.
def Q(z, d):
    a = (1-x)**(d+1)*sum(n**d*x**n for n in range(d+1))
    b = sum(c*x**p for p, c in terms(a, x) if p<(d+1))
    return b.subs(x, z)

if __name__ == '__main__':
    from sys import argv
    z, d = map(int, argv[1:])
    print(Q(z, d))

