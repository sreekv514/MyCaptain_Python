# Program to enter student details in a CSV file.

# Package for handling CSV file functions.
import csv

# File writing function
def file_write(student_info_list, filename):
  "Function to write student info into a CSV file"
  # Function call to write processed data to file.
  with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)

    # Processed data in form of list is written to file.
    writer.writerow(student_info_list)

    file.close()

# Check for pre-existing records in same file
def file_check(filename):
    "Function to check if there are pre-existing records"
    with open(filename, 'a', newline='') as file:
      if file.tell() == 0:
        # If file is empty, header is written to it.
        writer = csv.writer(file)
        writer.writerow(["Sl.No.", "Name", "Age", "Contact Number", "Email ID"])
        count = 0
        file.close()
        return count
      else:
        # Number of pre-existing records are returned as counter
        file = open(filename)
        file_content = file.read()
        num_of_students_registered = file_content.split("\n")
        count = -1
        for i in num_of_students_registered:
          if i:
            count += 1
        file.close()
        return count

# Main function
if __name__ == '__main__':
  filename = str(input("Enter name of file to store student information (kindly do NOT mention the extension): "))
  filename = filename.strip() 
  filename = filename + ".csv"
  count = file_check(filename)
  condition = True
  # 1. Entering or asking user to enter Student information.
  while(condition):
    count += 1
    student_info = input("Enter details for student no.{} in the given format - \n\t Name, Age, Contact_number, Email_ID: ".format(count))
    # 2. Pre-processing the collected data. ie. Converting the data into a list that can be written into a CSV file.
    student_info_list = [count, ] + student_info.split(", ")
    print("The following information will be written to file: ")
    print("\t Name: ", student_info_list[1])
    print("\t Age: ", student_info_list[2])
    print("\t Contact number: ", student_info_list[3])
    print("\t Email ID: ", student_info_list[4])

    # Conditional statements to check if the user wants to enter the same data in the file
    choice = True
    while(choice):
      confirm = input("Proceed to write student information to file? Y/N: ")
      if confirm == 'y' or confirm == 'Y':
        # 3. Writing all the pre-processed data into a File.
        file_write(student_info_list, filename)
        choice = False
      elif confirm == 'n' or confirm == 'N':
        count = count - 1
        print("The above details will NOT be added to file.")
        choice = False
      else:
        print("Incorrect value entered. Please enter Y for yes or N for no.")
        choice = False
    
    # Conditional statements to check if the user wants to enter another student's details
    choice = True
    while(choice):
      check_condition = input("Add another student's data? Enter Y/N: ")
      if check_condition == 'n' or check_condition == 'N':
        condition = False
        choice = False
      elif check_condition == 'y' or check_condition == 'Y':
        condition = True
        choice = False
      else:
        print("Incorrect value entered. Please enter Y for yes or N for no.")
        choice = False

  print("\nAll verified information written to file: " + filename)
  print("\nEnd of program.")
