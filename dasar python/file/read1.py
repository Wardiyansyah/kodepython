#######################
# Nama file: read1.py #
#######################

def main():
	# membuka file
	f = open('data.txt', 'r')
	
	# membaca data dari dalam file
	data = f.read()
	
	# mengonversi data ke dalam bentuk raw string
	rawData = data.encode('unicode-escape')
	
	# menampilkan isi data ke layar
	print(rawData)
	
	# menutup file
	f.close()
	
if __name__ == '__main__':
	main()

