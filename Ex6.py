




def double(x):
    return x*2


def Map(f,list):
    i=0
    while i<len(list):
        list[i]=f(list[i])
        i+=1
    i=0
    while i<len(list):
        print(list[i])
        i+=1





list=[1,2,3,4,5]
Map(double,list)






