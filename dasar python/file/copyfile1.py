###########################
# Nama file: copyfile1.py #
###########################

import os

def main():
	src = 'data.txt'
	dst = 'backup1.txt'
	
	os.system('cp %s %s' % (src, dst))
	
if __name__ == '__main__':
	main()
