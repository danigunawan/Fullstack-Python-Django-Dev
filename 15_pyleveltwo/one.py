# latihan 10.name and main.py


def func():
    print("func() in one.py")

print("TOP LEVEL ONE.PY")

if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py has been imported")


# jika one.py di run maka  hasilnya:
# TOP LEVEL ONE.PY
# one.py is being run directly


# jika two.py dirun maka hasilnya
# TOP LEVEL ONE.PY
# one.py has been imported
# TOP LEVEL TWO.PY
# func() in one.py
# Two.py being run directly
