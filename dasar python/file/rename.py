########################
# Nama file: rename.py #
########################

import os 

def main():
	oldName = 'data.txt'
	newName = 'mydata.txt'
	
	os.rename(oldName, newName)
	
if __name__ == '__main__':
	main()
