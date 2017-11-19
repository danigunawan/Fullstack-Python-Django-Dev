#List
#example 1
#mylist = [1,2,3]
mylist = ['ssadsadsadsasa',1,2,3,2.1, True, 'dsasa',[1,2,3]]
print(len(mylist)) #panjang karakter indexing = 8

#example 2
mylist2 = ['a','b','c','d','e']
print(mylist2[1:]) # a dskip mulai dari index ['b', 'c', 'd', 'e'] 

#example 3
mylist3 = ['a','b','c','d','e']
print(mylist3[:3]) # hanya diambil 3 index awal ['a', 'b', 'c']

#example 4
mylist4 = ['a','b','c','d','e']
print('before assigment') #sebelum penempatan atau assigment
print(mylist4) # bentuk print awal array  ['a','b','c','d','e']
mylist4[0] = 'New Item' # jadi 0 ini adalah array pertama untuk menggantikan posisi si 'a' pada  ['a','b','c','d','e']
print('after assigment') #sesudah penempatan atau assigment
print(mylist4) #  ['New Item','b','c','d','e']

#example 5
mylist5 = ['a','b','c','d','e']
mylist5.append("New Item") #append ini adalah memasukan array berikutnya yakni setelah 'e' maka hasil pada print ['a', 'b', 'c', 'd', 'e', 'New Item']
print(mylist5)  #['a', 'b', 'c', 'd', 'e', 'New Item']

#example 6
mylist6 = ['a','b','c','d','e']
mylist6.append(["x",'y','z']) #append ini adalah memasukan stdclass object array berikutnya yakni setelah 'e' maka hasil pada print ['a', 'b', 'c', 'd', 'e', 'New Item']
print(mylist6)  #['a', 'b', 'c', 'd', 'e', ['x', 'y', 'z']]

#example 7
mylist7 = ['a','b','c','d','e']
listtwo7 = ["x",'y','z']
mylist7.extend(listtwo7) #extend ini adalah memasukan list array berikutnya yakni setelah 'e' maka hasil pada print ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']
print(mylist7) #['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']

#example 8
mylist8 = ['a','b','c','d','e']
item = mylist8.pop(0)#funsgi pop ini memisahkan array terakhir yakni 'e' untuk dijadikan item baru
print(mylist8) #['a', 'b', 'c', 'd']
print(item) # e


#example 9
mylist9 = ['a','b','c','d','e']
item = mylist9.pop(0)#funsgi pop dengan parameter array 0 = pertama ini memisahkan array terakhir yakni 'a' untuk dijadikan item baru
print(mylist9) #['b', 'c', 'd','e']
print(item) # a

#example 10
mylist10 = ['a','b','c','d','e']
item = mylist10.reverse()#funsgi reverse ini membalikan urutan array dari awal hingga akhir
print(mylist10) #['e', 'd', 'c', 'b', 'a']

#example 11
mylist11 = [4,5,7,4,2,6,3]
item = mylist11.sort()#funsgi sort ini mengurutkan array 
print(mylist11) #[2, 3, 4, 4, 5, 6, 7]

#example 12
mylist12 = [1,2,['x','y','z']]
print(mylist12[0]) # hasilnya array 0 pertama = 1
print(mylist12[1]) # hasilnya array 1 kedua = 2
print(mylist12[2]) # hasilnya array ketiga percabangan #['x','y','z']
print(mylist12[2][0]) # hasilnya x yakni didapat dari array ketiga percabangan mengakses data pertama 'x' #['x','y','z']

#example 13
matrix = [[1,2,3],[4,5,6],[7,8,9]]
kolom_pertama = [row[0] for row in matrix] # mengakses kolom pertama dari matrix yakni 1,4,7
print(kolom_pertama) # [1, 4, 7]


