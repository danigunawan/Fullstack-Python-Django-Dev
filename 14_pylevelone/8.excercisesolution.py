# PART 6 LATIHAN #

##### Problem 1 ########

# Given String
s = 'django'

# use indexing to print out the following :

# 'd'
s[0]
# 'o'
s[5]  # karena 1 nya dimulai dari 0

# 'djan'
s[:4]  # atau s[0:4]

# 'jan'
s[1:4]

# 'go'
s[4:]

# Bonus : Use indexing to reverse the string
s[::-1]

##### Problem 2 #######

# Given this nested list
l = [3, 7, [1, 4, 'hello']]

# Reassign "hello" to be "goodbye" / menempatkan hello menjadi goodbye
# posisi hello ada di array ke dua setelah 0,1, lalu 2 dan kita set
# menjadi goodbye
l[2][2] = 'goodbye'


##### Problem 3 ####

# Using keys and indexing grab the 'hello' from the following dictionaries :

d1 = {'simple_key': 'hello'}

# menggunakan kunci array pertama / 0 'simple_key' untuk mengambil nilai
# 'hello'
d1['simple_key']

d2 = {'k1': {'k2': 'hello'}}
# mengambil nilai hello dari array pertama yakni k1 dan array bersarang
# dengan kunci k2
d2['k1']['k2']

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
d3['k1'][0]['this is deep'][1][0]  # pertama gunakan array pertama untuk akses nested array pertama 0 lalu gunakan akses key 'this is deep' untuk akses nested array 1 dan mengambil nilai hello pada nested array pertama [0] didalam nested array

### Problem 4 ###

# use a set to find the unique values of the list below :

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

set(mylist)

### Problem 5 ###

# You are given two variables:

age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print("hello my dog's name is {a} and he is {b} years old".format(
    a=age, b=name))
