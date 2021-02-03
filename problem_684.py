lst = [2, 2, 99]

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def my_reduce(lst, fun, initial):
    res = initial
    for val in lst:
      res = fun(res, val)
    return(res)

def sum(lst):
    return my_reduce(lst, add, 0)

def product(lst):
    return my_reduce(lst, multiply, 1)

result = product(lst)
print(result)
