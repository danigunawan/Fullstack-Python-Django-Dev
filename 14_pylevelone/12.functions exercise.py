# PART 9 FUNCTIONS EXERCISE

# PROBLEM 1
# given a list of integers, return true if the sequences of numbers 1,2,3
# appears in the list somewhere

# for example
# arrayCheck([1,1,2,3,1]) # true
# arrayCheck([1,1,2,4,1]) # false
# arrayCheck([1,1,2,1,2,3]) # false


def arrayCheck(nums):
# CODE GOES HERE

# PROBLEM 2
# Given a string, return a new string made of every other character starting
# With the first, so "Hello" yields "Hlo"

# For example :

# stringBits('Hello') # Hlo
# stringBits('Hi') # H
# stringBits('Heeololeo') # Hello


def stringBits(str):
        # Code Goes Here

# PROBLEM 3
# Given Two Strings, return True if either of the strings appears at the very end
# Of the other string, ignoring upper/lower case differences (in other words the computation should not be "Case Sensitive")
#
# Note : s.Lower() returns the Lowercase version of a string
#
# Examples :
#
# end other('Hiabc', 'abc') # True
# end other('AbC', 'Hiabc') # True
# end other('abc', 'abXabc') # True


def end_other(a, b):
# Code Goes Here

# PROBLEM 4
# Given a string, return a string where for every char in the original,
# there are two chars

#doubleChar('The') # TThhee
#doubleChar('AAbb') # AAAAbbbb
#doubleChar('Hi-There') # HHii--TThheerree

def doubleChar(str):
	#CODE GOES HERE

# PROBLEM 5
# Read this problem statement carefully

# Given 3 int values, a,b,c return their sum. However, if any of the values is a 
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule
# 
# in this way, you avoid repeating the teen code 3 times (i.e. "decomposition")
# define the helper below and at the same indent level as the main no_teen_sum()
# again, you will have two functions for this problem!
# examples :
# no_teen_sum(1,2,3) #6
# no_teen_sum(2,13,1) #3
# no_teen_sum(2,1,14) #3

def no_teen_sum(a,b,c):
	#CODE GOES HERE
def fix_teen(n):
	#CODE GOES HERE

# PROBLEM 6
# return the number of even integers in the given array
# examples :
# count_evens([2,1,2,3,4]) #3
# count_evens([2,2,0]) #3
# count_evens([1,3,5]) #0

def count_evens(nums):
	#CODE GOES HERE