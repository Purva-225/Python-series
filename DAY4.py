"""FUNCTION AND RECURSION"""

# To reduce Redendency in the code we use function

def cal_sum(a,b):
    sum = a+b
    print(sum)
    return sum

cal_sum (406,5)
cal_sum (405,500)
cal_sum (404,5000)
cal_sum (403,50000)
cal_sum (402,500000)
cal_sum (401,500000)

"""Avg of 3 numbers"""

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(44, 55, 66)

"""WAF to print len of a list(list is parameter)"""
citie = ["gurgoan","pune","mumbai","dholakpur"]
food =["edli","sambar","dosa","chutney"]

def print_len(poorie):
    print(len(poorie))
    
print_len(food)
print_len(citie)


"""WAF to print elemt of a list in a single num"""

heroes = ["kjciwjb", "wjbwkhbw", "kjwebfkwba","kwjahfk"]

def print_len(md):
    print(len(md))

def print_len(md):
     for iterm in md:
       print(iterm, end= " ")
    
print_len(heroes)

"""WAF to find factorial of n"""
def cal_factorial(n):
     fact = 1
     for i in range(1,n+1):
        fact *= i
     print(fact)
    
cal_factorial(5)

"""WAF to convert USD to INR"""
def convert(USD_val):
    inr_val = USD_val * 83
    print(USD_val,"USD =", inr_val,"INR")
    
convert(10)

"""RECURSION"""
"""IF I WANR TO PRINT NUM FROM 5 TO 1"""

def show(n):
    if(n == 0):
        return 
    print(n)
    show(n -1)
    
show(5)

"""factorial"""
def factorial(n):
         if(n == 1 or n  == 0):
             return 1
         return factorial(n-1) * n
         
print(factorial(5))

"""WARF TO CAL SUM OF N NATURAL NUM"""
def sum(n):
      if(n == 0):
        return 0
      return sum(n-1) + n
    
hit = sum(5)
print(hit)

"""WARF to print all elem in a list"""
#hint: use list and idx as parameter

def print_list(list,idx=0):
      if(idx == len(list)):
             return 
      print(list[idx])
      print_list(list,idx+1)
      
fruits = ["mango", "banana", "gava", "litchi"]
print_list(fruits)
    
    
