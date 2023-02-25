#Q1
'''
lambda x: x  # A lambda expression with one parameter x
# Function

a = lambda x: x  # Assigning the lambda function to the name a
a(5)
# 5

(lambda: 3)()  # Using a lambda expression as an operator in a call exp.
# 3

b = lambda x: lambda: x  # Lambdas can return other lambdas!
c = b(88)
c
# Function

c()
# 88

d = lambda f: f(4)  # They can have functions as arguments as well.
def square(x):
    return x * x
d(square)
# Error

z = 3
e = lambda x: lambda y: lambda: x + y + z
e(0)(1)()
# 4

f = lambda z: x + z
f(3)
# Error

higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(2)(g)  # Which argument belongs to which function call?
# Error

higher_order_lambda(g)(2)
# 4

call_thrice = lambda f: lambda x: f(f(f(x)))
call_thrice(lambda y: y + 1)(0)
# 3

print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
print_lambda
# Function

one_thousand = print_lambda(1000)
# 1000

one_thousand
# None



# Q2

def even(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)
    return odd
steven = lambda x: x
stewart = even(steven)
stewart
# None

stewart(61)
# None

stewart(-4)
# None

def cake():
   print('beets')
   def pie():
       print('sweets')
       return 'cake'
   return pie
chocolate = cake()
# beets

chocolate
# beets

chocolate()
# beets
# sweets

more_chocolate, more_cake = chocolate(), cake
# beets
# sweets
# sweets

more_chocolate
# beets
# sweets
# sweets

def snake(x, y):
   if cake == more_cake:
       return lambda: x + y
   else:
       return x + y
snake(10, 20)
# None

snake(10, 20)()
# None

cake = 'cake'
snake(10, 20)
# None

'''

#Q3 """Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions

def lambda_curry2(func):

    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: func(x, y)


# Q4
n = 9
def make_adder(n):
    return lambda k: k + n
add_ten = make_adder(n+1)
result = add_ten(n)

# Q5
a = lambda x: x * 2 + 1
x = 3
def b(b, x):
    return b(x + a(x))

b(a, x)
# 21
