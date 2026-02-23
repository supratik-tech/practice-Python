#multiplication table of a number except 5
n = int(input("Enter the number: "))
multiplication = 1
for i in range(1,11):
    if i == 5:
        continue
    print(f"{n} x {i} = ",n*i)

  
