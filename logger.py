from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 Вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 Вариант: \n"
                    f"{name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))
        
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('Выводим данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.read().splitlines()
        print(''.join(data_first)) 
        
    print('Выводим данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(''.join(data_second))

def change_data():
    file_name = input("Введите имя файла (data_first_variant.csv или data_second_variant.csv): ")
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        
    print("Текущие данные: ") 
    print(''.join(data))  
    
    line_to_change = int(input("Введите номер строки, которую нужно изменить: ")) - 1
    if 0 <= line_to_change < len(data):
        new_data = input("Введите новые данные в том же формате: ")
        data[line_to_change] = new_data + '\n' 
        
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(data)
        print("Данные изменены.")
        
    else:
        print("Неверный номер строки.")
        
def delete_data():
    file_name = input("Введите имя файла (data_first_variant.csv или data_second_variant.csv):")
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        
    print("Текущие данные:")
    print(''.join(data))
    
    line_to_delete = int(input("Введите номер строки, которую нужно удалить: ")) - 1
    if 0 <=line_to_delete < len(data):
        del data[line_to_delete]
        
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(data)
        print("Данные удалены.")
    else:
        print("Неверный номер строки.")
        
while True:
    print("\nВыберите действия:")
    print("1. Добавить данные")
    print("2. Вывести данные")
    print("3. Изменить данные")
    print("4. Удалить данные")
    print("5. Выход")
    
    choice = input("Введите номер действия: ")
    
    if choice == '1':
        input_data()
    elif choice == '2':
        print_data()
    elif choice == '3':
        change_data()
    elif choice == '4':
        delete_data()
    elif choice == '5':
        break
    else:
        print("Некорректный ввод.")