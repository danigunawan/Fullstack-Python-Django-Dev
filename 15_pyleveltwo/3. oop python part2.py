# Example 1
class Dog():

    def __init__(self, breed):
        self.breed = breed

mydog = Dog(breed="Lab")
# otherdog = Dog(breed="Huskie")
print(mydog.breed)
# print(otherdog.breed)

# Example 2


class Dog():

    def __init__(self, breed):
        self.breed = breed

mydog = Dog(breed="Lab")
otherdog = Dog(breed="Huskie")
print(mydog.breed)
print(otherdog.breed)


# Example 3
class Dog():

    # self adalah keyword yang digunakan object Dog() sudah nativenya
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog(breed="Lab", name="Sammy")
print(mydog.breed)  # Lab
print(mydog.name)  # Sammy

# Example 4 + CLASS OBJECT ATRIBUTE


class Dog():

    # CLASS OBJECT ATRIBUTE
    species = "mamal"

    # self adalah keyword yang digunakan object Dog() sudah nativenya
    # Constructor atau method init ini adalah method native dari python
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog(breed="Lab", name="Sammy")
print(mydog.breed)  # Lab
print(mydog.name)  # Sammy
print(mydog.species)  # mamal, diambil dari class object atribute species


# Example 5

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

myc = Circle()  # akses bluprint object class Circle
print(myc.radius)  # kita panggil keyword radius = 1 hasilnya 1

# Example 6

class Circle():
    # Global Variable / Properties nya lah
    pi = 3.14

    #Constructor method Python bawaan
    def __init__(self, radius=1):
        self.radius = radius

    # Buat Method 
    def area(self):
        return self.radius*self.radius *Circle.pi # 1x1x3.14, kita kembalikan fungsi method dengan return dan buat rumus 


myc = Circle(3)  # buat object dan set object = 3
print(myc.area())  # kita panggil method area hasilnya = 3133723.14


# Example 7 Set Radius

class Circle():
    pi = 3.14

    #Constructor method Python bawaan
    def __init__(self, radius=1):
        self.radius = radius

    # Buat Method 
    def area(self):
        return self.radius*self.radius *Circle.pi # 1x1x3.14, kita kembalikan fungsi method dengan return dan buat rumus 
    
    def set_radius(self,new_r): #self harus disertakan disetiap method
        self.radius = new_r

myc = Circle(3)  # buat object dan set object = 3
myc.set_radius(999) # kita gunakan object circle lalu kita set radius yang didapat pada method set_radius
print(myc.area())  # kita panggil method area hasilnya = 3133723.14
