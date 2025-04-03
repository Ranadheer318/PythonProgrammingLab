def credit(bal,amount):
    bal=bal+amount
    return bal
def debit(bal,amount):
    bal=bal-amount 
    return bal
def checkbal(bal):
    print(bal)




bal=0
bal=credit(bal,5000)
bal=debit(bal,1500)
checkbal(bal)
