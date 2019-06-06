from itertools import chain,repeat
coord_Types=dict(
        chain(
            zip(zip(repeat(0),range(50)),'1234567890') ,
            zip(zip(repeat(1),range(50)),'QWERTYUIOP') ,
            zip(zip(repeat(2),range(50)),'ASDFGHJKL;') ,
            zip(zip(repeat(3),range(50)),'ZXCVBNM,.-') ,
            )
        )
Types_coord={b:a for a,b in coord_Types.items()}

def diff(t1,t2):
    t1 = Types_coord[t1]
    t2 = Types_coord[t2]
    return (t1[0]-t2[0])%4,(t1[1]-t2[1])%10

def suma(t1,vect):
    if t1==' ':
        return t1
    a,b=Types_coord[t1]
    return coord_Types[(a+vect[0])%4,(b+vect[1])%10]

def main():
    import sys
    N=sys.stdin
    n=next(N)
    for i in range(int(n)):
        sign=next(N).strip()
        text=next(N).strip()

        delt=diff(sign,text[-1])
        origin = ''.join(map(lambda x:suma(x,delt),text)
                )
        print('Case #{}: {}'.format(i+1,origin))

main()
