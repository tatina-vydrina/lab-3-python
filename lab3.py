import sys 
import os

def exit():
    m = input('Вы хотите продолжить? (y/n)') 
    if m == 'y': 
        menu() 
    else: 
        sys.exit()
    
def count_files(): 
    di = input('Введите адрес директории: ')
    print('Файлов в директории:',len([name for name in os.listdir(di) if os.path.isfile(os.path.join(di, name))]))
    exit()

def show_products(): 

    file = open(b'products.txt', 'r')
    n_list = file.read().splitlines()
    file.close()

    for i in range(len(n_list)): 
        n_list[i] = n_list[i].split(';') 

    header = n_list.pop(0)

    print('%3s%20s%10s%20s' % (header[0], header[1], header[2], header[3]))

    n_list.sort(key=lambda x: x[1])

    for elem in n_list:
        print('%3s%20s%10s%20s' % (elem[0], elem[1], elem[2], elem[3]))
        
    exit()
    
def edit_products():

    file = open(b'products.txt', 'r') 
    n_list = file.read().splitlines()
    file.close()

    for i in range(len(n_list)): 
        n_list[i] = n_list[i].split(';') 

    header = n_list.pop(0)

    print('%3s%20s%10s%20s' % (header[0], header[1], header[2], header[3])) 
    n_list.sort(key=lambda x: x[1])

    for elem in n_list:
        print('%3s%20s%10s%20s' % (elem[0], elem[1], elem[2], elem[3]))
    
    print('Введите номера товара через пробел, количество которого хотите изменить:')
    nums = []
    nums = input('>> ').split(' ')
    print('Введите число, которое хотите прибавить к количеству:')
    quantity = input('>> ')

    for elem in n_list:
        if nums.count(elem[0]):
            print('Товар: {}'.format(elem)) 
            elem[3] = str(int(elem[3]) + int(quantity)) 
            print('Измененный товар: {}'.format(elem))
    i = input('Сохранить измененный список товаров в файл? (y/n)')
    
    if i == 'y':
        f = open('products.txt', 'w')
        f.write(str(';'.join(header)) + '\n')
        for elem in n_list: 
           f.write(str(';'.join(elem)) + '\n')
        f.close()
        print('Файл записан!')
        exit()
    else: 
        exit()

def menu():
    print('0 - Выход\n1 - Посчитать файлы в директории\n2 - Вывод информации о товарах, сортированных по названию' '\n3 - Изменение количества товаров указанных номеров')

    m = input('>> ') 
    if m == '0': 
        sys.exit() 
    if m == '1': 
        count_files() 
    if m == '2': 
        show_products() 
    if m == '3': 
        edit_products()


menu()
