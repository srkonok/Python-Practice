# #Exercise 1: Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
# print(list1[::-1])
# print(list1)

# # Exercise 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3=[i+j for i, j in (zip(list1,list2))]
# print(list3)#['My', 'name', 'is', 'Kelly']
# print(list(zip(list1,list2)))#[('M', 'y'), ('na', 'me'), ('i', 's'), ('Ke', 'lly')]

# # Exercise 3: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# new_list=list()
# for i in numbers:
#     new_list.append(i*i)
# #res=[n*n for n in numbers]
# print(new_list,res)

# # Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3=[i+j for i in list1 for j in list2]
# print(list3)#['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# # Exercise 5: Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x,y in zip(list1,list2[::-1]):
#     print(x, y)
# #10 400
# # 20 300
# # 30 200
# # 40 100

# # Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# # for name in list1:
# #     if not name:
# #         list1.remove(name)
# # print(list2)
# res=list(filter(None,list1))
# print(res)#['Mike', 'Emma', 'Kelly', 'Brad']


# #Exercise 7: Add new item to list after a specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # for num,value in enumerate(list1):
# #     print(num,value)
# #     if value==6000:
# #         list1.insert(num+1,7000)
# list1[2][2].append(7000)
# print(list1)#[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# #Exercise 8: Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


# # Exercise 9: Replace list’s item with new value if found
# list1 = [5, 10, 15, 20, 25, 50, 20]
# for index, value in enumerate(list1):
#     if value==20:
#         list1[index]=200
# print(list1)#[5, 10, 15, 200, 25, 50, 200]

# Exercise 10: Remove all occurrences of a specific item from a list.


list1 = [5, 20, 15, 20, 25, 50, 20]
# print(list(set(list1)))#[5, 15, 50, 20, 25]
res=[num for num in list1 if num!=20] 
print(res)
