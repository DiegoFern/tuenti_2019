from itertools import zip_longest
import numpy as np
from itertools import chain,groupby
ans4=[]


for i in chain(range(48,123)):
    for j in chain(range(48,123)):
        for k in chain(range(48,123)):
            for l in chain(range(48,123)):
                ans4.append((l,k,j,i,np.int8(l+k+i+j)))
ans4={k:min(map(lambda x:x[:4],v)) for k,v in groupby(sorted(ans4,key=lambda x:x[-1]),lambda x:x[-1])}
ans3=[]


for i in chain(range(48,123)):
    for j in chain(range(48,123)):
        for l in chain(range(48,123)):
                ans3.append((l,j,i,np.int8(l+i+j)))
ans3={k:min(map(lambda x:x[:3],v)) for k,v in groupby(sorted(ans3,key=lambda x:x[-1]),lambda x:x[-1])}

ans2=[]
for i in chain(range(48,123)):
    for j in chain(range(48,123)):
        ans2.append((j,i,np.int8(i+j)))
ans2={k:min(map(lambda x:x[:2],v)) for k,v in groupby(sorted(ans2,key=lambda x:x[-1]),lambda x:x[-1])}


ans1=[]
for i in chain(range(48,123)):
    ans1.append((i,np.int8(i)))
ans1={k:min(map(lambda x:x[:1],v)) for k,v in groupby(sorted(ans1,key=lambda x:x[-1]),lambda x:x[-1])}

all_ans={1:ans1,2:ans2,3:ans3,4:ans4,0:{}}
def sigma(xs):
    return xs[sigma.permut]

def pow_(f,l,xs):
    x=xs
    for i in range(l%16):
        x=f(x)
    return x

def hash_uniq(x):
    if x==0:
        return np.zeros(16,np.int8)
    xs = np.zeros(16,np.int8)
    xs[0] = bytes(x,'ISO_8859_1')[0]
    return xs

sigma.permut=((-1+np.arange(0,16))%16)[::]
def get_hash(text):
    if len(text)==0:
        return np.zeros(16,np.int8)
    return hash_uniq(text[0])+sigma(get_hash(text[1:]))


def get_unhash(hash_,len_):
    a=[]
    for i in hash_:
        try:
            a.append(all_ans[math.ceil((len_)/16)][i])
        except Exception as a:
            raise a
        len_=len_-1
    estandar_len=len(a[0])
    D=list(chain(*zip_longest(*a)))
    
    a=list(map(chr,filter(lambda x: x is not None ,D)))
    return a

def solver(text1,text2,I):
    T1A,T1B=text2.split('------')
    T1A,T1B=T1A+'---','---'+T1B
    target_hash=get_hash(text1)
    deltha=(target_hash)-(
    get_hash(list(T1A)
          +[0]*I
          +list(T1B))
    )
    hash_=(pow_(sigma,-len(T1A),deltha))
    return ''.join(get_unhash(hash_,I))
N=open('testInput.txt','r')
def main():
    import sys
    with open('testOutput.txt','w') as f:
        for i in range(int(next(N))):
            s=None
            t1=''
            for k in range(int(next(N))):
                t1+=next(N).strip()
            t2=''
            for k in range(int(next(N))):
                t2+=next(N).strip()
            print(t1)
            print(t2)
            c=True
            for K in range(70):
                try:
                    s=solver(t1,t2,K)
                    c=False
                    break
                except:
                    pass
                if not c:
                    break
            print(K)
            A,B=t2.split('------')
            A=A+'---'
            B='---'+B
            print('Case #{}: {}'.format(i+1,s),file=f)
main()
ans1=[]
for i in chain(range(48,123)):
    ans1.append((i,np.int8(i)))
ans1={k:min(map(lambda x:x[:1],v)) for k,v in groupby(sorted(ans1,key=lambda x:x[-1]),lambda x:x[-1])}

all_ans={1:ans1,2:ans2,3:ans3,4:ans4,0:{}}

def get_unhash(hash_,len_):
    a=[]
    for i in hash_:
        print((len_)/16)
        a.append(all_ans[math.ceil((len_)/16)][i])
        
        len_=len_-1
    estandar_len=len(a[0])
    
    a=list(map(chr,filter(lambda x: x is not None ,chain(*zip_longest(*a)))))
    return a

def solver(text1,text2,I):
    T1A,T1B=text1.split('------')
    T1A,T1B=T1A+'---','---'+T1B
    target_hash=get_hash(text2)
    deltha=(target_hash)-(
    get_hash(list(T1A)
          +[0]*I
          +list(T1B))
    )
    hash_=(pow_(sigma,-len(T1A),G))
    return ''.join(get_unhash(hash_,I))

def main():
    import sys
    N= sys.stdin
    for i in range(int(next(N))):
        s=None
        t1=''
        for k in range(int(next(N))):
            t1+=next(N).strip()
        t2=''
        for k in range(int(next(N))):
            t2+=next(N).strip()
        for _ in range(64):
            try:
                s=solver(t1,t2,i)
                break
            except Exception as e:
                print(e)
        print('Case {}: {}'.format(i,s))
main()
