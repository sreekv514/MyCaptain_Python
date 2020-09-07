# Program to read filename from user and print the extension
print("\t File extension decoder")
choice = 'Y'
while choice == 'Y' or choice == 'y':
  # Dictionary with common file extensions
  extDict = {
    "exe": "Executable file",
    "c": "C source file",
    "cpp": "C++ source file",
    "java": "Java source file",
    "class": "Java class file",
    "jar": "Java archive file",
    "py": "Python source file",
    "htm": "HTML file",
    "html": "HTML file",
    "php": "PHP file",
    "js": "JavaScript file",
    "sql": "SQL database",
    "db": "Database",
    "mdb": "Microsoft Access Database file",
    "txt": "Plain text file",
    "rtf": "Rich text format",
    "doc": "Document file",
    "docx": "Document file",
    "pdf": "PDF file",
    "xls": "Excel file",
    "ppt": "Powerpoint file",
    "mp3": "MP3 audio file",
    "rar": "Compressed RAR file",
    "bmp": "Bitmap file",
    "jpg": "JPEG image file",
    "jpeg": "JPEG image file",
    "png": "PNG image file",
    "gif": "GIF file"
  }
  print()
  # Read input from user
  fname = input("Enter filename with extension: ")
  # Split filename to extract only extension code
  extension = fname.split('.')
  extension = extension[1].lower()
  found = 0
  # Loop through the dictionary to find matching extension
  for x in extDict:
    if(extension == x):
      found = 1
      print("The file type is:", extDict.get(x))
      break
  if (found == 0):
    print("Sorry! This file extension is not part of our dictionary.")
  print()
  # Request user whether to or not rerun the program 
  choice = input("Would you like to continue? Y/N: ")
print("Program terminated.")