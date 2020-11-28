"""
This code could:

1. convert cell parameters to cell vectors


"""



import math
a = 1
b = 1
c = 1

alpha = math.pi/2
beta = math.pi/2
gamma = math.pi*(2/3)

def cellvectors(a,b,c,alpha,beta,gamma):
    x1 = a
    y1 = 0
    z1 = 0
    x2 = b*math.cos(gamma)
    y2 = b*math.sin(gamma)
    z2 = 0
    x3 = c*math.cos(beta)
    y3 = c*(math.cos(alpha)- math.cos(gamma)*math.cos(beta))/math.sin(gamma)
    z3 = (b*b*math.sin(beta)*math.sin(beta) - y3*y3)**(0.5)

    return [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]

print(cellvectors(a,b,c,alpha,beta,gamma))