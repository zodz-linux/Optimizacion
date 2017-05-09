import numpy
import itertools

def direccionesR(n):
    """
    n  :  numero de vectores canonicos
    """
    puntos=[]
    for  i in xrange(1,n):
        tmp=itertools.combinations(range(n),i)
        for element in tmp:
            point=[]
            for j in xrange(n):
                if j in element:
                    point.append(1)
                else: point.append(-1)
            puntos.append(point)
    puntos.append([1]*n)
    puntos.append([-1]*n)
    return  np.array(puntos)

def EVOP(p,delta,epsilon,f):
    ndimension=len(p)
    direcciones=direccionesR(ndimension)
    while delta > epsilon:
        vertices=[[0,list(p+((delta*direccion)))] for direccion in direcciones]
        for v in vertices:
            v[0]=f(v[1])
        vertices.sort()
        if f(p) > vertices[0][0]:
            p= vertices[0][1]
        else:
            delta*=.5
    return p
