#game banayga apan
import random
n= random.randint(1,100)
'''number guess kr 10 chance h tere paas'''

i=7
while(True and i>0):
    print("enter your number: ")
    num=int(input())
    if num==n:
        print("congo bhai tu jeet gya ptta nhi kaise itna acha guess krte ho")
        break
    elif num >n:
        print("iss seh chota number daal bhai")
    else:
        print("iss seh baada number daal re baba")
        i=i-1
        print("tere paas bus ",i,"chances h ree...baba")
        if(i==0):
            print("game khatm haar gya fer try kr re baba...")
            break





    
