
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Several of the examples we've done in class have involved dealing with prime numbers: decide whether a number is a prime, find the next prime, print the first 100 primes, etc. The concept of a prime number is fundamental in mathematics, particularly in number theory. In fact, the fundamental theorem of arithmetic states that every positive integer (greater than 1) can be represented uniquely (where order doesn't matter) as a product of one or more primes. Your task in this assignment is to input a series of arbitrary positive integers and return for each a list of its prime factors. Exit when the user enters 0.

Begin by printing the welcome message: "Find Prime Factors:" Then, enter a loop to handle a series of inputs. At each iteration of the loop do the following:

	1.	Ask the user to input an integer. You can assume that the input will be an integer.
	2.	If the input is 0, exit the program with a Goodbye message.
	3.	If the input is 1, report that 1 has no prime factorization.
	4.	If the input is negative, report that.
	5.	Finally, if the input is a positive integer greater than 1, print the prime factorization as a list. If the number is a prime, print a list with just that number.

See the example behavior below for details of the interactions. Put a blank line between each round of interaction to make the output more readible.

Notice that with this assignment, you can finally use lists in your programming. In fact, you're expected to do so.

Expected Output:

Below is some sample output for this program. You should match this exactly for these inputs. As usual, this shows running the code from the command line.

> python FindPrimeFactors.py
Find Prime Factors:
Enter a positive integer (or 0 to stop): 103
  The prime factorization of 103 is: [103]

Enter a positive integer (or 0 to stop): 104
  The prime factorization of 104 is: [2, 2, 2, 13]

Enter a positive integer (or 0 to stop): 1000
  The prime factorization of 1000 is: [2, 2, 2, 5, 5, 5]

Enter a positive integer (or 0 to stop): -104
  Negative integer entered. Try again.

Enter a positive integer (or 0 to stop): 1
  1 has no prime factorization.

Enter a positive integer (or 0 to stop): 1234567890
  The prime factorization of 1234567890 is: [2, 3, 3, 5, 3607, 3803]

Enter a positive integer (or 0 to stop): 0
Goodbye!

Finding the Prime Factorization:

You can find the prime factorization of a number num with the following algorithm, which you do have to code:

if num is prime:
   answer is a list containing only num

otherwise num is composite:
   set the list of factors to the empty list
   set d to 2
   as long as num is greater than 1 do the following:
      check if d divides num
         if it does, add d to the end of the list of factors
            and divide num by d
         keep checking d until it doesn't divide num
      set d to the next biggest prime
   at this point num is 1 and the list of factors is the prime factorization
   answer is the list of factors

You should play with this algorithm on paper until you're very confident how it works. Then code it.
