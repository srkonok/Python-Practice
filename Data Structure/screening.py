vowels = ['a', 'e', 'i', 'o', 'u']
str = input("Input string: ")
set1 = set()
for v in vowels:
    if v in str:
        set1.append(v)
    else:
        print(f"Not present {v}")
if (set1 == vowels):
    print(f"All vowel are present in {str}")
