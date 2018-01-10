import os
file_path = raw_input('Filename path: ')
# Check if file exists
if os.path.exists(file_path):
  print("File exists at %s") %(file_path);
else:
  print("File not found");
