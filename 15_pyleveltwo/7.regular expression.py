# REGEX
#syarat harus import re (regular expression)
import re

#example 1
patterns = ['term1', 'term2']

text = 'this is a string with term1, not not the other!'

for pattern in patterns:
    print("im searching for:" + pattern)

#example 2
patterns = ['term1', 'term2']

text = 'this is a string with term1, not not the other!'

for pattern in patterns:
    print("im searching for:" + pattern)

    if re.search(pattern,text): #regular expression dengan fungsi search (re.search)
    	print("match")
    else:
    	print("no match")

#example 3
text = 'this is a string with term1, not not the other!'

match = re.search('term1',text) # mencari dengan regular expression

print(type(match)) #<class '_sre.SRE_Match'> tipe data string regular expression

#example 4
text = 'this is a string with term1, not not the other!'

match = re.search('term1',text) # mencari dengan regular expression

print(match.start()) #22 pencarian regex hasilnya

#example 5

split_term = '@'
email = 'user@gmail.com'
print(re.split(split_term,email)) #['user', 'gmail.com'] jadi menghilangkan @ dan memisahkan user dan gmail.com dengan list array ['user','gmail.com']


#example 6

print(re.findall('match','test phrase match in middle')) #mencari match dijadikan list array hasilnya['match']

#example 7

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'sdsd..sssddd..sddddsddd...dsds...dssssss...sddddd'

test_pattern = ['sd*']

multi_re_find(test_pattern,test_phrase)#['sd', 'sd', 's', 's', 'sddd', 'sdddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sddddd']


#example 8

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'sdsd..sssddd..sddddsddd...dsds...dssssss...sddddd'

test_pattern = ['sd+'] # mencari string sd dan + gabungan atau string selanjutnya akan diambil contoh sda, sds dsb

multi_re_find(test_pattern,test_phrase) #['sd', 'sd', 'sddd', 'sdddd', 'sddd', 'sd', 'sddddd']

#example 8

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'sdsd..sssddd..sddddsddd...dsds...dssssss...sddddd'

test_pattern = ['sd?'] # mencari string hanya bernilai sd  atau s dan d selain itu tidak dicari

multi_re_find(test_pattern,test_phrase) #['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sd']

#example 9

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'sdsd..sssddd..sddddsddd...dsds...dssssss...sddddd'

test_pattern = ['sd{3}']

multi_re_find(test_pattern,test_phrase) #['sddd', 'sddd', 'sddd', 'sddd']



#example 10

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'sdsd..sssddd..sddddsddd...dsds...dssssss...sddddd'

test_pattern = ['sd{1,3}']

multi_re_find(test_pattern,test_phrase) #['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddd']



#example 11

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'sdsd..sssddd..sddddsddd...dsds...dssssss...sddddd'

test_pattern = ['sd[sd]+']

multi_re_find(test_pattern,test_phrase) #['sdsd', 'sddd', 'sddddsddd', 'sds', 'sddddd']

#example 12

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'This is a string! But is has punctuation. How can we remove it?'
test_pattern = ['[^!.?]+'] # menghilangkan ! dan ? dengan fungsi ^

multi_re_find(test_pattern,test_phrase) #['This is a string', ' But is has punctuation', ' How can we remove it']

#example 13

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'This is a string! But is has punctuation. How can we remove it?'

test_pattern = ['[a-z]+'] # mencari huruf a sampai z dan + gabungan huruf selanjutnya

multi_re_find(test_pattern,test_phrase) #['his', 'is', 'a', 'string', 'ut', 'is', 'has', 'punctuation', 'ow', 'can', 'we', 'remove', 'it']


#example 14

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'This is a string! But is has punctuation. How can we remove it?'

test_pattern = ['[A-Z]+'] # mencari huruf A sampai Z Yang kapital atau beserta gabungan huruf selanjutnya yang kapital

multi_re_find(test_pattern,test_phrase) #['T', 'B', 'H']

#example 15

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'This is a string with number 12312 and a symbol #hashtag'

test_pattern = [r'\d+'] # mencari nilai number saja yang diambil dijadikan list array

multi_re_find(test_pattern,test_phrase) #['12312']

#example 16

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'This is a string with number 12312 and a symbol #hashtag'

test_pattern = [r'\D+'] # menghilangkan number pada kalimat string diatas

multi_re_find(test_pattern,test_phrase) #['This is a string with number ', ' and a symbol #hashtag']

#example 17

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'This is a string with number 12312 and a symbol #hashtag'

test_pattern = [r'\s+'] # s mengambil nilai spasi saja isi dari string atau number tidak diambil, space ini dijadikan array list []

multi_re_find(test_pattern,test_phrase) #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


#example 18

def multi_re_find(patterns,phrase):
	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))
		print('\n')

test_phrase = 'This is a string with number 12312 and a symbol #hashtag'

test_pattern = [r'\W+'] # W ini mengambil simbol saja yang lainnya tidak dan dijadikan array list sesuai panjang string pada regex

multi_re_find(test_pattern,test_phrase) #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #']

