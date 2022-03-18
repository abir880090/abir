def myfunc(num):
  numbers = []
  
  
  for i in range (1, 1+num):
    allElements =  num = int(input("Enter elements: "))
    numbers.append(allElements)
  even_list = []
  odd_list = []
  
  for j in numbers:
    if j % 2==0:
      even_list.append(j)
    else:
      odd_list.append(j)
      
  print("Even number list", even_list)
  print("Odd number list", odd_list)
num = int(input("Enter number of elements: ")) 
result=myfunc(int(num))
print(result)
      