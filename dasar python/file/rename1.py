#########################
# Nama file: rename1.py #
#########################

import os

def main():
	oldName = 'data.txt'
	newName = 'mydata.txt'
	
	os.system('mv %s %s' % (oldName, newName))
	
if __name__ == '__main__':
	main()
