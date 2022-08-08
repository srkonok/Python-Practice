# #Exercise 1A: Create a string made of the first, middle and last character

# str="Konok"
# n=len(str)
# res=str[0]+str[int(n/2)]+str[n-1]
# print(res)

# # Exercise 1B: Create a string made of the middle three characters
# str1 = "JhonDipPeta"
# m=int(len(str1)/2)
# print(str1[m-1:m+2])

#Exercise 10: Write a program to count occurrences of all characters within a string
str= "i am a python programmer"
list1=[*str]
print(list1)
dic1=dict()
for i in list1:
	if i in dic1:
		dic1[i]+=1
	else:
		dic1[i]=1
print(dic1)


print(min(dic1,key=dic1.get))