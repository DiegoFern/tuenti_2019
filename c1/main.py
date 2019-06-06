import sys
def get_number(x,y):
    return (x+1)//2+(y+1)//2

def parser(inp):
    s=1
    for i in range(int(next(inp))):
        print('Case #{}: {}'.format(s,get_number(*(map(int,next(inp).split())))))
        s+=1
parser(sys.stdin)
