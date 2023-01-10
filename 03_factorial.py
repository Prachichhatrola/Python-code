# #n! = 1*2*3*4
# n=0
# product = 1
# for i in range(n):
#     product=product*(i+1)
# print(product)    

from math import factorial


def factorial_liter(n):
    product = 1
    for i in range(n):
     product=product*(i+1)
    return product 

def factorial_recursive(n):
    
    if n==1 or n==0:
     return 1
    return n * factorial_recursiv(n-1)
# f = factorial_iter(5)
f=factorial_recursive(0)
print(f)