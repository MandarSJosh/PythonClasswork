import numbers


name = input('Please enter your name ')

for i in name:
    print(i, end = "-")

upto_num = int(input("Enter the number of elements of the fibonacci sequence that you wish me to print: "))

a = 1
b = 1
if upto_num == 1:
    print("0")
elif upto_num == 2:
    print("0,1")    
else:
    print("0,1,1", end = ",")
    for i in range(2,upto_num-1):
        c = b + a
        a = b
        b = c
        print(f"{c}", end = ',')
    


