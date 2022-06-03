Someone dropped our cyber haiku dictionary and the order in which they were stored is all messed up. 
Can you fix the order dictionary and print them out in the right order? 
The name of your helper function(s) and parameter(s) is/are up to you. 

#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import ast



### HELPER FUNCTIONS (IF NECESSARY) ###
def haiku(dict):
  input = dict.read()
  haiku_dct = ast.literal_eval(input)
  return_str = ""
  haiku_l = len(haiku_dct)
  
  for num in range(1, haiku_l):
    return_str += haiku_dct[str(num)]
    if haiku_dct[str(num)] != "\n" and num != haiku_l - 1:
      return_str += " "
    elif haiku_dct[str(num)] == "\n":
      return_str = return_str.rstrip() + "\n"

  return return_str
### MAIN FUNCTION ###
def main(): 
  file_name = sys.argv[1]
  with open(file_name) as f:
    print(haiku(f))
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()
#```
