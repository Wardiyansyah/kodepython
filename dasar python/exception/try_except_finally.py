####################################
# Nama file: try_except_finally.py #
####################################

f = None
status = True
fileName = input('Masukkan nama file yang akan dibaca: ')

try:
	f = open(fileName)
	data = f.read()
	print(data)
except FileNotFoundError as e:
	status = False
	print('Kesalahan: file \'%s\' tidak ditemukan.' % fileName)
finally:
	if f is not None:
		f.close()
	if not status:
		print('operasi dibatalkan...')
	else:
		print('operasi selesai...')
	
