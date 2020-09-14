# Fibonacci series
limit = int(input("Enter number of elements you want to see (integer values only): "))
if limit==0:
  print("You have chosen 0 number of elements to display.")
elif limit==1:
  print("Fibonacci series: 0")
elif limit==2:
  print("Fibonacci series: 0 1")
elif limit>= 3:
  a = 1
  b = 1
  i = 4
  print("Fibonacci series: 0")
  print("\t\t ", a)
  print("\t\t ", b)
  while i<=limit:
    b = a+b
    print("\t\t ", b)
    i = i+1
    if(i<=limit):
      a = a+b
      print("\t\t ", a)
      i = i+1
    else:
      break
else:
  print("Incorrect input. Program terminated.")
