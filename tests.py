import main as EvensAndOdds

import random
import string

prompts = []
inputs = []

def random_string_generator(str_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(str_size))


def mock_int_input(*args, **kwargs):
  """Returns an integer 1-999 as a str"""
  prompts.append(args[0]) # Keep track of prompts

  str_size = random.randint(1,3)
  chars = string.digits
  s = random_string_generator(str_size, chars)
  inputs.append(s) # Keep track of returned values
  return s

def test_numbers_to_check_prompt(monkeypatch):
  """This test case makes sure the first input prompt asks for 'how many numbers'"""
  monkeypatch.setattr('builtins.input', mock_int_input)  
  prompts.clear()
  inputs.clear()

  EvensAndOdds.main()
  # Assert the first prompt is about 'how many numbers'
  assert 'how many numbers' in prompts[0].lower()

def test_enter_number_prompts(monkeypatch, capsys):
  """This test case makes sure the program outputs 'Enter number: '"""
  monkeypatch.setattr('builtins.input', mock_int_input)
  prompts.clear()
  inputs.clear()

  EvensAndOdds.main()
  # output = capsys.readouterr().out
  prompt_count = 0
  for p in prompts:
    if p.lower().startswith("enter number"): # Count prompts starting with "enter number"
      prompt_count+=1
  assert prompt_count == int(inputs[0])

def test_even_oddness(monkeypatch, capsys):
  """This test case makes sure that even/odd numbers are displayed correctly"""
  monkeypatch.setattr('builtins.input', mock_int_input)
  prompts.clear()
  inputs.clear()

  EvensAndOdds.main()
  output = capsys.readouterr().out
  for line in output.split('\n'):
    d = line.split(" ")[0]
    if d.startswith("-"): # .isdigit() doesn't work on negatives so slice '-' from the str.
      d = d[1:]

    if d.isdigit():
      if int(d) % 2 == 0: assert "even" in line.lower()
      else: assert "odd" in line.lower()

def test_even_odd_count(monkeypatch, capsys):
  """This test verifies that the even and odd count are correct."""
  monkeypatch.setattr('builtins.input', mock_int_input)
  prompts.clear()
  inputs.clear()

  EvensAndOdds.main()
  output = capsys.readouterr().out.split('\n')

  even_count, odd_count = 0, 0
  for x in inputs[1:]: # Skip first input which is loop number
    x = int(x)
    if x % 2 == 0: even_count += 1
    else: odd_count += 1

  # get index of list item containing substring from https://stackoverflow.com/a/38303263
  odd_count_index = [idx for idx, s in enumerate(output) if 'you entered' in s.lower() and 'odd' in s.lower()][0]
  even_count_index = [idx for idx, s in enumerate(output) if 'you entered' in s.lower() and 'even' in s.lower()][0]

  # Assert that each line says the correct count.
  odd_count_line = output[odd_count_index]
  assert str(odd_count) in odd_count_line
  even_count_line = output[even_count_index]
  assert str(even_count) in even_count_line