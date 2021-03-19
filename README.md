# Evens and Odds

Asks a user for how many numbers they would like to check. Use a loop to determine and display if the number is even or odd and at the end output how many even and odd numbers were each entered.

Originally by Edhesive Intro to CS.

## Overview

Write a program that will ask a user for how many integer numbers they would like to check. Then, using a for loop, prompt the user for an integer, and output if that integer is even or odd. Continue doing this as many times as the user indicated. Once the loop ends, output how many even integers were entered and how many odd integers were entered.

**Hint:** For an integer to be even, when the integer is divided by 2, there should be no remainder - so you will want to use the modulus (`%`) operator.

**Hint:** You will need two count variables to keep track of odd and even numbers.

## Sample Run 1
```
How many numbers do you need to check? 5
Enter number: 20
20 is an even number.
Enter number: 33
33 is an odd number.
Enter number: 4
4 is an even number.
Enter number: 77
77 is an odd number.
Enter number: 8
8 is an even number.
You entered 3 even number(s).
You entered 2 odd number(s).
```

## Sample Run 2
```
How many numbers do you need to check? 3
Enter number: 10
10 is an even number.
Enter number: 3
3 is an odd number.
Enter number: 400
400 is an even number.
You entered 2 even number(s).
You entered 1 odd number(s).
```

## Benchmarks

1. Prompt the user to answer the question, `“How many numbers do you need to check? “`
2. Create and initialize two count variables - one for `odd_count` and one for `even_count`.
3. Based on the previous input, create a `for` loop that will run that exact number of times.
   1. Prompt the user to `“Enter number: “`
   2. If that number is even:
      1. Output `“{number} is an even number.”`
      2. Update the `even_count` variable.
   3. Or else if the number is odd:
      1. Output `“{number} is an odd number.”`
      2. Update the `odd_count` variable.
4. Output `“You entered {even_count} even number(s).”`
5. Output `“You entered {odd_count} odd number(s).”`

## Enhancements

Incorporate at least 2 of the following enhancements or come up with your own!
* Define and call a function that uses parameters and returns if the number is even or odd.
  * Consider something like `is_even(num)` that returns `True` if `num` is even.
* Add additional outputs to the end such as:
  * Largest number entered
  * Smallest number entered
  * Sum of numbers entered
* Instead of crashing, prompt the user to try again if they enter a string or invalid number.
(Enhancements should add some significant new functionality to the program and be more than cosmetic changes.)