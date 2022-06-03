# Write a function called match_ends with a parameter called str_list (list), which represents a list of strings. 
Your match_ends function should return an int value representing how many strings are both greater than or equal to 2 in length, 
and have the same char at the beginning and end.

#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys

### HELPER FUNCTIONS (IF NECESSARY) ###



### MAIN FUNCTION ###
def match_ends():
  count = 0
  str_list = sys.argv[1:]
  for word in str_list:
    if len(word) > 1 and word[0] == word[-1]:
      count += 1
  return count

print(match_ends())






### DUNDER CHECK ###
#if __name__ == "__main__":
  #main()
