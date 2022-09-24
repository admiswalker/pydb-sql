#import sys

def LT2L(LT):
    # convert ListTuple2List

    v_ret=[]
    
    for T in LT:
        for s in T:
            v_ret.append(s)
    
    return v_ret

