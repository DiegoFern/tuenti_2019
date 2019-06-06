from math import pi
tau = 2*pi
import numpy as np
class state:
    def __init__(self,n,max_c,fuel,path,cargament,moons,pos,minerals_moons
                ,moon_r
                ):
        self.pos = pos
        self.moon_r=moon_r
        self.n,self.max_c,self.fuel,self.path,self.cargament,self.moons,self.minerals_moons=n,max_c,fuel,path,cargament,moons,minerals_moons
    def __hash__(self):
        return hash((self.path))# in every problem the state is define by the path
    
    def isValid(self):
        return ((len(self.path)==0 
                or (self.fuel>=self.moon_r[self.path[-1]]) )
                and self.cargament<=self.max_c
               )
    def is_Full(self):
        return self.cargament==self.max_c
    def __repr__(self):
        return '''Fuel:{} ,Moons {},cargament:{},valid:{},max_c:  {}'''.format(
                self.fuel,self.path,self.cargament,self.isValid(),self.max_c)
    
    def get(self):
        m = (self.minerals_moons[list(self.path)])
        #m[-1] = min(m[-1],self.max_c-m.sum()+m[-1])
        ans=[]
        to_fill=self.max_c
        for i in m:
            if i>=to_fill:
                ans.append(to_fill)
                to_fill=0
            else:
                ans.append(i)
                to_fill-=i
        out=[]
        for i in self.moons:
            if i in self.path:
                out.append(ans[self.path.index(i)])
            else :
                out.append('None')
        if len(ans)==0:
            return ['None']
        return sorted(ans)
    
    def parser(self):
        return 'Case #{}: {}'.format('{}',' '.join(map(str,self.get())))
    
def dist(X,Y):
    R1,Theta1 = X 
    R2,Theta2 = Y
    return np.sqrt(R1**2 + R2**2 - 2*R1*R2*np.cos(Theta1 - Theta2))

def childrens(State):
    self=State
    respath = set(self.moons)-set(self.path)
    if len(self.path)>0:
        actual_moon = self.path[-1]
        distances = {m:dist((self.moon_r[m],self.pos[self.n,m]),(self.moon_r[actual_moon],self.pos[self.n,actual_moon]))
                     for m in respath}
    else:
        distances=dict(zip(range(1000),self.moon_r))
    cargaments = {m:(self.cargament+self.minerals_moons[m]) for m in self.moons}
    return {
        m:state(self.n+1,self.max_c,self.fuel-distances[m],self.path+(m,),cargaments[m],self.moons,self.pos,
                
                self.minerals_moons,
               self.moon_r
               )
        #self,n,max_c,fuel,path,cargament,moons,pos,minerals_moons
        #        ,moon_r
        for m in respath
    }

def parser(It#->input part of a problem (iterator)
          ):
    M = int(next(It))
    moons = set(range(M))
    moon_r = np.array(list(map(float,next(It).split())),dtype=float)
    R = np.array(list(map(float,next(It).split())),dtype=float)
    V = (6*tau)/np.array(list(map(float,next(It).split())),dtype=float)#ti
    
    Theta= np.array(tuple(V*i+R for i in moons))
    minerals_moons=np.array(list(map(int,next(It).split())),dtype=int)#ui
    Cargament=int(next(It))
    fuel = float(next(It))
    State=state(n=0,
                max_c=Cargament,
                fuel=fuel,
                path=(),
                cargament=0,moons=moons,pos=Theta
                ,minerals_moons=minerals_moons
                ,moon_r=moon_r)
    rec_min = max(bfs_paths(State),key=lambda self:(self.cargament,self.fuel))
    
    return rec_min

def main():
    import sys
    N = sys.stdin
    for i in range(int(next(N))):
        print(parser(N).parser().format(i+1))
        
def bfs_paths(start):
    queue = [(start)]
    see_path ={}
    while queue:
        (node) = queue.pop(0)
        yield node
        
        for next in childrens(node).values():
            set_path = tuple(sorted(next.path[:-1] ))+next.path[-1:]
            if set_path in see_path and see_path[set_path]>=next.fuel:
                continue
            else:
                see_path[next.path]=next.fuel
            if (not next.is_Full()) and next.isValid():
                queue.append(next)
                
            elif next.isValid():
                yield next
                queue = []

main()
