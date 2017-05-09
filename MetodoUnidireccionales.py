import numpy

def BusquedaExhaustiva(a,b,n,f):
    """
    a  : Cota inferior del intervalo
    b  : Cota superior del intervalo
    n  : Numero de subintervalos
    f  : Funcion objetivo
    """
    x1=a
    deltaX= (b-a)/float(n)
    x2=x1+deltaX
    x3=x2+deltaX
    while x3 <= b:
        if f(x1) >= f(x2) and   f(x2) <= f(x3): return  (x1,x3)
        x1=x2
        x2=x3
        x3=x2+deltaX
    if f(a) < f(b): return (a,a)
    else: return  (b,b)
