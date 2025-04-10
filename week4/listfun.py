n1=int(input("Enter the size of List 1:"))
n2=int(input("Enter the size of List 2:"))
n3=int(input("Enter the size of List 3:"))



def createlist(l,n):
    for i in range(n):
        temp=int(input("enter the element in list"))
        l.append(temp)
    for i in l:
        print(i)
    return(l)    



    
l1=[]
l2=[]
l3=[]
l1=createlist(l1,n1)
l2=createlist(l2,n2)
l3=createlist(l3,n3)
    


