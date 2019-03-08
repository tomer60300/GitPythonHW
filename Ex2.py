
def ex2A():
    sum=0

    temp=input("Enter secret code")
    while(temp!="stop"):
        if(temp!="stop"):
            sum+=int(temp)
        temp=input("Enter secret code")

    print (sum)


def ex2A(str):
    sum=0
    list=str.split(',')
    i=0
    while(i<len(list)):
        sum+=int(list[i])
        i+=1
    print (sum)




ex2A("1,2,3,4")
