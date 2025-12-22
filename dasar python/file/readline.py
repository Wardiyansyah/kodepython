##########################
# Nama file: readline.py #
##########################

def main():
	# membuka file
	f = open('data.txt', 'r')
	
	# membaca data pertama
	baris1 = f.readline()
	
	# membaca data kedua
	baris2 = f.readline()
	
	# membaca data ketiga
	baris3 = f.readline()
	
	# membaca data keempat
	baris4 = f.readline()
	
	# menampilkan data
	print(baris1, end='')
	print(baris2, end='')
	print(baris3, end='')
	print(baris4, end='')
	
	# menutup file
	f.close()
	
if __name__ == '__main__':
	main()
