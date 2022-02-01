
import math
def d1(s,x,r,sig,t):
   return (math.log10(s/x)+((r+((sig**2)/2))*t))/(sig*(math.sqrt(t)))

def d2(s,x,r,sig,t):
    return (d1(s,x,r,sig,t)-(sig*(math.sqrt(t))))

def c(s,x,r,sig,t,n):
    return ((s*n*(d1(s,x,r,sig,t)))-(x*(math.exp(-r*t))*n*(d2(s,x,r,sig,t))))

def p(s,x,r,sig,t,n):
    return ((x*(math.exp(-r*t))*n*(-(d2(s,x,r,sig,t))))-(s*n*(-(d1(s,x,r,sig,t)))))

