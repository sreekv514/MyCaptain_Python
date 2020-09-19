# Program to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

import operator

def StrToSet(x):
	"Sorts the string as individual alphabets into a set to avoid duplicates"
	xset = set()
	for i in x:
		xset.add(i)
	xset = sorted(xset)
	return xset

def most_frequent(x, set_x, dict_x):
	"Checks the frequency of individual letters in a given string"
	# Calculates frequency of alphabets in the string
	for i in x:
		for j in  dict_x:
			if i == j:
				 dict_x[j] =  dict_x.get(j) + 1
	
	# Sorts the dictionary in the correct order
	dict_x = dict(sorted(dict_x.items(), key=operator.itemgetter(1),reverse=True))
        
	# Prints frequency in descending order
	print("\n\t The frequency of alphabets:")
	for i in dict_x:
		if dict_x.get(i) != 0:
			for j in set_x:
				if i == j:
					print(j, " : ",  dict_x.get(i))

# Main body of the program >>>

choice = 'y'
while choice == 'y' or choice == 'Y':
	# Dictionary to store frequency
	dict_x = {
      		"a":0, "b":0, "c":0, "d":0, "e":0, "f":0,
      		"g":0, "h":0, "i":0, "j":0, "k":0, "l":0,
      		"m":0, "n":0, "o":0, "p":0, "q":0, "r":0,
      		"s":0, "t":0, "u":0, "v":0, "w":0, "x":0,
      		"y":0, "z":0
	}

	# Read string input from user
	x = str(input("Enter a string: "))

	# Displays the user input and converts it to lowercase
	print("\n\t The text you entered is: ", x)
	x = x.lower()

	# Function calls
	set_x = StrToSet(x)
	most_frequent(x, set_x, dict_x)

	# Asks user whether to run program again
	choice = str(input("\n\t Do you wish to run program again? Y/N : "))

if choice != 'n' or choice != 'N':
	print("\n Invalid input, terminating program... Kindly rerun the program if you wish to use it again.")
else:
	print("\n *** Thank you ! ***")
print("\n End of program.")