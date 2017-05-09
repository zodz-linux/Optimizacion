
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

def IntervalosPorLaMitad(a,b,epsilon,f):
    """
    a        : Cota inferior del intervalo
    b        : Cota superior del intervalo
    epsilon  : Error
    f        : Funcion objetivo
    """
    xm=(b+a)/2.0
    l=b-a
    while abs(l) > epsilon:
        x1=a+(l*.25)
        x2=b-(l*.25)
        if f(x1)<f(xm):
            b=xm
            xm=x1
        else:
            if f(x2)<f(xm):
                a=xm
                xm=x2
            else:
                a=x1
                b=x2
        l=b-a
    return (a,b)


def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return float(fibonacci(n-1) + fibonacci(n-2))

def MetodoFibonacci(a,b,iteraciones,f):
    """
    a            : Cota inferior del intervalo
    b            : Cota superior del intervalo
    iteraciones  : Numero de iteraciones maximas
    f            : Funcion objetivo
    """
    L=b-a
    contador=2
    f1=fibonacci(iteraciones)
    while  contador <= iteraciones:
        lxk=0
        lxk= (fibonacci(iteraciones-contador)/f1)*L
        x1=a+lxk
        x2=b-lxk
        if f(x1) > f(x2):
            a=x1
        else:
            if f(x1) < f(x2):
                b=x2
            else:
                a=x1
                b=x2
        contador+=1
    return (a,b)

def MetodoSeccionDorada(a,b,epsilon,f):
    """
    a        : Cota inferior del intervalo
    b        : Cota superior del intervalo
    epsilon  : Error
    f        : Funcion objetivo
    """
    aw=0
    bw=1
    lw=1
    while lw>epsilon:
        w1=aw+(0.618*lw)
        w2=bw-(0.618*lw)
        if f(w1) < f(w2):
            aw=w2
        else:
            bw=w1
        lw=bw-aw
    return (w1*3,w2*3)

def InterpolacionCuadratica(epsilonX,epsilonY,delta,x1,f):
    def CalculateValue(x1,x2,x3,f1,f2,f3):
        a1=(f2-f1)/(x2-x1)
        a2=(1/(x3-x2))* (((f3-f1)/(x3-x1))-((f2-f1)/(x2-x1)))
        return  (.5*(x1+x2))-(a1/(2*a2))
    data=[]
    data.append([f(x1),x1])
    x2=x1+delta
    data.append([f(x2),x2])
    if data[0][0] > data[1][0]:
        data.append([f(x1+(2*delta)),(x1+(2*delta))])
    else:
        data.append([f(x1-delta),(x1-delta)])
    data.sort()
    xb=CalculateValue(data[0][1],data[1][1],data[2][1],data[0][0],data[1][0],data[2][0])
    data.pop()
    data.append([f(xb),xb])
    while (abs(data[0][0]-data[2][0])>epsilonY) or (abs(data[0][1]-data[2][1]) > epsilonX ):
        data.sort()
        xb=CalculateValue(data[0][1],data[1][1],data[2][1],data[0][0],data[1][0],data[2][0])
        data.pop()
        data.append([f(xb),xb])
    return  data[2][0],data[2][1]
