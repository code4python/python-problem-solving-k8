# def reverse_number(n):
#     n_str = str(n)
#     if "-" in n_str:
#         n_str = n_str[1:]
#         n_str =  int("-" + n_str[::-1])
#     else:
#         n_str = int(n_str[::-1])
#     return n_str


# print(reverse_number(123))
# print(reverse_number(-123))
# print(reverse_number(1000))


# def solution(string):
#     string = str(string[::-1])
#     return string

# print(solution("world"))

# def count_sheeps(sheep):
#   # TODO May the force be with you
#     for sh in sheep:
#         res = []
#         res.append(sh)
#         sh += 1
#         print(bool[res] n)
      

# count_sheeps([1,2,0,0,0,0,111])

#############################################
#conbatebl number"""
# def get_factors(n):
#     factors =[]
#     for i in range(1 , n+1):
#         if n % i == 0:
#             factors.append(i)
#     return factors

# def are_coprime(n ,m):
#     n_fac = set(get_factors(n))   
#     m_fac = set(get_factors(m))   
#     return len(n_fac.intersection(m_fac))==1
# print(are_coprime(20,33))

#------------------end---------------------#



# Get Desmal part for geven number

# def get_desmal(n):
#     n_str = str(n)
#     n_part = n_str.split(".")
#     if len(n_part) == 1: return 0
#     return float("0."+ n_part[1])
# print(get_desmal(0.4))
# print(get_desmal(-2.5))


# get sum numbers:

# def get_sum(a,b):
#  return sum(range(min(a,b), max(a,b) + 1))
# print(get_sum(2,1))
# print(get_sum(4,4))
# print(get_sum(-2,4))
# print(get_sum(2,-8))

#+++authers
# def get_sum(a,b):
#     if a==b: return a
#     return sum(range(min(a,b), max(a,b) + 1))
# print(get_sum(2,2))
# print(get_sum(-2,-4))
# print(get_sum(-5,1))
# print(get_sum(-2,-4))
# print(get_sum(-2,-2))



# # sum 16 + 18 = 214

# def get_sum_advansed(a,b):
#     n1 = str(a)
#     n2 = str(b)
#     max_length= max(len(n1) , len(n2))
#     n1 = n1.rjust(max_length ,"0")
#     n2 = n2.rjust(max_length ,"0")
#     # ziping = list(zip(n1,n2))
#     tolels = [ int(d1) + int(d2) for d1,d2 in zip(n1 ,n2) ]
#     res= [ str(totel) for totel in tolels ]
#     return int("".join(res))

# print(get_sum_advansed(144522,4245))


# Numbers of Desmael Diget:

# def desmail_diget(n):
#     return len(str(n))

# print(desmail_diget(2325551234))
# print(desmail_diget(2555588))
# print(desmail_diget(25))


####################################################
#   Sum min number in list:

# def sum_min_n_in_list(n):

#     return sum(map(min, n))
    
# # print(sum_min_n_in_list([[1,2,2,3],[5,5,5,7,8], [10,50,20]]))

# =======================================================
# def get_fac(n):
#     n_str = str(n)
#     if "-" in n_str:
#         n_str = n_str[1:]
#         n_str = int("-" + n_str[::-1])
#     else:
#         n_str = int(n_str[::-1])
#     return n_str

# print(get_fac(11544552))
# print(get_fac(-5455))
# print(get_fac(10000000))


# Get Mien fo list:

# def get_mein(n):
#     return sum(n) / len(n)
# print(get_mein([6,6]))

#-------------------------------------------------

# Get Random Color in the list:

# import random 

# colors = ['red','yallow', 'black', 'white']
# def get_random_colors(c):
#     c= str(c)
#     for c in range(1,colors + 1):
#         random.choice(c)
#         print(c)

# get_random_colors(colors)


# Convert list to dicsenary:

# def conv(hash):
#     arr = [    ]
#     for key, value in hash.items():
#         arr.append([key,value])
#     return sorted(arr)

# print(conv({'name':'ahmed' ,'age':23, 'contey':'Sudan'}))

# cont of number in the list:

# def sort(n, xs):
#     return str(sorted(xs)[-n:])
# print(sort([1,2,2,4,5,1,2,3,3,]))


#================================================

# def sum_int_in_chat(s):
#     numbers = '123456789'
#     for l in s:
#         if l  not in numbers:
#             s = s.replace(l," ")
#     new_s = s.split()
#     nums =[]
#     for i in new_s:
#         if i != "":
#             nums.append(i)
#     return sum(int(x) for x in nums) 
# print(sum_int_in_chat('ggggg5ddgvfgb5frbb2g4vvv4vvv85vcvc4vd6d'))


# infinsed loop
# def infised_loop(n):
#     res = [] 
#     i = 1
#     while i <= n :
#         res.append(i)
#         i += 1

#     return res
# print(infised_loop(10))


#run any with bool equal true:
# def _if(bool, func1, func2):
#     if bool:
#         return func1()
#     else:
#         return func2()
# def hi():
#     print("hi")
# def py():
#     print("bry")
# _if(False,hi, py )


#catyears in hument:
# """ 
# if hument_years= 1 :
#     catyears = 9
#     dog_years = 15
# if humentyears = 2:
#     catyears = 9
#     dggyears = 14
# else:
#     catyeats = 4
#     dogyears = 5
#  """
# def get_homntyears(hument_years):
#     cat_years = 0
#     dog_years = 0
#     for year in range(1, hument_years +1):
#         if hument_years == 1 :
#             cat_years +=9
#             dog_years +=15
#         elif hument_years == 2:
#             cat_years +=9
#             dog_years +=14
#         else:
#             cat_years +=4
#             dog_years +=5
#     return [ hument_years , cat_years , dog_years ]
# print(get_homntyears(20))


# Sum prodcet in bay total or ane :
#--task:
#   n<5 : 100
#   n>=5 and n<10: 95
#   n >= 10 : 90

#  def  sum_total_in_disconut(item):
#     if item < 5:
#         return item * 100
#     elif item > 5 and item < 10:
#         return item * 95
#     else:
#         return item *90
# print(sum_total_in_disconut(7))
  
# def  sum_total_in_disconut(item):
#     return item * (100 if item < 5 else 95 if item >=5 and item < 10 else 95)
# print(sum_total_in_disconut(7))



# re

# import re 


# name = "Ahmed Abaker Haroun"

# res =  re.findall("\s" ,name)

# print(res)


# def max_int(a,b):
#     return max(a,b)

# print(max_int(5,8))
# print(max_int(5,-8))
# print(max_int(-5,-55))

import os

print(os.mkdir(''))