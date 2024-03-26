import os
from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    
    while True:
        var = input(f"\nВ каком формате записать данные?\n\n"
                    f"Вариант 1: \n\n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"Вариант 2:\n\n"
                    f"{name};{surname};{phone};{address}\n"
                    f"\nВыберете вариант: ")

        if var == '1' or var == '2':
            break 

        print('\n Неправильный ввод. Введите число 1 или 2.')

    try:
        var = int(var)
    except ValueError:
        print()
        print('\n! Неправильный ввод. Введите число 1 или 2.')
        return

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    try:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.read().strip().split('\n\n')
            if data_first[0]: 
                print('\nВывожу данные из 1 файла:')
                for i, record in enumerate(data_first, start=1):
                    print(f"\nЗапись {i}.\n")
                    print(record)
            else:
                print("\n! У вас пока нет записей в первом файле.")
    except FileNotFoundError:
        print("Файл data_first_variant.csv не существует.")

    try:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = [line.strip() for line in f.readlines() if line.strip()]
            if data_second:
                print('\nВывожу данные из 2 файла:')
                for i, record in enumerate(data_second, start=1):
                    print(f"\nЗапись {i}.\n\n{record}")
            else:
                print("\n! У вас пока нет записей во втором файле.")
    except FileNotFoundError:
        print("Файл data_second_variant.csv не существует.")


def edit_data():
    print("\nВыберите файл, в котором нужно отредактировать запись:\n")
    print("1. data_first_variant.csv")
    print("2. data_second_variant.csv")
    
    while True:  
        file_choice = input("\nВведите номер файла - 1 или 2: ")
        if file_choice == '1' or file_choice == '2':
            break  
        print('\n! Неправильный ввод. Введите число 1 или 2.')

    if file_choice == "1":
        try:
            with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
                data_first = f.read().strip().split('\n\n')
                if not data_first[0]:  
                    print("\n! У вас пока нет записей для редактирования в первом файле.")
                    return
                print('\nВывожу данные из 1 файла:')
                for i, record in enumerate(data_first, start=1):
                    print(f"\n\nЗапись {i}.\n")
                    print(record)
        except FileNotFoundError:
            print("Файл data_first_variant.csv не существует.")
            return
        
    elif file_choice == "2":
        try:
            with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
                data = [line.strip() for line in f.readlines() if line.strip()]
                if not data:  
                    print("\n! У вас пока нет записей для редактирования во втором файле.")
                    return
                print('\nВывожу данные из 2 файла:')
                for i, record in enumerate(data, start=1):
                    print(f"\nЗапись {i}.\n\n{record}")
        except FileNotFoundError:
            print("\nФайл data_second_variant.csv не существует.")
            return
    else:
        print("\n! Неверный выбор файла.")
        return

    while True:  
        record_choice = input("\nВведите номер записи для редактирования: ")
        try:
            record_index = int(record_choice) - 1
            if file_choice == "1":
                if record_index < 0 or record_index >= len(data_first):
                    print("\n! Неверный номер записи.")
                else:
                    break  
            elif file_choice == "2":
                if record_index < 0 or record_index >= len(data):
                    print("\n! Неверный номер записи.")
                else:
                    break
        except ValueError:
            print("\n! Неверный номер записи.")

    name = input('\nВведите новое имя: ')
    surname = input('Введите новую фамилию: ')
    phone = input('Введите новый телефон: ')
    address = input('Введите новый адрес: ')

    if file_choice == "1":
        new_record = f"{name}\n{surname}\n{phone}\n{address}"
        data_first[record_index] = new_record
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(data_first) + '\n\n') 
    elif file_choice == "2":
        new_record = f"{name};{surname};{phone};{address}"
        data[record_index] = new_record
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for record in data:
                f.write(record.strip() + '\n\n')  

    print("\nЗапись успешно отредактирована и сохранена.")


def delete_data():
    print("\nВыберите файл, из которого нужно удалить запись:\n")
    print("1. data_first_variant.csv")
    print("2. data_second_variant.csv")
    
    while True:  
        file_choice = input("\nВведите номер файла - 1 или 2: ")
        if file_choice == '1' or file_choice == '2':
            break  
        print('\n! Неправильный ввод. Введите число 1 или 2.')

    if file_choice == "1":
        try:
            with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
                data_first = f.read().strip().split('\n\n')
                if not data_first[0]:  
                    print("\n! В выбранном файле пока нет записей для удаления.")
                    return
                print('\nВывожу данные из 1 файла:')
                for i, record in enumerate(data_first, start=1):
                    print(f"\nЗапись {i}.\n")
                    print(record)
        except FileNotFoundError:
            print("Файл data_first_variant.csv не существует.")
            return
        
    elif file_choice == "2":
        try:
            with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
                data = [line.strip() for line in f.readlines() if line.strip()]
                if not data:  
                    print("\n! В выбранном файле пока нет записей для удаления.")
                    return
                print('\nВывожу данные из 2 файла:')
                for i, record in enumerate(data, start=1):
                    print(f"\nЗапись {i}.\n\n{record}")
        except FileNotFoundError:
            print("\nФайл data_second_variant.csv не существует.")
            return
    else:
        print("\n! Неверный выбор файла.")
        return

    while True:  
        record_choice = input("\nВведите номер записи для удаления: ")
        try:
            record_index = int(record_choice) - 1
            if file_choice == "1":
                if record_index < 0 or record_index >= len(data_first):
                    print("\n! Неверный номер записи.")
                else:
                    break  
            elif file_choice == "2":
                if record_index < 0 or record_index >= len(data):
                    print("\n! Неверный номер записи.")
                else:
                    break
        except ValueError:
            print("\n! Неверный номер записи.")

   
    if file_choice == "1":
        del data_first[record_index]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            if len(data_first) > 0: 
                f.write('\n\n'.join(data_first) + '\n\n') 
    elif file_choice == "2":
        del data[record_index]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for record in data:
                f.write(record.strip() + '\n\n')

    print("\nЗапись успешно удалена.")







   