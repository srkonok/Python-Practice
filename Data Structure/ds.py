# # String
# str="Python Programming"
# print(len(str))
# print(str[-1])
# print(str[0:3])
# print(str[0:-1])
# import math
# print(math.ceil(2.2))

# x=input("x:")
# y=int(x)+1
# print(f"x:{x}, y:{y}")

# #LOOP
# x = 1
# for i in range (5):
#     x+=i;
# print(x)

# #xargs
# def multiply(*numbers):
#     total=1
#     for num in numbers:
#         total *=num;
#     return total
# ad=[2,3,4,5]
# print(multiply(*ad))

# chars =list("Hellos")
# print(chars)
# print(chars.append('y'))

# #Finding an item
# numbers=["a","b","c"]
# if "d" in numbers:
#     print(numbers.index("d"))

# # Sorting List
# numbers = [5, 2, 8, 1, 9, 3]
# SN = sorted(numbers,reverse=True)
# print(numbers)
# print(SN)

# items = [
#     ("pdct1", 10),
#     ("pdct2", 9),
#     ("pdct3", 12),
# ]


# # def sort_item(item):
# #     return item[1]


# # items.sort(key=lambda item: item[1])
# # print(items)
# # Tuple to make list
# prices=list(map(lambda item:item[1],items))
# print(prices)

# bs = []
# # print(bs.pop())
# # bs.append(4)
# if not bs:
#     print("Empty")

# #Queue
# from collections import deque
# queue=deque([])
# queue.append(4)
# print(queue.popleft())

# tp="Konok"
# print(type(tp))

# #array creation

# from array import array

# arr.remove(2)
# arr=array("i",[5,2,4])
# print(arr)

# values=[x*2 for x in range(5)]
# print(values)
str = "This is a common interview question"
listStr = [*str]
print(listStr)
count = 0
values = {}
for x in listStr:
    values[x] = 0
for x in listStr:
    values[x] += 1
# print(values)
# print(max(values,key=values.get))

cf = sorted(values.items(), key=lambda kv: kv[1], reverse=True)
print(cf[0])
