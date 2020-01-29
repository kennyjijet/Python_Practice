
""""
///////
3,4 
abababb

abbabba ????

4,2
aabaab

2,4
abbabb

5,4

aabbaabba -> they need aabbaabba
aabaababb

4,4
aabbaabb

4,2
aabaab

///////


 if isA:
            if (aLen - bLen) == -1:
                strMade += 'a'
                index -= 1
            else:
                strMade += 'aa'
                index -= 2
            isA = False
        
        else:
            if (bLen - aLen) == 1:
                strMade += 'b'
                index -= 1
            else:
                strMade += 'bb'
                index -= 2
            isA = True


1,2
abb
3,2
aabba

4,2
aabaab ???
ababaa ???




2 4
abab
6,4
aabbaabbaa

8,4
aabbaabbaaaa -> error


4,4
aabbaabb
1,4
-> error

2,4
abbabb



3,4
aabbabb ????

#wordArr = [word[i:i+2] for i in range(0, len(word), 2)]
    #sortedArr = wordArr.sort()
    #print()
    #return [word[i:i+2] for i in range(0, len(word), 3)]
    myStr = ''
    while 
    a = 'a' * 2
    return a
if(index % 2 == 0):
            wordsAB += 'b'
        else:
            wordsAB += 'a'
        index += 1

    aabbaa
    abababb


while index > 0:
        if isA:
            if aLen == 0:
                isA = False
                continue
            
            if (aLen - bLen) <= -1:
                strMade += 'a'
                aLen -= 1
                index -= 1
            
            elif (aLen - bLen) == 0:
                strMade += 'aa'
                aLen -= 2
                index -= 2
            
            elif (aLen - bLen) >= 1:
                strMade += 'aa'
                aLen -= 2
                index -= 2
            isA = False
        else:
            if bLen == 0:
                isA = True
                continue
            if (bLen - aLen) <= -1:
                strMade += 'bb'
                bLen -= 2
                index -= 2
            
            elif (bLen - aLen) == 0:
                strMade += 'bb'
                bLen -= 2
                index -= 2
            
            elif (bLen - aLen) >= 1:
                strMade += 'b'
                bLen -= 1
                index -= 1
            isA = True

        print('aLen', aLen)
        print('bLen', bLen)
        print('strMade', strMade)
        print('index', index)
        
if a > b:
        while index > 0:
            if isA:
                if aLen == 0:
                    isA = False
                    continue
                if aLen >= 2:
                    strMade += 'aa'
                    aLen -= 2
                    index -= 2
                else:
                    strMade += 'a'
                    aLen -= 1
                    index -= 1
                isA = False 
            else:
                if bLen == 0:
                    isA = True
                    continue
                if bLen >= 2:
                    strMade += 'bb'
                    bLen -= 2
                    index -= 2
                else:
                    strMade += 'b'
                    bLen -= 1
                    index -= 1
                isA = True 
    elif a == b:
        while index > 0:
            if isA:
                if aLen == 0:
                    isA = False
                    continue
                strMade += 'aa'
                aLen -= 2
                index -= 2
                isA = False
            else:
                if bLen == 0:
                    isA = True
                    continue
                strMade += 'bb'
                bLen -= 2
                index -= 2
                isA = True
    else:
        while index > 0:
            if isA:
                if aLen == 0:
                    isA = False
                    continue
                if (aLen - bLen) <= -1:
                    strMade += 'a'
                    aLen -= 1
                    index -= 1
                elif (aLen - bLen) == 0:
                    strMade += 'aa'
                    aLen -= 2
                    index -= 2
            
                elif (aLen - bLen) >= 1:
                    strMade += 'aa'
                    aLen -= 2
                    index -= 2
                isA = False
            else:
                if bLen == 0:
                    isA = True
                    continue
                if (bLen - aLen) <= -1:
                    strMade += 'bb'
                    bLen -= 2
                    index -= 2
            
                elif (bLen - aLen) == 0:
                    strMade += 'bb'
                    bLen -= 2
                    index -= 2
            
                elif (bLen - aLen) >= 1:
                    strMade += 'b'
                    bLen -= 1
                    index -= 1
                isA = True
"""