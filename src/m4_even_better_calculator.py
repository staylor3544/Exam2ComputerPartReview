###############################################################################
# TODO: 1.
#   
#   For this _TODO_, we are going to improve on our calculator from the Session
#   7 Coding Exercises.
#
#   So, first you will need to copy a working version of your calculator. Make
#   sure you have your operator functions as well as your primary calculator
#   function. You may use either your if-statement version or match-case
#   version. Regardless, make sure you have a working version.
#
#   We will be making a few different improvements to make this calculator even
#   better.
#
#      1. First, let make it so that the user can keep doing more calculations.
#         So, the calculator should keep asking for new numbers and operations
#         after it calculates the previous one. Use a while loop for your
#         solution.
#      
#      2. Next, make it so that if the user puts in an invalid operation it
#         prompts the user again for an operation. (Use a while loop)
#      
#      3. Next, add some logic to check that the numbers that user enters are
#         actually numbers. If the number is valid, the calculator should keep
#         going. If the number is invalid, it should prompt the user like so:
#             "Invalid Number"
#         and ask for a new one. (You will likely need a couple more while
#         loops to do this for each number)
#      
#             HINT: There is a built-in method that can check this called
#                   isdigit(). It returns True if every character in the string
#                   is a digit. You can look at this method more in the
#                   Resources in Session 3. 
#      
#      4. Finally, you will notice that the isdigit() function won't work for
#         decimals because "." is not a digit. There are many ways to solve
#         this, but here is a rough guide to help you get started.
#      
#             1) First, check if there is a "." in the string.
#             2) Next, make a copy of the string but remove the "." from it.
#             3) Now, check if the new string is a digit.
#                 a) If it is, convert the original string to a float and you
#                    can do the math
#                 b) If not, it is an invalid number. And you should prompt
#                    the user saying it is invalid and ask for a new number.
#      
#   Your calculator should still work like Session 7 except for the changes
#   outlined above.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
t = (2,5,3)

print(t[1:])
