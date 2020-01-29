import math

def compute_gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return compute_gcd(b,a%b)


def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

#return heads
def countDogs(heads, legs): 
    temp = legs - (heads * 2)
    dogs = temp / 2
    return dogs

def farms (heads, legs):
    
    
    #print(compute_gcd(heads,legs))
    #if ((legs / 4) + ((legs / 2) - heads)) != heads:
    #    print("Error")
    #    return

    #print(math.gcd(heads, legs))


    #print((legs / 4), 'Birds') #birds
    #print((legs / 2), 'Dogs') ## get dogs
    dogs = countDogs(heads, legs) 

    print("Birds =", heads - dogs) 
    print("Dogs =", dogs) 





if __name__ == "__main__":
   
    farms(35,94)

    
    # 35 heads 94 legs -> find birds and dogs
    # Birds Dogs heads 35 legs 94
    # how many birds and dogs in this farm.

"""
# Python 3 implementation of above approach 
  
# Function that calculates Rabbits 
def countRabbits(Heads, Legs): 
    count = 0
  
    count = (Legs) - 2 * (Heads) 
    count = count / 2
  
    return count 
  
# Driver code 
if __name__ == '__main__': 
    Heads = 100
    Legs = 300
  
    Rabbits = countRabbits(Heads, Legs) 
  
    print("Rabbits =", Rabbits) 
    print("Pigeons =", Heads - Rabbits) 
  
# This code is contributed  
# by Surendra_Gangwar 
"""