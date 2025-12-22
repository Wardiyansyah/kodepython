##########################
# Nama file: variabel.py #
##########################

def main():
	a = 13
	b =45.67
	
	print('Sebelum diubah:')
	print('Nilai a\t\t:', a)
	print('Nilai b\t\t:', b)
	print('Tipe data a\t:', type(a))
	print('Tipe data b\t:', type(b))
	print('Identitas a\t:', id(a))
	print('Identitas b\t:', id(b))
	
	# mengubah variabel a dan b untuk menunjuk objek lain
	a = 'Python'
	b = True
	
	print('Setelah diubah:')
	print('Nilai a\t\t:', a)
	print('Nilai b\t\t:', b)
	print('Tipe data a\t:', type(a))
	print('Tipe data b\t:', type(b))
	print('Identitas a\t:', id(a))
	print('Identitas b\t:', id(b))
	
	x = 13
	y = 26
	print(f"{x} dan {y}")
    print("%s" % a)
    

if __name__ == '__main__':
	main()
