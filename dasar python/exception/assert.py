########################
# Nama file: assert.py #
########################

a = float(input('Masukkan nilai a: '))
b = float(input('Masukkan nilai b: '))

#if b == 0:
#	raise AssertionError('Kesalahan: nilai b tidak bole 0')
assert b != 0, 'Kesalahan: nilai b tidak boleh 0'

c = a / b
print('%.3f / %.3f = %.3f' % (a, b, c))
