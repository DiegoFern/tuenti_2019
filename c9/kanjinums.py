#pytthon 3
import itertools 
NUMS = ((0,''),
        (1, u"一"),
        (2, u"二"),
        (3, u"三"),
        (4, u"四"),
        (5, u"五"),
        (6, u"六"),
        (7, u"七"),
        (8, u"八"),
        (9, u"九"),
        (10,            u"十"),
        (100,           u"百"),
        (1000,          u"千"),
        (10000,         u"万"),
        (100000000,     u"億"),
        (1000000000000, u"兆"))

KANJIS = dict((kanji, num) for (num, kanji) in NUMS)

def _break_down_nums(nums):
    first, second, third, rest = nums[0], nums[1], nums[2], nums[3:]
    if first < third or third < second:
        return [first+second, third] + rest
    else:
        return [first, second*third] + rest

def kanji2num(kanji, enc="utf-8"):
    """
    Convert the kanji number to a Python integer.
    Supply `kanji` as a unicode string, or a byte string
    """
    kanji = (kanji)

    # get the string as list of numbers
    nums = [KANJIS[x] for x in kanji]

    num = 0
    while len(nums) > 1:
        first, second, rest = nums[0], nums[1], nums[2:]
        if second < first: # e.g. [10, 3, ...]
            if any(x > first for x in rest): # e.g. [500, 3, 10000, ...]
                nums = _break_down_nums(nums)
            else: # e.g. [500, 3, 10, ...]
                num += first
                nums = [second] + rest
        else: # e.g. [3, 10, ...]
            nums = [first*second] + rest

    return num + sum(nums)

def permutations(A):
    pos='十百千万'
    exp=[a for a in A if a in pos]
    exp=sorted(exp,key=lambda x:-KANJIS[x])
    mult=[a for a in A if a not in pos]
    mult.extend(['' for i in range(len(exp)+1-len(mult))])
    #print(' '.join(map(str,map(KANJIS.get,exp))),' '.join(map(str,map(KANJIS.get,mult))))
    def f(x,y):
        M,exp_list=x,y
        ans=0
        y =iter(y)
        for m,e in zip(x,y):
            ans+=(1 if e=='' else KANJIS[e])*KANJIS[m]
            if e=='' and m=='万':
                return None
            if e=='一' and m in '十百千':
                return None
        ans+=KANJIS[(next(y))]

        #print(list(map(KANJIS.get,ans)))
        return (ans)
    return set(filter(lambda x:x is not None ,map(f,itertools.repeat(exp),itertools.permutations(mult),)))
def main():
    import sys
    N=sys.stdin
    Sum ='+' 
    Prod='*'
    Sub='-'
    Div='/'
    for i in range(int(next(N))):
        Ak,Op,Bk,eq,Ck= next(N).strip().split()
        #if i+1 not in {6,7,5}:
        #    continue
        ##print('|'.join(map(str,map(KANJIS.get,Ak)),))
        #print('|'.join(map(str,map(KANJIS.get,Bk)),))
        #print('|'.join(map(str,map(KANJIS.get,Ck)),))
        # A Op B = C
        solved=False
        pA=(permutations(Ak))
        pB=(permutations(Bk))
        pC=(permutations(Ck))
        for A in pA:
            
            A =  (A)
            for B in pB:
                
                B =  (B)
                for C in (pC):
                    C =  (C)
                    for op,f in [
                        (Sum,lambda x,y:x+y),
                        (Prod,lambda x,y:x*y),
                        (Sub,lambda x,y:x-y),
                        ]:
                        if f(A,B)==C:
                            solved=True
                            print('Case #{}: {} {} {} = {}'.format(i+1,A,op,B,C,))
                            break
                    if solved:
                       break
                if solved:
                    break
            if solved:
                break
        #print('Case #{}: {} {} {} = {}'.format(i+1,A,op,B,C,))
main()
