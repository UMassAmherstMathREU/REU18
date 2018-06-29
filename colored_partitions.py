#This partitions function was taken from https://stackoverflow.com/questions/5384570/whats-the-shortest-way-to-count-the-number-of-items-in-a-generator-iterator
def partitions(n, I=1):
    yield [n,]
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield [i,] + p

def colorPartitions(n):
    #black and white count the total black and white squares for the partition
    black = 0
    white = 0
    #black and white matrix will count the number of black and white squares per partition
    whiteMatrix = 0
    blackMatrix = 0
    q = 0
    lenPart = 0
    #find the length of the partitions
    for x in partitions(n):
        lenPart += 1
    #fill an array of length equal to the number of partitions with all 0's
    bigArray = [0,]*lenPart
    coefficent = [0,]*lenPart
    #now go into the array and fill each position with a partition
    for x in partitions(n):
        bigArray[q] = x
        q += 1
    #make a new array of all 0's with size equal to the number of partitions
    bigArrayPart2 = [0,]*lenPart
    part2Index = 0
    for part in bigArray:
        #make an array with all 0's of size equal to a specific partition
        grandArray = [0,]*len(part)
        for elementIndex in range(0, len(part)):
            #make a small array filled with 0's of size equal to 
            smallArray = [0,]*part[elementIndex]
            grandArray[len(part) - 1 - elementIndex] = smallArray
        part = grandArray
        bigArrayPart2[part2Index] = part
        part2Index += 1
    #this part "colors" our partitions, 1 for white squares and 0 for black squares
    coeff = 0
    #array to fit the number of white squares per partition
    newArray = []
    #array to fit the number of black squares per partition
    newArray2 = []
    #create the checkerboard partitions
    for part in bigArrayPart2:
        for x in range(0,len(part)):
            for y in range(0, len(part[x])):
                if (x + y) % 2 == 0:
                    part[x][y] = 1
                    white += 1
                    whiteMatrix += 1
                else:
                    black +=1
                    blackMatrix +=1
        #appends the number of white/black squares 
        newArray.append([whiteMatrix])
        newArray2.append([blackMatrix])
        #reset the black and white matrix to 0 for the new partition
        whiteMatrix = 0
        blackMatrix = 0
    j = 1
    i = 0
    #counts the number of times a certain number of white squares appears
    while i < len(newArray):
        if(newArray.count([j]) != 0):
            print("The number of times ", j, "appears in the white array is ", newArray.count([j]))
            j += 1
            i += 1
        else:
            j += 1
            i += 1    
    print("And now for the number of times a number appears in the black squares")
    l = 1
    k = 0    
    #counts the number of times a certain number of black squares appears
    while k < len(newArray2):
        if(newArray2.count([l]) != 0):
            print("The number of times ", l, "appears in the black array is ", newArray2.count([l]))
            l += 1
            k += 1
        else:
            l += 1
            k += 1
    #number of times a white square appears in a partition
    print(newArray)
    #number of times a black square appears in a partition
    print(newArray2)
    #all checkerboard partitions of n
    print(bigArrayPart2)
    print("the number of white squares is", white)
    print("the number of black squares is", black)     
