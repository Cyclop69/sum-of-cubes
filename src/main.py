def sum_cubes(a):
  sum=0
  for i in range(1,a+1):
    sum=sum+(i**3)
  return sum
  
num=int(input("enter the number upto which u want the summation of cubes:\n"))
s=sum_cubes(num)
print("the sum is",s)
