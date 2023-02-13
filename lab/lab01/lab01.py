"""Lab 1: Expressions and Control Structures"""
#Q3
'''
def both_positive(x, y):
    if x > 0 and y > 0:
        print('x and y are both positive')
        return
    else:
        print('not true')
        return
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    # return x and y > 0 # You can replace this line!
both_positive(1,0)

'''

#Q4
def sum_digits(n):
    while n < 1000 :

        a = n % 10 
        b = (n % 100 - a) / 10
        c = (n % 1000 - 10 * b - a) / 100

        t = a + b + c
        print(t)
        return t
sum_digits(999)
   
'''
 Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
 "*** YOUR CODE HERE ***"

'''
