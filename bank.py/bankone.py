bank=[]
for i in range(1):
    thisdict ={
        "name":"",
        "branch":"",
        "balance":0
    }
    name=str(input('enter the  name'))
    branch=str(input('enter the  branch'))
    thisdict["name"]=name
    thisdict["branch"]=branch
    bank.append(thisdict)
print(bank)
balance=int(input("balance"))
thisdict["balance"]=balance
bank.append(thisdict)
print(balance)

 