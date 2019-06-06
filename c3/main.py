
def T(W,H,bx,by):
    by=by+[-(i)-1 for i in by]
    by=[i+H for i in by]
    return W,H*2,bx+bx,by

def L(W,H,bx,by):
    bx=bx+[-i-1 for i in bx]
    bx=[i+W for i in bx]
    return W*2,H,bx,by+by

def R(W,H,bx,by):
    bx=bx+[W*2-(i)-1 for i in bx]
    return W*2,H,bx,by+by

def B(W,H,bx,by):
    by=by+[H*2-i-1 for i in by]
    return W,H*2,bx+bx,by





def parser(inp):
    s=1
    for i in range(int(next(inp))):
        W,H,F,P =list(map(int,(next(inp).split())))
        fold=[]
        for i in range(int(F)):
            fold.append(next(inp).strip())
        px,py=[],[]
        for i in range(int(P)):
            x,y=next(inp).strip().split()
            x,y=int(x),int(y)
            px.append(x)
            py.append(y)
        for i in fold:
            W,H,px,py=eval(i)(W,H,px,py)
        print('Case #{}:'.format(s))
        s+=1
        for a,b in sorted(zip(px,py)):
            print('{} {}'.format(a,b))

import sys
parser(sys.stdin)
