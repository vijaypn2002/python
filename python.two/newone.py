
b=[]
choice='y'
while  choice !='n':
    
    a=str(input('enter the word'))
    b.append(a)
    print(b)
    if choice=='n':
        b.pop(a)
    choice=str(input('y=add,n=remove (y/n)'))
    break



