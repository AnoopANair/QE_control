import math
a = 1
b = 1
c = 1

alpha = math.pi/2
beta = math.pi/2
gamma = math.pi*(2/3)

x1 = a
y1 = 0
z1 = 0
x2 = b*math.cos(gamma)
y2 = b*math.sin(gamma)
z2 = 0
x3 = c*math.cos(beta)
y3 = c*(math.cos(alpha)- math.cos(gamma)*math.cos(beta))/math.sin(gamma)
z3 = (b*b*math.sin(beta)*math.sin(beta) - y3*y3)**(0.5)

print([[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]])
