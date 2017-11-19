#STRINGS

mystring = "abcdefg"

print(mystring)



#INDEXING
##Extract String
print(mystring[0]) #a
print(mystring[1]) #b
print(mystring[2]) #c
print(mystring[3]) #d
print(mystring[4]) #e
print(mystring[5]) #f
print(mystring[6]) #g

#Example 2
print(mystring[0:]) #abcdefg
print(mystring[1:]) #bcdefg
print(mystring[2:]) #cdefg
print(mystring[3:]) #defg
print(mystring[4:]) #efg
print(mystring[5:]) #fg
print(mystring[6:]) #g

#Slicing

#Example 3
print(mystring[0:6]) #abcdef
print(mystring[0:5]) #abcde
print(mystring[0:4]) #abcd
print(mystring[0:3]) #abc
print(mystring[0:2]) #ab
print(mystring[0:1]) #ab
print(mystring[0:0]) #KOSONG

#Example 4
##print(mystring[::0]) #Error
print(mystring[::1]) #abcdefg
print(mystring[::2]) # menghilangkan angka yang urutanya kedua abcdefg = aceg yang hilang bdg
print(mystring[::3]) # menghilangkan angka setelah urutan ketiga berurutan abcdefg = adg 
print(mystring[::4]) # menghilangkan angka setelah urutan keempat berurutan abcdefg = ae 
print(mystring[::5]) #  angka setelah urutan kelima berurutan abcdefg = af 
print(mystring[::6])a #ceg menghilangkan angka setelah urutan keenam berurutan abcdefg = ag 


#example 5
#mystring5 = 'abcdefg'
#mystring5[0] = 'X'  #maka eror TypeError: 'str' object does not support item assignment

#Basic Methods

#example 6 print huruf besar semua dalam variable
mystringhurufbesar = 'abcdefg'
x = mystringhurufbesar.upper()
print(x) #ABCDEFGH

#example 7 print huruf kecil semua dalam variable
mystringhurufkecil = 'ABCDEFGH'
kecilhuruf = mystringhurufkecil.lower()
print(kecilhuruf) #abcdefg

#example 8 print huruf kapital variable
mystringkapital = 'abcdefg'
kapital = mystringkapital.capitalize()
print(kapital) #Abcdefg

#example 9 split print huruf
mystringsplit = 'Hello World'
split = mystringsplit.split('e')
print(split) #['H', 'llo World'] displit



#Print Formatting
#example 10 
cobalagi = "Insert Another string here: {}".format("INSERT ME!") #{} ini print format array 1 diisi dengan INSERT ME! 
print(cobalagi)

#example 11
cobalagi2 = "Item One: {} Item Two: {}".format("dog item 1","dog item 2") #array 1 Item One: {} = "Dog item 1" , array 1 Item Two: {} = "Dog item 2"
print(cobalagi2)


#example 12
cobalagi2 = "Item One: {data1} Item Two: {data2}".format(data1="data item 1",data2="data item 2") #array 1  Item One: {data1} pasingan untuk data1 = "data item 1" dan array 2  Item two: {data2} pasingan untuk data2 = "data item 2" 
print(cobalagi2)