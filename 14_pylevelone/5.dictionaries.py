# dictionaries
# example 1
my_stuff = {"key1": "value", "key2": "value2"}
# mengakses value dari array pertama/ 0 dengan kunci index 'key1'
print(my_stuff['key1'])

# example 2
my_stuff2 = {"key1": 123, "key2": "value2", "key3": {'123': [1, 2, 3]}}
print(my_stuff2)  # mengakses value dari array pertama/ 0 dengan kunci index 'key1'

# example 3
my_stuff3 = {"key1": 123, "key2": "value2", "key3": {'123': [1, 2, 'grab me']}}
# mengakses value dari array 3/ 0 dengan kunci index 'key3' dan mengakses
# data array pertama dari 'key3' yakni '123' dengan index ke tiga [2]
# yakni 'grab me' #maka hasilnya di print grab me
print(my_stuff3['key3']['123'][2])


# example 4
my_stuff4 = {"key1": 123, "key2": "value2", "key3": {'123': [1, 2, 'grab me']}}
# mengakses value dari array 3/ 0 dengan kunci index 'key3' dan mengakses
# data array pertama dari 'key3' yakni '123' dengan index ke tiga [2]
# yakni 'grab me' dan gunakan fungsi upper untuk hasil huruf besar semua
# #maka hasilnya di print GRAB ME
print(my_stuff4['key3']['123'][2].upper())

# example 5
my_stuff5 = {'lunch': 'pizza', 'bfast': 'eggs'}
# akses array pertama dengan index key 'lunch' maka hasilnya pizza
my_stuff5['lunch']
# akses array pertama dan set nilai key lunch dengan value burger
my_stuff5['lunch'] = 'burger'
# akses array baru dan set nilai key dinner dengan value pasta
my_stuff5['dinner'] = 'pasta'
print(my_stuff5['lunch'])
# menambahkan parameter nilai array key dinner {'lunch': 'burger',
# 'bfast': 'eggs', 'dinner': 'pasta'}
print(my_stuff5)
