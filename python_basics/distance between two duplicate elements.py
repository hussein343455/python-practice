def loope(x):
    for ind,val in enumerate(x):
        if x.count(val)==2:
            return len(x)-ind
x=[1,2,3,4,5,12,31,41,54,65,76,8,2]
print(loope(x))