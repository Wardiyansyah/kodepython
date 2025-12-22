###########################
# Nama file: readlines.py #
###########################

def main():
	# membuka file 
	f = open('data.txt', 'r')
	
	# membaca seluruh data ke dalam bentuk list
	data = f.readlines()
	
	# menampilkan data dalam bentuk list
	print(data)
	
	# menutup file
	f.close()
	
if __name__ == '__main__':
	main()
