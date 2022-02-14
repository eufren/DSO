import numpy as np

def GoldenSection(func, x1, x2, x3, iterations):

    
    GoldenRatio = 0.61803
    
    for i in range(iterations):
          
        h1 = x2-x1
        h2 = x3-x2
        
        print(f"Iteration:{i}\n")
        print(f"x1:{x1}, x2:{x2}, x3:{x3}\n")
        print(f"h1:{h1}, h2:{h2}\n")

        y1 = func(x1)
        y2 = func(x2)
        y3 = func(x3)
        
        print(f"y1:{y1}, y2:{y2}, y3:{y3}")
        
        if h1 > h2: # if left
            x4 = GoldenRatio*(h1) + x1

        
        else: # if right
            x4 = (1-GoldenRatio)*(h2) + x2


        if func(x4) < func(x2):
            if x2 < x4:
                x1 = x2
            else:
                x3 = x2
            x2 = x4
            
        else:
            if x4>x2:
                x3 = x4
            else:
                x1 = x4
            
        y4 = func(x4)
        print(f"x4:{x4}, y4:{y4}\n")
        
    return x4, func(x4)
        

def InverseParabolic(func, x1, x2, x3, iterations):
    
    
    
    for i in range(iterations):
        

          
        print(f"Iteration:{i}\n")
        print(f"x1:{x1}, x2:{x2}, x3:{x3}\n")
        
        y1 = func(x1)
        y2 = func(x2)
        y3 = func(x3)
        
        print(f"y1:{y1}, y2:{y2}, y3:{y3}")
         
       
        x4_num = (y3-y2)*(x2**2-x1**2)+(y1-y2)*(x3**2-x2**2)
        x4_den = 2*((y3-y2)*(x2-x1)-(y2-y1)*(x3-x2))
        
        x4 = x4_num/x4_den
       
        if func(x4) < func(x2):
            if x2 < x4:
                x1 = x2
            else:
                x3 = x2
            x2 = x4

        else:
            if x4>x2:
                x3 = x4
            else:
                x1 = x4
            
        y4 = func(x4)
        print(f"x4:{x4}, y4:{y4}\n")
           
    return x4, func(x4)


def NewtonMethod(func, func_prime, func_dprime, x_0, iterations):
        
    for i in range(iterations):
        x_0 = x_0-(func_prime(x_0)/func_dprime(x_0))
    
    return x_0
    
    
