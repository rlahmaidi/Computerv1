from operator import add

# dic = {1:-1, 4: -1, 2: 1}
# sort = sorted(dic)
# print(sort)
# print(dic[sort[2]])


# name = "rc-hidlahm-idi-lidri+si"
# npos = 0
# dic = {}
# while npos < len(name):
#     npos = name.find('-',npos)
#     if npos == -1:
#         break
#     print("the value of npos is ", npos)
#     dic[npos] = -1
#     npos += 1

# print(dic)
# from math import sqrt

# print((sqrt(8) + 4)/ 4)
# print((2 - sqrt(2)) / 2)

# number = -1
# print(str(number))

# lst = [1,2,3] 
# lst = [i * (-1) for i in lst]
# print(lst)


name = 'rachid'
second_name = "lahmaidi"
text = "my first name is: {first}, and my second name is {second}"

print(text.format(first=name, second=second_name))