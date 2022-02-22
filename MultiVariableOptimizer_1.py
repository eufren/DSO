import LineSearch
import numpy as np
import sympy as s
from sympy.vector import CoordSys3D

R = CoordSys3D('R')



x1, x2, lam = s.symbols('x1, x2, lam')
x = s.Matrix([x1, x2])

# f = x - x + 2*x**2 + 2*x*x + x**2

f = x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2

nabla_f = s.diff(f, x)

xi = x - lam*nabla_f
fi = f.subs([(x1, xi[0]), (x2, xi[1])])

dfi_dlam = s.diff(fi, lam)

# lam_star = s.solve(dfi_dlam, lam)[0]

# print(lam_star.subs([(x1, 0), (x2, 0)]))




# Cauchy(lambda x: x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1]+x[1]**2, 
#        lambda x: np.array([1+4*x[0]+2*x[1], -1+2*x[0]+2*x[1]]),
#        np.array([0, 0]), 
#        lambda l: 2*l-2, 1)


def Cauchy(func, nabla_f, df_dlambda, x0, iterations):
    
    xi = x0
    
    for i in iterations:
        xi =  func(xi - lam**func(xi))
        
    


