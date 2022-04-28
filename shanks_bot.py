from math import floor

def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

def shanks_bot(prime_number):
    value = "0." #instantiating numerical value of (1/prime_number) up to a precision equal to the shanks of the prime number
    remainder = 1 #remainder in long division
    lst = [] #list of remainders during long divison.
    while True:
        count = 0 #counts the number of zeros to be appended to the value variable
        #implementing long division
        while remainder < prime_number:
            remainder = remainder * 10 #'add' one zero to the remainder if the divisor is less than the dividend

            #counts the number of non-significant zeros to be added to 'value' if after the previous
            #operation the remainder is still less than the prime number
            count += 1
            if count > 1:
                value += str(0) #adds insignificant zero to 'value'

        #Exit loop if a remainder from the long divion is repeated...
        if remainder in lst:
            break
        
        #...otherwise we add the remainder to 'lst' and continue with the long divison.
        lst.append(remainder)
        digit = floor(remainder/prime_number) #gets the most significant digit from the divison
        value += str(digit) #inserts the digit(s) to 'value'
        
        #gets remainder after the division. Alternatively we can use, (remainder = remainder % prime_number) to get the remainder
        remainder = remainder - (floor(remainder/prime_number)*prime_number)
        if remainder == 0:
            print("{0} has 0 shanks".format(prime_number))
            break

    del lst #delets 'lst' from memory.

    #counts the number of insignificant zeros
    if value[2:].startswith(str(0)):
        i = 0
        while value[2:][i] == str(0):
            i += 1
    else:
        i = 0
        
    if remainder != 0:  
        print("Reciprocal of {0} repeats after {1} figures".format(prime_number, len(value[2:])-i)) #prints the shanks
        prompt_message = "Enter 1 if you wish to see the reciprocal of {0} before it starts to repeat. ".format(prime_number)
        
        ask = input(prompt_message)
        if int(ask) == 1:
            print(value[:-i])

##Test
num = int(input("Enter a prime number to find its shank "))
if is_prime(num):
    shanks_bot(num)
else:
    print("{0} is not a prime number. Exiting program.".format(num))
