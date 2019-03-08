

def ex1():
    codes= {1144:4000,1254:8200,1256:92000,1908:-400,8523:-9800,3436:78000,1311:0} # Key - secret code , Value- amount of money in the account
    Exit=0
    while(Exit==0):
        code=int(input("Enter secret code"))
        if(codes.get(code)!=None):
            option=input("Enter A-Bank balance B-Cash withrawal C-Change secret code D-Exit")

            if(option=='A'):
                print(codes.get(code))
            if(option=='B'):
                amount=int(input("Enter the amount to withrawal"))
                dic={code:codes.get(code)-amount}
                codes.update(dic)
                print("cash withrawal completed")
            if(option=='C'):
                newcode=int(input("Enter new secret code"))
                if(codes.get(newcode)==None):
                    amount=codes.get(code)
                    del codes[code]
                    dic={newcode:amount}
                    codes.update(dic)
                    print("Change secret code completed")
                else:
                    print("Unvaild code")
            if(option=='D'):
                Exit=1
        else:
            print("The code does not exist in the system or the code isn't valid")
            Exit=1
ex1()



