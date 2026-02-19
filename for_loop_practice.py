# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# num  =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for x in num:
#     print(x)

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
chr =(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = int(input("Enter the number : "))
idx = 0
for el in chr:
    if (el == x):
        print("Number found at index",idx)
    idx+=1