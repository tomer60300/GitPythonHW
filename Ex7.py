
Cache={}


def kefelwithCache(x,y):


    cacheElement=(x,y)
    if(Cache.get(cacheElement)!= None):
        print("From mem")
        return Cache[cacheElement]

    Answer=x*y
    updated={cacheElement:Answer}
    Cache.update(updated)
    return Answer



print(kefelwithCache(4,7))
print(kefelwithCache(4,7))
