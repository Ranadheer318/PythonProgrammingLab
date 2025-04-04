


def credit(bal,amount,transactions):
    bal=bal+amount
    transactions.append(amount)
    return bal
def debit(bal,amount,transactions):
    bal=bal-amount 
    transactions.append(-amount)
    return bal
def checkbal(bal):
    print(bal)
def lasttransactions(transactions):
    for transaction in transactions:
        if transaction < 0:
            print("Debit ",transaction)
        else:
            print("Credit ",transaction)





bal=0
transactions=[]
bal=credit(bal,5000,transactions)
bal=debit(bal,1500,transactions)
checkbal(bal)
