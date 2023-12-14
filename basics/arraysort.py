import array as Array
# Array bubble sort

x=int(input("Enter max number to be given"))
random = Array.array("i",[])
for i in range(x):
    random.append(int(input()))

print("Orignal Array",random)

for i in range(x):
    for j in range(x-1,0,-1):
        if random[j] < random[i]:
            temp = random[i]
            random[i] = random[j]
            random[j] = temp

print ("modified Array",random)
