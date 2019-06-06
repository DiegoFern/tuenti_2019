from collections import Counter
from functools import *
def _mcm(x, y): 
    a=x*y 
    while(y): 
        x, y = y, x % y 
  
    return a/x 
def _gcd(x, y): 
    a=x*y 
    while(y): 
        x, y = y, x % y 
  
    return x               
mcm=lambda x:reduce(_mcm,x)
gcd=lambda x:reduce(_gcd,x)
def parser_1(x):
    C=Counter(map(int,x.split()))
    #calculate min X possible:
    p=[]
    X=mcm([o/gcd([C[o],o]) for o in C])
    _,A,B=(X,sum(map(lambda x:(X*x[1])/x[0],C.items())),sum(p*X for n,p in C.items()))
    return B,A

def main():
    S=sys.stdin
    s=1
    for i in range(int(next(S))):
        next(S)
        a,b=parser_1(next(S).strip())
        a2=a/gcd([a,b])
        b2=b/gcd([a,b])
        print('Case #{}: {}/{}'.format(s,int(a2),int(b2)))
        s+=1
import sys
main()
