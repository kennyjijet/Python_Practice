def sequence_ab(a,b):
    strMade = ""
    aLen = a
    bLen = b
    if abs(aLen - bLen) > 2:
        return "Error"
    index = (a+b)
    while index > 0:
        if (aLen - bLen) < 0:
            if (bLen - aLen) == 1: #Odd
                if aLen != 0:
                    strMade += 'a'
                    aLen -= 1
                    index -= 1

                strMade += 'b'
                bLen -= 1
                index -= 1

            if (bLen - aLen) == 2: #Even
                if aLen != 0:
                    strMade += 'a'
                    aLen -= 1
                    index -= 1

                strMade += 'bb'
                bLen -= 2
                index -= 2


        elif (aLen - bLen) == 0:
            strMade += 'aa'
            aLen -= 2
            index -= 2

            strMade += 'bb'
            bLen -= 2
            index -= 2

        elif (aLen - bLen) > 0: #2,0 5,4
            if aLen != 0:
                if aLen >= 2:
                    strMade += 'aa'
                    aLen -= 2
                    index -= 2
                else:
                    strMade += 'a'
                    aLen -= 1
                    index -= 1

            if bLen != 0:
                if bLen >= 2:
                    strMade += 'bb'
                    bLen -= 2
                    index -= 2
                else:
                    strMade += 'b'
                    bLen -= 1
                    index -= 1
    return strMade
    

if __name__ == "__main__":
    
    print(sequence_ab(3,4))
    #print(sequence_ab(2,1))
    #print(sequence_ab(2,0))
    #print(sequence_ab(1,0))
    
    #print(sequence_ab(4,4))
    #print(sequence_ab(5,4))
    #print(sequence_ab(4,2))
    #print(sequence_ab(2,4)) #Wrong
    
    
    
    
    #print(sequence_ab(3,4)) # 7 abababb
    #print(sequence_ab(5,4)) # 9

# 3 % 2 1