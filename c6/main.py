import networkx as nx
from networkx.algorithms.dag import all_topological_sorts
def length_min_2(x):
    x = iter(x)
    try:
        next(x)
    except:
        return 0
    try:
        next(x)
    except:
        return 1

    return 2

def get_rel(a,b):
    for i,j in zip(a,b):
        if i!=j:
            return i,j

def parser_1(inp):
    n=nx.DiGraph()
    last=''
    for i in range(int(next(inp))):
        
        act_string=next(inp).strip()
        for i in act_string:
            n.add_node(i)
        if last!='' and last!=act_string:
            S=get_rel(last,act_string,)
            if S is not None:
                n.add_edge(*S)

        last=act_string
    it=all_topological_sorts(n)
    ans={2:'AMBIGUOUS',1:''}[length_min_2(it)]
    if ans=='':
        ans=' '.join(next(all_topological_sorts(n)))
    return ans
def main():
    import sys
    N=sys.stdin
    n=next(N)
    for i in range(int(n)):
        print('Case #{}: {}'.format(i+1,parser_1(N)))
main()
