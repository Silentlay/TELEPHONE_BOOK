from logger import input_data, print_data, edit_data, delete_data

def interface():
    print("\nДобрый день! Вы попали на специальный бот справочник от GeekBrains!")
    while True:
        print("\n1 - запись данных")
        print("2 - вывод данных")
        print("3 - редактирование данных")
        print("4 - удаление данных")
        print("5 - выход")
        command = input('\nВведите число: ')

        if command == '1':
            input_data()
            print("\nДанные успешно записаны!")
        elif command == '2':
            print_data()
        elif command == '3':
            edit_data()
           
        elif command == '4':
            delete_data()
            
        elif command == '5':
            print("\nВыход программы.")
            break
        else:
            print('\n! Неправильный ввод. Пожалуйста выберете 1, 2, 3, 4, или 5.')

if __name__ == '__main__':
    interface()
