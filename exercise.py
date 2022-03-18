def myfunc(number):
  
  if number%2==0:
    return 'this is even'
  else:
    return 'this is odd'
    
num=int(input("Enter a number"))
result=myfunc(int(num))
print(result)