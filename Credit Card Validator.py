## ----------------Credit Card Validator---------------- ##

# 1. Remove any '-' or ' '.
# 2. Add all digits in the odd places from right to left.
# 3. Double every even position digit then add all from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3.
# 5. If sum is divisible by 10, the credit card # is valid. 


#STEP (1):
def get_card_number():
    card_number = list(input("Enter the credit card number #: ")) # Prompts the credit card number from the user and type cast it to a list.

    for element in card_number: # Looping through the list and remove any spaces or hyphens.
        if element == " " or element == "-": # If the element in the list of characters is hyphen or space and remove it.
            card_number.remove(element)

    card_number = list(map(int,card_number)) # After removing all the spaces or hyphens let's turn the list of characters to list of integers

    card_number.reverse() # Reverse the order of the credit card list as we operate from right ro left

    return card_number


#STEP (2):
def sum_odd(card_number):   
    sum_odd_digits = 0 # Accumlator for the sum of odd digits 
    i = 0 # Index of first odd digit position 
    while i < len(card_number):
        sum_odd_digits += card_number[i] # Accmulate to get the sum
        i += 2 # Increment by two to get odd postions only as we started from (i = 1)--->(1,3,5,...so on)

    return sum_odd_digits    



#STEP (3):
def sum_even(card_number):
    sum_even_digits = 0
    j = 1 #Index of first even postion 
    while j < len(card_number):
        digit = card_number[j] * 2 # Double every digit

        if digit >= 10: # Ten is a two-digit number so if the sum is greater than or equal 10 it would be a two digit number two.
            digit = str(digit) # Type cast it to a string 
            digit =list(map(int,digit)) # Separate the each digit of the two-digit number into a list
            digit = sum(digit) #summation of these two digit number will be our new digit 
            sum_even_digits += digit # Accmulate to get the sum
        else:
            sum_even_digits += digit    
        j += 2 # Increment by two to get even postions only as we started from (i = 0)--->(0,2,4,...so on)

    return sum_even_digits




#STEP (4) and STEP (5):
def check_valid(sum_odd,sum_even):
    total = sum_even + sum_odd 
    if total % 10 == 0:#Check if the Total is divisble by 10.
        print("Valid Credit Card")
    else:
        print("Invalid Credit Card") 





def main():
    card_number = get_card_number() 
    odd_sum = sum_odd(card_number)
    even_sum = sum_even(card_number)
    check_valid(odd_sum,even_sum)       


if __name__ == "__main__":
    main()    