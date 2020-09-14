# Program to print all positive numbers in a list

choice = 'y'
while choice=='y' or choice=='Y':
  listA = []
  listB = []
  num = int(input("Enter number of elements in list: "))
  for i in range(0, num):
    element = int(input("Enter element: " ))
    listA.append(element)
  i = 0
  for i in listA:
    if i>0:
      listB.append(i)
    else:
      continue
  print("Even numbers in given list: ")
  i = 0
  for i in listB:
    print(i)
  choice = str(input(" Do you wish to continue? Y/N: "))
print("End of program.")