# Booleans
True
False
# Tuples
# example 1
t = (1, 2, 3)
print(t[0])  # akses array pertama = 1

# example 2
# da = ('a', True, 123) #tupples selalu menggunakan ()
# print(t)
# t[0] = 'NEW' # jika kita set nilai array pertama/ 0 yakni 'a' dengan
# string 'New' maka error TypeError: 'tuple' object does not support item
# assignment karna yang diset object tersebut bukan tupple melainkan array
# [0] solusinya di example 3


# example 3
mylist = ['a', True, 123]  # solusinya kita ubah menjadi object array []
print(mylist)  # ['a', True, 123]
mylist[0] = 'NEW'  # jika kita set nilai array pertama/ 0 yakni 'a' dengan string 'New' maka error TypeError: 'tuple' object does not support item assignment object tersebut bukan tupple
# ['NEW', True, 123] jadi nilai array pertama [0] dari kita ubah nilainya dari 'a' menjadi 'NEW'
print(mylist)

# Sets
# example 1
x = set()
x.add(1)
x.add(2)
print(x)  # hasilnya {1, 2}

# example 2
x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
print(x)  # {0.1, 1, 2, 4}

# example 3
x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(4)
x.add(4)
print(x)

# menset nilai array yang tadinya {1, 2, 4} menjadi {1, 2, 3}
converted = set([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3])
# menset nilai array yang tadinya {1, 2, 4} menjadi {1, 2, 3, 5}
converted = set([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 5])

print(converted)
