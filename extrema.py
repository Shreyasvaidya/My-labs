import math
maxnum=-10000
minnum=10000
n=0
import math
def f(x):
    return 72*(math.sin(x))+math.cos(72*x)
x=22/(7*142) 
y=22/(7*146)
while x<=6.28 and y<=6.28:
    if max(f(x),f(y))>maxnum:
        maxnum=max(f(x),f(y))
        maxc1=x
        maxc2=y
    if min(f(x),f(y))<minnum:
        minnum=min(f(x),f(y))
        minc1=x
        minc2=y
    n-=1
    x=((22/14)-(2*n*22/7))/71
    y=((22/14)-(2*n*22/7))/73
    
print(maxnum,minnum,maxc1,maxc2,f(maxc1),f(maxc2),minc1,minc2,f(minc1),f(minc2))    

