n = int(input("Enter your no. "))
flag = 0
i = 2
while (i < n):
    if(n%i == 0):
        flag =1
        break ;
    i+=1
if(flag == 1):
    print("This is not a prime number")
else:
    print("This is a prime number")

        