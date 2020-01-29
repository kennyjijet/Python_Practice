import random

def expr(depth):
    if depth==1 or random.random() < 1.0/(2**depth-1): 
        return str(int(random.randrange(1,100)))
    return expr(depth-1) + random.choice(['+','-','*','/']) + expr(depth-1)

while (True):
    #print expr(2)
    #print (eval(expr(2))
    expression = expr(4)
    result = eval(expression)
    if result == 100:
        print(expression)
        print(result)
        break
       
        


"""
from random import random, randint, choice
def Possibilities(randomNumber):
    # 1 + 2 + 34 - 5 + 67 - 8 + 9 =100 -> 
    #possibility to put + - or nothing to get 100 python generate expression by random and result sould be 100.
    x = random.randint(1,100)

    return x



if __name__ == "__main__":
    print(Possibilities(100))
    #print(Possibilities(100), end="")
"""