#Perfect square chake
num = int(input("Enter the chaking number : "))

flag = False
i = 1
while(i*i)<= num:
    flag = True
    break;
    i+=1
    
if flag == False:
    print("This is a perfect square")
if flag == True:
    print("This is not a perfect square")