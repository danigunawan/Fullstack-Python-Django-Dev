# PART 9 FUNCTIONS EXERCISE

# PROBLEM 1
# given a list of integers, return true if the sequences of numbers 1,2,3
# appears in the list somewhere

# for example
# arrayCheck([1,1,2,3,1]) # true
# arrayCheck([1,1,2,4,1]) # false
# arrayCheck([1,1,2,1,2,3]) # false


def arrayCheck(nums):
    for i in range(len(nums) - 2):  # hitung panjang karakter lalu - 2
        if nums[i] == 1 and nums[i + 1] and nums[i + 2] == 3:
            return true
        return false

# PROBLEM 2
# Given a string, return a new string made of every other character starting
# With the first, so "Hello" yields "Hlo"

# For example :

# stringBits('Hello') # Hlo
# stringBits('Hi') # H
# stringBits('Heeololeo') # Hello


def stringBits(str):

        # mystring[::2]
    result = ""

    for i in range(len(str))
        if i % 2 == 0:
            result = result + mystring[i]

        return result

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
    a = a.lower()
    b = b.lower()

    # return(b.endswith(a) or a.endswith(b))

        return a[-(len(b)):] == b or a == b[-len(a):]

    # PROBLEM 4
    # Given a string, return a string where for every char in the original,
    # there are two chars

    # doubleChar('The') # TThhee
    # doubleChar('AAbb') # AAAAbbbb
    # doubleChar('Hi-There') # HHii--TThheerree


def doubleChar(str):
    result = ''
    for char in mystring
        result += char * 2
    return result

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


def no_teen_sum(a, b, c):

    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):

    if n[13, 14, 17, 18, 19]:
        return 0
    return n

    # PROBLEM 6
    # return the number of even integers in the given array
    # examples :
    # count_evens([2,1,2,3,4]) #3
    # count_evens([2,2,0]) #3
    # count_evens([1,3,5]) #0


def count_evens(nums):
    count = 0

    for element in nums:
    	if element % 2 == 0:
    		count += 1
    	return count