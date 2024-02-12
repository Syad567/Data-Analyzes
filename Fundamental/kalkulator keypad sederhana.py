print('operasi MTK')
print(' 1. jumlah \t [+]')
print(' 2. kurang \t [-]')
print(' 3. kali \t [*]')
print(' 4. bagi \t [/]')

operasi = input('pilih operasi (1/2/3/4): ')
bilangan_1 = eval(input('masukan angka pertama: '))
bilangan_2 = eval(input('masukan angka kedua: '))

if operasi == '1':
    hasil = bilangan_1 + bilangan_2
    print(f'hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')

elif operasi == '2':
    hasil = bilangan_1 - bilangan_2
    print(f'hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')

elif operasi == '3':
    hasil = bilangan_1 * bilangan_2
    print(f'hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')

elif operasi == '4':
    hasil = bilangan_1 / bilangan_2
    print(f'hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')

else:
    print('invalid')


