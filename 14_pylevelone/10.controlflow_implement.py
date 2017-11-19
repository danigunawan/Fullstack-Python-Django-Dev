###### COMPARISON OPERATOR

## Example 1
if 1 < 2 :
	print('yes!')


## Example 2
if 1 < 2 :
	if 2 < 3:
		print ("True") ## Jika kedua kondisi bernilai benar maka print true

## Example 3
if 1 < 2 :
	print ('first block')
	if 2 < 3:
		print ("True") ## Jika kedua kondisi bernilai benar maka print true

## Example 4 if else kondisi

if 1 < 2 :
	print ('first block')
	if 20 < 3: #tidak akan tampil karena tidak memenuhi logic 
		print ("True") ## Jika kedua kondisi bernilai benar maka print true


## Example 5 
if 1 < 2 :
	print("hello") # maka benar hello
else:
	print("Last")

## Example 6
if 1 > 2 :
	print("hello") # Salah
elif 3 == 3:
	print("elif ran") # Benar ini yang diprint
else:
	print("Last") # jika salah maka tidak di print

## For Loops
# Example 7 
seq = [1,2,3,4,5,6]

for data1 in seq:
	#Code Here
	print('Hello') # Hello  6x

# Example 8 
seq = [1,2,3,4,5,6]

for data1 in seq: # untuk data1 dari variabel seq
	#Code Here
	print(data1)  # 1,2,3,4,5,6


# Example 9
d = {"Sam":1, "Frank":2,"Dan":3}  #untuk datakey dari variabel dictionary d

for datakey in d:
	#Code Here
	print(datakey) #Sam, Frank, Dan

# Example 10
d = {"Sam":1, "Frank":2,"Dan":3}  #untuk k dari variabel dictionary d

for k in d:
	#Code Here
	print(k) #Sam, Frank, Dan
	print(d[k]) #1,2,3 ini hanya mengambil key nya saja untk

# example 11

mypairs = [(1,2),(3,4),(5,6)]

for(tup1, tup2) in mypairs :
	print(tup1) # 1,3,5
	print(tup2) # 2,4,6
	#jika digabung menjadi 1,2,3,4,5,6

# example 12
i = 1

while i<5: # berarti 0,1,2,3,4 = 5 kali
	print("i is: {}".format(i))
	i = i +1 # jadi selama 5x 0,1,2,3,4 ditambah 1 jadi 0+1,1+1,2+1,3+1 sampai empat saja karena dalam perhitungan loop begitu

## RANGE

#example 13
#Code in terminal
# [1,2,3,4,5]
# range(5) # range(0,5)
# list(range(0,5)) # [0,1,2,3,4]
# list(range(0,20,2)) #[0,2,4,6,8,12,14,16,18]
# list(range(0,21,2)) #[0,2,4,6,8,12,14,16,18,20]
# range(10000000) #range(0,10000000)
# quit()

# Example 14
for item in range(10): # range(10) ini menghasilkan range(0,10) atau 0 s/d 10
	print(item) # 0,1,2,3,4,5,6,7,8,9

## List Comprehension

#Example 15
x = [1,2,3,4]
out = []

for num in x:
	out.append(num**2) # maksudnya num**2 kelipatan 2 jadi [1x1] = 1, [1x1, 2x2], [1x1, 2x2, 3x3], [1x1, 2x2, 3x3, 4x4]
	print(out)
#maka hasilnya
# [1]
# [1, 4]
# [1, 4, 9]
# [1, 4, 9, 16]

#Example 16
x = [1,2,3,4]
out = [num**2 for num in x]
print(out) #[1, 4, 9, 16]
 
