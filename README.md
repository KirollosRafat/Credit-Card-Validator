# Credit Card Validator
Python credit card validator program:
Prompts the credit card number from the user and return if it's a vaild credit card or not.

1. Remove any '-' or ' '
2. Add all digits in the odd places from right to left
3. Double every second digit from right to left.
(If result is a two-digit number,
add the two-digit number together to get a single digit.)
4. Sum the totals of steps 2 & 3
5. If sum is divisible by 10, the credit card # is valid
