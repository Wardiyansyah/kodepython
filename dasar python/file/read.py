######################
# Nama file: read.py #
######################

def main():
	# membuka file
	f = open('data.txt', 'r')
	
	# membaca data dari dalam file
	data = f.read()
	
	# menampilkan isi data ke layar
	print(data)
	
	# menutup file
	f.close()
	
if __name__ == '__main__':
	main()
