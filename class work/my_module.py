'''modules:a module in python is a file that contain pyhon code such as functions,variables,or classes,which can be imported and used in another program
why need module:
    code reusability
    avoid repeating the same code
    to keep the pragram clean and organized
#user defined module:
'''
def welcome(name):
    return f'hello {name},welcome to python'

def simple_intrest(p,r,t):
    return (p*r*t)/100
    
def upper_text(text):
    return text.upper()

def max_num(numbers):
    return max(numbers)
    
def reverse_num(numbers):
    return numbers[::-1]

def check_login(username,password):
    if (username ,password)==('Divya','1234'):
        return 'login succsuful'
    else:
        return 'invalid credentials'

def total(m1,m2,m3):
    return m1+m2+m3
def percentage(m1,m2,m3):
    return m1+m2+m3/3
