 # INHERITANCE

# example 1
class Animal():
    # buat construct method native python

    def __init__(self):
        print("ANIMAL CREATED")
    # buat method method

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print('EATING')

# INSTANTIASI OBJECT
mya = Animal() #kita instantiasi object agar bisa diakses
mya.whoAmI() #kita akses method whoAmI pada object Animal
mya.eat() #kita akses method eat pada object Animal

# INHERITANCE

# example 2


class Animal():
    # buat construct method native python

    def __init__(self):
        print("ANIMAL CREATED")
    # buat method method

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print('EATING')

class Dog(Animal): # Class Dog disini adalah child class atau anak kelas turunan dari Animal / extends prinsip oop pewarisan sifat
    #Construct initialisasi method python
    def __init__(self):
        # Animal.__init__(self)
        print("DOG CREATED")
    def bark(self):
        print("WOOF")
# INSTANTIASI OBJECT ANIMAL
mya = Animal() #kita instantiasi object agar bisa diakses
mya.whoAmI() #kita akses method whoAmI pada object Animal
mya.eat() #kita akses method eat pada object Animal

# INSTANTIASI OBJECT DOG
mydog = Dog() # instantiasi object dog
mydog.whoAmI() # bisa akses whoAmI karena di extends dari kelas parent nya / induknya Animal yang memiliki method whoAmI
mydog.eat() # bisa akses whoAmI karena di extends dari kelas parent nya / induknya Animal yang memiliki method eat, jika kita buat method di kelas sendiri Dog() maka yang di execute adalah method pada kelas sendiri terlebih dahulu yakni method eat() pada kelas Dog() jika tidak ada method eat() pada kelas Dog() maka yg diexecute eat() adalah pada induknya yakni Animal() 
mydog.bark() # method yang diakses dari keleasnya sendiri Dog()


# example 2 
# jika kita buat method di kelas sendiri Dog() maka yang di execute adalah method pada kelas sendiri terlebih dahulu yakni method eat() pada kelas Dog() jika tidak ada method eat() pada kelas Dog() maka yg diexecute eat() adalah pada induknya yakni Animal() 

class Animal():
    # buat construct method native python

    def __init__(self):
        print("ANIMAL CREATED")
    # buat method method

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print('EATING')

class Dog(Animal): # Class Dog disini adalah child class atau anak kelas turunan dari Animal / extends prinsip oop pewarisan sifat
    #Construct initialisasi method python
    def __init__(self):
        # Animal.__init__(self)
        print("DOG CREATED")
    def bark(self):
        print("WOOF")
    def eat(self):
        print("DOG EATING")
# INSTANTIASI OBJECT ANIMAL
mya = Animal() #kita instantiasi object agar bisa diakses baik method maupun properties
mya.whoAmI() #kita akses method whoAmI pada object Animal
mya.eat() #kita akses method eat pada object Animal

# INSTANTIASI OBJECT DOG
mydog = Dog() # instantiasi object dog
mydog.whoAmI() # bisa akses whoAmI karena di extends dari kelas parent nya / induknya Animal yang memiliki method whoAmI
mydog.eat() # bisa akses whoAmI karena di extends dari kelas parent nya / induknya Animal yang memiliki method eat, jika kita buat method di kelas sendiri Dog() maka yang di execute adalah method pada kelas sendiri terlebih dahulu yakni method eat() pada kelas Dog() jika tidak ada method eat() pada kelas Dog() maka yg diexecute eat() adalah pada induknya yakni Animal() 
mydog.bark() # method yang diakses dari keleasnya sendiri Dog()

# SPECIAL METHODS
# example 3

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
b = Book("Python","jose",200) # instantiasi object dan kita set nilai object
print(b) # <__main__.Book object at 0x000000000231D780> object pada memory

mylist = [1,2,3] #[1, 2, 3]
print(mylist)

# example 4
#buat class
class Book():
    #buat constructor method native python dan inisialisasi
    def __init__(self,title,author,pages):
        self.title = title # self keyword title utk didaftarkan pada kelas fungsinya utk membedakan dari method atau fungsi diluar class dan setiap method tsb harus memiliki parameter self
        self.author = author
        self.pages = pages

    def __str__(self): #Pernyataan print dan str() menggunakan __str__ untuk menampilkan representasi objek dalam bentuk string yang dapat dibaca , Reff: https://jinbaskom.wordpress.com/2015/05/10/apa-itu-fungsi-repr-di-python/
        return"Title: {}, author: {}, pages: {}".format(self.title,self.author,self.pages) # agar bisa dibaca secara string tidak secara memory sebelumnya

b = Book("Python","jose",200) # instantiasi object dan kita set nilai object
print(b) # Title: Python, author: jose, pages: 200

mylist = [1,2,3] #[1, 2, 3]
print(mylist)


# example 5
#buat class
class Book():
    #buat constructor method native python dan inisialisasi
    def __init__(self,title,author,pages):
        self.title = title # self keyword title utk didaftarkan pada kelas fungsinya utk membedakan dari method atau fungsi diluar class dan setiap method tsb harus memiliki parameter self
        self.author = author
        self.pages = pages

    def __str__(self): #Pernyataan print dan str() menggunakan __str__ untuk menampilkan representasi objek dalam bentuk string yang dapat dibaca , Reff: https://jinbaskom.wordpress.com/2015/05/10/apa-itu-fungsi-repr-di-python/
        return"Title: {}, author: {}, pages: {}".format(self.title,self.author,self.pages) # agar bisa dibaca secara string tidak secara memory sebelumnya

    #solusi TypeError: object of type 'Book' has no len() pakai def __len__(self)
    def __len__(self):
        return self.pages


b = Book("Python","jose",200) # instantiasi object dan kita set nilai object
print(b) # Title: Python, author: jose, pages: 200

mylist = [1,2,3] #[1, 2, 3]
print(len(b)) # TypeError: object of type 'Book' has no len() jika method def __len__ belum dibuat


# example 6
#buat class
class Book():
    #buat constructor method native python dan inisialisasi
    def __init__(self,title,author,pages):
        self.title = title # self keyword title utk didaftarkan pada kelas fungsinya utk membedakan dari method atau fungsi diluar class dan setiap method tsb harus memiliki parameter self
        self.author = author
        self.pages = pages

    def __str__(self): #Pernyataan print dan str() menggunakan __str__ untuk menampilkan representasi objek dalam bentuk string yang dapat dibaca , Reff: https://jinbaskom.wordpress.com/2015/05/10/apa-itu-fungsi-repr-di-python/
        return"Title: {}, author: {}, pages: {}".format(self.title,self.author,self.pages) # agar bisa dibaca secara string tidak secara memory sebelumnya

    #solusi TypeError: object of type 'Book' has no len() pakai def __len__(self)
    def __len__(self):
        return self.pages

    # def __del__(self) untuk hapus object
    def __del__(self):
        print("a book is destroyed")

b = Book("Python","jose",200) # instantiasi object dan kita set nilai object
print(b) # Title: Python, author: jose, pages: 200

mylist = [1,2,3] #[1, 2, 3]
del b # a book is destroyed // object b dihapus

