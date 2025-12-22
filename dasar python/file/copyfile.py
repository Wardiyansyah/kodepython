##########################
# Nama file: copyfile.py #
##########################

import shutil

def main():
	src = 'data.txt'
	dst = 'backup.txt'
	
	shutil.copyfile(src, dst)
	
if __name__ == '__main__':
	main()
