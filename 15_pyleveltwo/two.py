# latihan 10.name and main.py
import one # ini dari one.py

print("TOP LEVEL TWO.PY")
one.func() # mengambil method dari one.py yakni func() maka setelah import one, untuk menggunakan method tersebut/panggil dengan one.func()
# jadi akan memanggil seluruh fungsi dari one.py dari method func()

#selanjutnya menampilkan argument dari two.py
# logic
if __name__ == '__main__':
	print("Two.py being run directly")
else:
	print("two is being imported")

#jika one.py di run maka  hasilnya:
#TOP LEVEL ONE.PY
#one.py is being run directly


#jika two.py dirun maka hasilnya 
# TOP LEVEL ONE.PY
# one.py has been imported
# TOP LEVEL TWO.PY
# func() in one.py
# Two.py being run directly


#kasusnya jika di two.py method one.func() akan membaca file yang terimport sekaligus menjalankan method func() maka dari itu argument
#pada one.py  if __name__ == '__main__': akan bernilai print("one.py has been imported"), namun jika diakses didalam methodnya sendiri atau file name sendiri maka dia akan bersifat directly