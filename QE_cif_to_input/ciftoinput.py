import math
a = 1
b = 1
c = 1

alpha = math.pi/2
beta = math.pi/2
gamma = math.pi*(2/3)

def cellvectors(a,b,c,alpha,beta,gamma):
    x1 = round(a,8)
    y1 = round(0,8)
    z1 = round(0,8)
    x2 = round(b*math.cos(gamma),8)
    y2 = round(b*math.sin(gamma),8)
    z2 = round(0,8)
    x3 = round(c*math.cos(beta),8)
    y3 = round(c*(math.cos(alpha)- math.cos(gamma)*math.cos(beta))/math.sin(gamma),8)
    z3 = round((b*b*math.sin(beta)*math.sin(beta) - y3*y3)**(0.5),8)

    return [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]

print(cellvectors(a,b,c,alpha,beta,gamma))