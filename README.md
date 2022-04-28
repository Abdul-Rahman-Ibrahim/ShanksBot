# ShanksBot
William Shanks - Reciprocal of Prime Numbers
This bot calculates the number of figures in the period of the reciprocal of prime numbers
Given the reciprocal of a prime number 1/n, the bot computes how many digit of 1/n comes before it starts to repeat.
Example. n = 7
1/n = 1/7 = 0.142857142857142857142857142857...
From the above example, it can be seen that,after the decimal point, 1/7 repeats after 6 digits. That is after 142857, the 1/7 repeats.
Similarly, 1/11 = 0.090909090909... After the decimal point, 1/11 repeats after 2 figures. That is after 09, 1/11 repeats.
For simplicity, lets call the the number of digits shanks.
We say 7 has shanks of 6, 11 has shanks of 2.
William shanks spent several years manually computing shanks of prime numbers.
In his book, 'Reciprocal of Prime Numbers', he made some few mistakes in the computation. However, all the mistake was either half of the actual shank
or twice of the actual shank. This makes me believe he had an algorithm for the computation.
Examples of prime numbers and their shanks:
60013 - 5001
60017 - 60016
60029 - 60028
61561 - 505
