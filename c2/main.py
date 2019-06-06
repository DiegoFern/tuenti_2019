from functools import partial

def parser_1(inp):
    graph = {}
    for i in range(int(next(inp))):
        A,Bs=next(inp).strip().split(':')
        Bs=Bs.split(',')
        graph[A]=graph.get(A,[])+(Bs)
    return graph

def solve(G,o):
    if o in solve.d:
        return solve.d[o]
    else:
        return sum(map(partial(solve,G),G[o]))

def main():
    import sys
    N=sys.stdin
    s=1
    for i in range(int(next(N))):
        solve.d={'New Earth':1}
        G=parser_1(N)
        print('Case #{}: {}'.format(s,solve(G,'Galactica')))
        s+=1
main()
