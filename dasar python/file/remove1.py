########################
# Nama file: remove.py #
########################

import os

def main():
	fileName = 'backup.txt'
	
	os.system('rm %s' % fileName)
	
if __name__ == '__main__':
	main()

