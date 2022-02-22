import sympy as s


def steepest_descent(func, x0, iterations):
    n = len(x0)
    lam = s.symbols('lam')
    xsymbols = s.Array(s.symbols('x1:%d'%(n+1)))  # makes a tuple of symbols (x1, x2, x3... xn)
    xisymbols = s.Array(s.symbols('xi1:%d'%(n+1)))  # makes a tuple of symbols (xi1, xi2, xi3... xin)

    # Do derivative, find function for lamba*
    f = func(xisymbols)  # Set up function
    nabla_f = s.diff(f, xisymbols)  # Differentiate w.r.t x
    xip1 = xsymbols - lam*nabla_f.subs([(xisymbols[i], xsymbols[i]) for i in range(n)])  # Find equation for xi+1
    fip1 = f.subs([(xisymbols[i], xip1[i]) for i in range(n)])  # Find equation for f(xi+1)
    dfi_dlam = s.diff(fip1, lam)  # Find derivative w.r.t lambda
    lamstar = s.solve(dfi_dlam, lam)  # Solve for lambda*
    if len(lamstar) != 1:
        raise Exception(f'Multiple solutions for lambda*, check what happened: {lamstar}')
    else:
        lamstar = lamstar[0]  # Load in the single solution

    x0 = s.Array(x0)  # Make x0 into a sympy Array (works for lists, tuples, numpy ndarrays, sympy arrays)

    xnext = x0
    for i in range(iterations):  # Loop for iterations, print values
        print(f"Iteration {i}:")
        print(f"xi = {xnext} = [{', '.join([str(xnext_val.n(3)) for xnext_val in xnext])}]")
        print(f"f(xi) = {f.subs([(xisymbols[i], xnext[i]) for i in range(n)])} = {f.subs([(xisymbols[i], xnext[i]) for i in range(n)]).n(3)}")
        lam_star = lamstar.subs([(xsymbols[i], xnext[i]) for i in range(n)])  # Calculate value of lambda*
        print(f"lambda* = {lam_star} = {lam_star.n(3)}")
        xnext = xip1.subs([(xsymbols[i], xnext[i]) for i in range(n)]).subs([(lam, lam_star)])  # Calculate next x
        print(f"xi+1 = {xnext} = [{', '.join([str(xnext_val.n(3)) for xnext_val in xnext])}]\n")


if __name__=="__main__":
    steepest_descent(lambda x: x[0] - x[1] + 2*x[0]**2 + 2*x[0]*x[1] + x[1]**2, [0, 0], 5)  # Test steepest descent