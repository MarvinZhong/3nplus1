def cycleLength(seed): #def cycleLength(seed)
    len = 1 #set len = 1
    while seed != 1: #while seed!=1
        if seed % 2 == 0: #seed is even
            seed = seed // 2 #seed = seed/2
        else: #seed is odd
            seed = seed * 3 + 1 #seed = 3*seed + 1
        len = len + 1 #len = len + 1
    return len #return len as the result of cycleLength(seed)
while True : #while there is more input
    data = input()
    if data == '' :
        break #stop
    max = 1 #set max = 1
    start,stop = list(map(int,data.split())) #read in start, stop
    begin, end = start,stop #set start, stop to begin, end
    if begin > end : #if begin > end
        begin,end=end,begin #set end,begin to begin,end
    seed = begin #set begin to seed
    while seed <= end : #for seed from start to stop
        cl = cycleLength(seed) #find the cycle length cl of seed,that is cl = cycleLength(seed)
        if cl > max : #if cl > max
            max = cl #set max + cl
        seed = seed + 1 #seed = seed + 1
    print(start, stop, max) #print out start, stop, max
