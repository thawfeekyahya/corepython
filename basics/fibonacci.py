# print fibonaci series

num=int(input("Enter the max number to find the fibnoaci series "))

res=0
n1,n2=0,1
prev=0

while res <= num:
   prev=n1
   res = n1 + n2
   print(res)
   n1 = res
   n2 = prev
