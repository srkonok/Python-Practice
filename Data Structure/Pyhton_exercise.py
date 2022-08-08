# #Exercise 1: Create a list by picking an odd-index items from the 
# # first list and even index items from the second with higher order function
# def _odd(lst):
#     oddList = []
#     for index, letter in enumerate(lst):
#         if(index % 2 != 0):
#             oddList.append(letter)
#     return oddList


# def _even(lst):
#     evenList = []
#     for index, letter in enumerate(lst):
#         if(index % 2 == 0):
#             evenList.append(letter)
#     return evenList


# def result(lists, func):
#     rList = func(l1)
#     return rList


# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# res1=result(l1,_odd)
# res2=result(l2,_even)
# print(FinalList)
# print(f"Element at odd-index positions from list one \n {res1}")
# print(f"Element at even-index positions from list two \n {res2}")
# FinalList=[*res1,*res2]

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
res1=l1[1::2]
res2=l2[0::2]
fres=[*res1,*res2]
print(f"Element at odd-index positions from list one{res1} \n Element at even-index positions from list two {res2}\n Printing Final third list{fres} ")
