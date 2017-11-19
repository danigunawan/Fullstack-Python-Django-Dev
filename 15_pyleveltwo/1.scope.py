# example 1
x = 25


def my_func():
    x = 50
    return x
print(x)  # kita print langsung tanpa menggunakan method = 25
print(my_func())  # jika menggunakan method = 50

# example 2
x = 25


def my_func():
    x = 50
    return x
# print(x) # kita print langsung tanpa menggunakan method = 25
# print(my_func()) # jika menggunakan method = 50

my_func()  # ini tidak muncul
print(x)  # yang muncul ini

# example 3
# LOCAL

lambda x: x**2

# Eclosing function locals
name = 'this is a global name!'


def greet():
    name = "sammy"

    def hello():
        print("hello " + name)

    hello()  # fungsi lokal dari method hello
greet()  # fungsi lokal dari method greet
print(name)  # global variabel name


# example 4
x = 50


def func(x):
    print('x is:', x)
    x = 1000
    print('local x changed to:', x)

func(x)
print(x)# 50 langsung dari global variabel yakni x



# example 5
x = 50


def func():
	global x # ini untuk fungsi global variabel didalam method
	x = 1000
print("before fuction call, x is:", x) # sebelum fungsi dipanggil maka hasilnya 50 karena x berasal dari global variabel x bukan didalam func() / method
func()
print("after function call, x is:", x) # dipanggil berdasarkan fungsi maka x diganti menjadi 1000 nilainya 


