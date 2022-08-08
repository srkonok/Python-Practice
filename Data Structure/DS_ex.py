# #Exercise 1: Create a list by picking an odd-index items from the
# # first list and even index items from the second
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# res1=l1[1::2]
# res2=l2[0::2]
# fres=[*res1,*res2]
# print(f"Element at odd-index positions from list one{res1} \n Element at even-index positions from list two {res2}\n Printing Final third list{fres} ")

# Exercise 2: Remove and add item in a list
# list1 = [54, 44, 27, 79, 91, 41]
# x = list1.pop(4)
# print(f"List After removing element at index 4 {list1}")
# list1.append(33)
# list1.insert(2, 90)
# print(f"List after Adding element at index 2 {list1}")

# # Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# n=int(len(sample_list)/3)
# s=0
# e=n
# for i in range(3):
#     indexes=slice(s,e)
#     list_chunk=sample_list[indexes]
#     print("Chunks:",i,list_chunk)
#     s=e
#     e+=n
#     print(list_chunk[::-1])

# # Exercise 4: Count the occurrence of each element from a list
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# num_freq = {}
# for num in sample_list:
#     if num in num_freq:
#         num_freq[num] += 1
#     else:
#       num_freq[num] = 1
# print(f"Printing count of each item {num_freq}")

# #Exercise 5: Create a Python set such that it shows the element from both lists in a pair
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# res=zip(first_list,second_list) 
# print(set(res))

# #Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
# res=first_set.intersection(second_set)
# res2=first_set -res
# print(res)
# print(res2)

# #Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# first_set = {57, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
# print( first_set.issubset(second_set))
# print(second_set.issubset(first_set))
# print(first_set.issuperset(second_set))
# print(second_set.issuperset(first_set))
# if first_set.issubset(second_set):
#     first_set.clear()
# if second_set.issubset(first_set):
#     second_set.clear()
# print("First Set ", first_set)
# print("Second Set ", second_set)

# #Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# # for key,value in sample_dict.items():
# #     if value not in roll_number:
# #         roll_number.remove(value)
# temp=[]
# print(sample_dict.values())
# for x in roll_number:
#     if x in sample_dict.values():
#         temp.append(x)
# roll_number=temp
# print(roll_number)

# #Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# list1=list()
# for key,value in speed.items():
#     if value not in list1:
#         list1.append(value)
# print(list1) 

#Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print(max(sample_list))
print(max(tuple(list(set(sample_list)))))
