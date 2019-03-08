


def ex4(str1):
    newstr=""
    j=0
    i=0
    while i<len(str1):
        newstr=newstr[:j] + str1[i] + newstr[j:]
        j+=1
        i+=1
        true=1
        count=1
        while(true) and (i<len(str1)):
            if(str1[i-1]==str1[i]):
                count+=1
                i+=1
            else:
                true=0
        newstr=newstr[:j] + count.__str__() + newstr[j:]

        j+=1

    print(newstr)






str="abcaadddcc"

ex4(str)
