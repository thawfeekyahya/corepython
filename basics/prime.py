# Find prime number till max user input

max=int(input("Enter the number upto find the prime numbers "))

for num in range(2,max+1):
    for i in range(2,num):
        if (num % i) == 0:
            break
        elif (i==num-1):
            print("The number is prime",num)
