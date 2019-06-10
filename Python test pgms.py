import math

z=int(input("Enter a positive number to check for Fibonacci:"))

def sq_check(a):            
    x = int(math.sqrt(a))
    return x*x == a

def isFibonacci(b):
    return sq_check(5*b*b + 4) or sq_check(5*b*b - 4)
    
sq_check(z)

if(isFibonacci(z)==True):
   print("The number is Fibonacci")
else:
   print("The number is not part of Fibonacci")


#Prime number generator
import math
def prime_gen(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

b=list(filter(prime_gen, range(1,20)))
len(b)

for x in b:
    print(len(x))
    
    
print [x for x in range(1,100) if isprime(x)]



 












import math 
  
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
# A utility function to test above functions 
for i in range(1,11): 
     if (isFibonacci(i) == True): 
         print(i,"is a Fibonacci Number")
     else: 
         print(i,"is a not Fibonacci Number ")
         
         

age = input("What is your age? ")
print ("Your age is: ", age)
type(age)