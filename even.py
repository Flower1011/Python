# Write a function called is_even with a parameter called file, which represents an open file containing a single number on each line. 
Your is_even function should go through the open file line by line, determine if the number on that line is even or not and print: 
'<number> <True/False>' depending on if the number is even or not. 

#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def is_even(file):
  for line in file:
    line = line.strip()
    if int(line) %2 == 0:
      print (line + " " + str(True))
    else:
      print (line + " " + str(False))




### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  open_file = open(file_name)
  (is_even(open_file))
  open_file.close()
  
  

### DUNDER CHECK ###
if __name__ == "__main__":
  main()
