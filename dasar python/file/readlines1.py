###########################
# Nama file: readlines.py #
###########################

def main():
	# membuka file 
	f = open('data.txt', 'r')
	
	# membaca seluruh data ke dalam bentuk list
	data = f.readlines()
	
	# menelusuri seluruh elemen list
	for elemen in data:
		print(elemen, end='')
	
	# menutup file
	f.close()
	
if __name__ == '__main__':
	main()

