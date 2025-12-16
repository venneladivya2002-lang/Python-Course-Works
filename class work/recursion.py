# a recursion function is a function that calls itself
#two important rules of recursion:
#1. base case:this stops tha recursion without this the function will call itself forever
#2. recursive case:this part where the function calls itself with a smaller/simpler value
'''
def countdown(n):
    if n==0:
        print('stop')
    else:
        print(n)
        countdown(n-1)
print(countdown(3))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
        

def sum(n):
    if n==0 or n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(10))
 
def multiply(a,b):
    if b==0:
        return 0
    else:
        return a+multiply(a,b-1)
print(multiply(2,3))

def subtraction(a,b):
    if b==0:
        return a
    else:
        return subtraction(a-1,b-1)
print(subtraction(10,5))

b=(lambda a,b:a+b)
print(b(3,2))

#print list:

def print_list(lst, i=0):
    if i == len(lst):
        return
    print(lst[i])
    print_list(lst, i + 1)
print(print_list([10,20,30]))

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(4))
'''

        


    
