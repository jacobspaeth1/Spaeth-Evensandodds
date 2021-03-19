"""
EvensAndOdds
Name: 
Period/Core: 

Ask a user for how many integer numbers they would like to check.
Then, using a for loop, prompt the user for an integer,
and output if that integer is even or odd.

Continue doing this as many times as the user indicated.
Once the loop ends, output how many even integers were entered and
how many odd integers were entered.
"""

import os
import importlib.util

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command) # Run pytest command

### BEGIN EDITING HERE

def main():
  """This function should contain the code for EvensAndOdds."""
  x = int(input("How many numbers do you need to check?"))
  
  # Are the commands in your main function indented?


### STOP EDITING HERE

if __name__ == "__main__":
  main() # Call main function
  t = input("Run pytest? (y/n)").lower() # Ask to run Pytest
  if t == 'y':
    run_tests()