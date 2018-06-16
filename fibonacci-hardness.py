#!/usr/bin/python3

import re
from math import log,sqrt

logs5=log(sqrt(5))/log(10)
logphi=log((1+sqrt(5))/2)/log(10)

adj=[[15,4,8./15],[7,6,6./7],[5,4,4./5]]

ladj=[[21,6,12./21],[15,4,8./15],[6,4,2./3]]

f=open("fibonacci.txt")
for line in f:
    r = re.match(r'F([0-9]+)\W.*C([0-9]+)',line)
    if (r):
        n=int(r.group(1))
        gsz=int(r.group(2))
        ssz=logphi*n-logs5
        sdeg=6
# SNFS difficulty adjustments for different factors
        for p in adj:
            if (n%p[0]==0):
                sdeg=p[1]
                ssz=ssz*p[2]
                break
            
        print(["F",n,gsz,sdeg,ssz])

f=open("lucas.txt")
for line in f:
    r = re.match(r'L([0-9]+)\W.*C([0-9]+)',line)
    if (r):
        n=int(r.group(1))
        gsz=int(r.group(2))
        ssz=logphi*n
        sdeg=6
# SNFS difficulty adjustments for different factors
        for p in ladj:
            if (n%p[0]==0):
                sdeg=p[1]
                ssz=ssz*p[2]
                break
            
        print(["L",n,gsz,sdeg,ssz])

    