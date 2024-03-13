#bank
bank=[]
thisdict ={
        "name":"",
        "branch":"",
        "balance":0,
          }
while True:
    print("""1.Add Account,
        2.Add Amount
        3.Withdraw Amount
        4.Exit""")
    choise=(input("enter your choise"))
    if choise=='1':
        name=str(input('enter the  name'))
        branch=str(input('enter the  branch'))
        thisdict["name"]=name
        thisdict["branch"]=branch
        bank.append(thisdict.copy())
        print(bank)

    elif choise=='2':
        amount=str(input('account_name'))
        amount=int(input('add your amount'))
        thisdict["account_name"]=name
        thisdict["amount"]=amount
        bank.append(thisdict)
        print(bank)

    elif choise=='3':
        withdraw=int(input("enter your withdrawel amount"))
        thisdict["withdraw"]=withdraw
        bank.append(thisdict)
        print(bank)
    