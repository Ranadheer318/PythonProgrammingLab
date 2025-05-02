l=[1,0,4,5,6]
def sorted(l):
    for i in range(1,len(l)):
        if(a[i]<a[i-1]):
            return False
    return True
a=sorted(l)
print(a)
