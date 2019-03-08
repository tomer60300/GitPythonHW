

def ex4(id):

    mask=[0,2,1]
    tempmask=2
    sum=0
    i=0
    while(i<8):
        num=int(id[i])
        sum+=numop(num*mask[tempmask])
        tempmask=mask[tempmask]
        i=i+1
    print(sum)
    return int(sum/10) *10 +10 - sum


def numop(num):
    if(num>9):
        return int(num%10) + int(num/10)
    return num




print(ex4("54372042"))
