# Decorators


def func():
    return 1

print(func())

# example 2
s = "GLOBAL VARIABLE"  # s adalah variabel global


def func(s):
    print(s)

func(s)

# #example 3
s = "GLOBAL VARIABLE"  # s adalah variabel global


def func(s):
    s = 50
    print(s)

func(s)  # 50 dia pakai variabel yang berada di local function/method
print(s)  # Menggunakan nilai pada GLOBAL VARIABLE s


# example 4
s = "GLOBAL VARIABLE"  # s adalah variabel global


def func():
    mylocal = 10
    print(locals())
    print(globals())

func()

# example 5
# s = "GLOBAL VARIABLE" # s adalah variabel global
# def func():
# 	mylocal = 10
# 	# print(locals())
# 	print(globals(['s']))

# func()


# example 6
def hello(name="Jose"):  # parameter name berisi nilai Jose
    return "hello " + name  # mengembalikan nilai pasingan dari string dan parameter

print(hello())  # kita print method hello

mynewgreet = hello  # instantiasi object dari hello dan membuat object baru mynewgreet

print(mynewgreet())  # print object mynewgreet

# #example 7

# def hello(name="jose"):
# 	print("THE HELLO() FUNCTION HAS BEEN RUN!")

# 	def greet():
# 		return "THIS STRING IS INSIDE GREET()"


# 	def welcome():
# 		return "THIS STRING IS INSIDE WELCOME!"
# 	print(greet())
# 	print(welcome())
# 	print("END of hello()")

# welcome()


# example 8

def hello(name="jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME!"

    if name == "jose":
        return greet
    else:
        return welcome

x = hello()  # instantiasi object dari class/def hello

print(x())  # tampilkan object bluprint


# example 9

def hello():
	return "Hi Jose!"


def other(func):
	print("HELLO")

	# func ini dari method other  mengakses propertis langsung dengan method
	print(func())

other(hello)  # ini adalah menampilkan data dari method hello() melalui atau berasal dari method other yang meextend method dari hello


# example 10

def new_decorator(func):  # parameter dekorator func


	def wrap_func():
		print("CODE HERE BEFORE EXECUTING FUNC")
		func()  # parameter decorator
		print("FUNC() HAS BEEN CALLED")  # print method func() jika dekorator berhasil dipanggil
	return wrap_func

def func_needs_decorator(): # fungsi ini butuh dekorator baru untuk dipanggil
	print("THIS FUNCTION IS IN NEED OF A DECORATOR")

func_needs_decorator = new_decorator(func_needs_decorator) #membuat variabel baru dengan func_needs_decorator() method mengambil dekorasi method dari 

func_needs_decorator() #ini panggil dekorator yang dibuat baru



# example 11 cara lain memanggil dekorator

def new_decorator(func):  # parameter dekorator func


	def wrap_func():
		print("CODE HERE BEFORE EXECUTING FUNC")
		func()  # parameter decorator
		print("FUNC() HAS BEEN CALLED")  # print method func() jika dekorator berhasil dipanggil
	return wrap_func

@new_decorator
def func_needs_decorator(): # fungsi ini butuh dekorator baru untuk dipanggil
	print("THIS FUNCTION IS IN NEED OF A DECORATOR")


func_needs_decorator() #panggil fungsi dekorator


