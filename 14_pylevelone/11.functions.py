# FUNCTIONS
# example 1


def my_func(parameter1='default'):
    """

    THIS IS THE DOCTRINGS

    """
    print("my first python function {}".format(parameter1))

# Example 2


def hello():  # jadi setelah syntax itu adalah doc string nya kita pakai / execute dalam kasus ini setelah method di buat hello() kita buat pernyataan print("hello") dan memanggil object dengan hello() setelah doctrings
    print("hello")
hello()  # maka hasilnya = hello


# Example 3

def hello():  # jadi setelah syntax itu adalah doc string nya kita pakai / execute dalam kasus ini setelah method di buat hello() kita buat pernyataan return "hello" dan memanggil object dengan hello() setelah doctrings
    return "hello"  # kasus ut
result = hello()  # kita buat variabel result untuk menampung object

print(result)  # lalu kita print variabel yang berisi object tsb maka hasilnya = hello


# Example 4

def addNum(num1, num2):  # dalam method python argument di wakilkan dengan colon (:) jika pada php {}
    return num1 + num2


# jika begini maka masuk dalam fungsi dan hasilnya 3 namun jika
result = addNum(1, 2)
# result = addNum("1","2") #namun jika begini dengan maka yang direturn
# adalah nilai string hasilnya 12 maka tidak benar jika gunakan ini
print(result)

# Example 5


def addNum(num1, num2):  # dalam method python argument di wakilkan dengan colon (:) jika pada php {}
    return num1 + num2
# jika begini maka masuk dalam fu
# ngsi dan hasilnya 3 namun jika
result = addNum(1, 2)
# result = addNum("1","2") #namun jika begini dengan maka yang direturn
# adalah nilai string hasilnya 12 maka tidak benar jika gunakan ini
# fungsi type ini melihat tipe data apa saja yang dipasing atau
# ditampilkan jika int maka hasilnya <class 'int'>
print(type(result))

# Example 6


def addNum(num1, num2):  # dalam method python argument di wakilkan dengan colon (:) jika pada php {}
    # jika if pernyataan juga ditandai dengan colon (:) jika pd php {}
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:  # colon ini : menggantikan {} kurawal
        return "Sorry,i need integers!"
result = addNum(2, 3)
print(result)  # 5

# Example 7


def addNum(num1, num2):  # dalam method python argument di wakilkan dengan colon (:) jika pada php {}
    # jika if pernyataan juga ditandai dengan colon (:) jika pd php {}
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:  # colon ini : menggantikan {} kurawal
        return "Sorry,i need integers!"
result = addNum("2", '3')
print(result)  # Sorry,i need integers!

# Lambda Expression

# Filter/
# example 8
mylist = [1, 2, 3, 4, 5, 6, 7, 8]


def even_bool(num):
    return num % 2 == 0
evens = filter(even_bool, mylist)
print(evens)  # <filter object at 0x0000000002253E80>

# example 9

mylist = [1, 2, 3, 4, 5, 6, 7, 8]


evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))  # [2, 4, 6, 8]

# example 10
tweet = "Go Sport! #Sports"
result = tweet.split('#')
# ['Go Sport! ', 'Sports'] split disini yakni merubah huruf # menjadi koma untuk dijadikan array list
print(result)

# example 11
tweet = "Go Sport! #Sports"
# artinya mengambil nilai array list kedua yakni [gosport, sports] = 0 , 1
result = tweet.split('#')[1]
# ['Go Sport! ', 'Sports'] split disini yakni merubah huruf # menjadi koma untuk dijadikan array list
print(result)

# example 12
print('x' in[1,2,3,'x']) #true