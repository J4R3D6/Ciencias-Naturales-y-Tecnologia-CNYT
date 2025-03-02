import math
def sum(a, b):
    return (a[0]+b[0],a[1]+b[1])

def res(a, b):
    return (a[0]-b[0],a[1]-b[1])

def mult(a,b ):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+b[0]*a[1])

def div(a,b):
    return ((a[0]*b[0]+a[1]*b[1])/(b[0]**2+b[1]**2),(a[1]*b[0]-a[0]*b[1])/(b[0]**2+b[1]**2))

def module(a):
    return (a[0]**2+a[1]**2)**(1/2)

def conjugado(a):
    return (a[0], -1*a[1])

def face(a):
    return math.atan2(a[1],a[0])
    
def cartesiana_a_polar(a):
    return (module(a),face(a))

def polar_a_cartesiana(a):
    return (a[0]*math.cos(a[1]),a[0]*math.sin(a[1]))

def operaciones():
    a=(4,-3)
    c = mult(a,a)

    print(c)
if __name__ == "__main__":
    operaciones()
