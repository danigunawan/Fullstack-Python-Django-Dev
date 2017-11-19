# Error and Exception
#example 1 error NameError: name 'mylist' is not defined
# mylisthere = [1,2,3]
# print(mylist)

#example 2 

try:
    f = open('simple.txt','w') # 'w' itu menulis = write, r= read setiap kali execute akan diwrite
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
print("hello world!")


#example 3
f = open('simple.txt','w')
f.write("Test write to simple text!")
print("hello world!")
try:
    f = open('simple.txt','w')
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
print("hello world!")   

#example 4
try:
    f = open('simple.txt','w')
    f.write("Test write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I ALWAYS WORK < NO MATTER WHAT")