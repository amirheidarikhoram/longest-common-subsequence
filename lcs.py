
def lcs (sel, i, j):
    if i >= 0 and j >= 0:    
        if sel == 'check':
            li, lj = i, j
            while second.find(first[i],0,lj+1) == -1 and i >= 0: i -= 1
            while first.find(second[j],0,li+1) == -1 and j >= 0: j -= 1
            if num(i,j) != 1:
                inear = lcs ('row',i-1,j)
                if inear == 'nf': inear = i
                jnear = lcs('col',i,j-1)
                if (jnear == 'nf'):jnear = j
                if inear == i and jnear == j: lcs('check',i-1,j-1)
                elif inear == i and jnear != j: lcs ('check',i,jnear)
                elif inear != i and jnear == j: lcs ('check',inear,j)
                else: lcs ('check',inear,j) if (inear+1)*(j+1) > (jnear+1)*(i+1) else lcs ('check',i,jnear)
            else:
                ans.append(first[i])
                lcs('check',i-1,j-1)
        elif sel == 'row':
            if i == 0 and num(i,j)!= 1: return ('nf' if num(i,j)!= 1 else 0) 
            else: return (i if num(i,j) == 1 else lcs ('row',i-1,j))
        elif sel == 'col':
            if j == 0: return ('nf' if num(i,j)!= 1 else 0) 
            else: return (j if num(i,j) == 1 else lcs ('col',i,j-1))
    else:
        if sel == 'row' or sel == 'col': return 0
        else: 
            ans.reverse()
            return 0

def num(i,j): return (1 if first[i] == second[j] else 0)

from sys import *

if len(argv) >= 2:
    first = argv[1]
    second = argv[2]
    ans=[]
    lcs('check',len(first)-1,len(second)-1)
    print(ans,' with length: ',len(ans))
else: print ('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')