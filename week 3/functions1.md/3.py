def solve(numheads, numlegs):
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return j, i
numheads=35
numlegs=94
res=solve(numheads, numlegs)
print(res)