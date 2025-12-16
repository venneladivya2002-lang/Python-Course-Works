 #generators:
'''def count_up():
    for i in range(1,6):
        yield i
for x in count_up():
    print(x)
 #even nubers:   

def even_numbers(*numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number

for x in even_numbers(2, 3, 4, 6, 7, 8):
    print(x)
#square::
def square(n):
    for i in range(n,n+1):
        yield i*i
for x in square(4):
    print(x)
'''
#cube:
def gen_cube(n):
    for i in range(n,n+1):
        yield i**3
for x in gen_cube(3):
    print(x)

'''
#genarating characters:
def gen_ch(s):
    for ch in s:
        yield ch
for x in gen_ch('divya'):
    print(x)

#odd numbers:
def gen_odd():
    for i in range(1,11):
        if i%2!=0:
            yield i
for x in gen_odd():
    print(x)


def gen_word(sentance):
    for word in sentance.split():
        yield word
for x in gen_word("i love india"):
    print(x)

#fibonacci series:
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,b+a
for x in fibonacci(10):
    print(x)

#genarating dictionary value:
def dic_value_gen(d):
    for value in d.values():
        yield value
for x in dic_value_gen({'a':1,'b':2}):
    print(x)

#genarating dictionary keys:
def dic_keys_gen(d):
    for keys in d.keys():
        yield keys
for x in dic_keys_gen({'a':1,'b':2}):
    print(x)

#genarating dictionary items:
def dic_items_gen(d):
    for items in d.items():
        yield items
for x in dic_items_gen({'a':1,'b':2}):
    print(x)

#multiple:
def multiple(n):
    for i in range(1,11):
        yield i*n
for x in multiple(5):
    print(x)

#multiplication table:
def table(n):
    for i in range(1,11):
        yield n*i
for x in table(2):
    print(x)

# check vowel or not:
def vowel_gen(s):
    for ch in s:
        if ch.lower() in 'aeiou':
            yield ch
for x in vowel_gen('divya'):
    print(x)
    '''
#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        yield fact
for x in factorial(3):
    print(x)
        
    

    
    
    
