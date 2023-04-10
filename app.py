
def show_all():
    file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
                '\\Semenars\\phone_numbers.txt', 'r', encoding='UTF-8')
    contacts = file.read()
    if contacts.endswith(';'):
        contacts = contacts.rstrip(contacts[-1])
    contacts_structured = contacts.split(';')
    dict1 = {}
    index1 = 1
    index2 = 2

    for i in range(0, len(contacts_structured), 3):
        dict1.setdefault(contacts_structured[i],
                         (contacts_structured[index1],
                          contacts_structured[index2]))
        i += 3
        index1 += 3
        index2 += 3

    index3 = 1
    for k, v in dict1.items():
        print(f"\nПользователь №{index3} {k}", end=' -- ')
        print(f"Номер телефона: {v[0]}", end=' -- ')
        print(f"Доп. информация: {v[1]}")
        index3 += 1
    file.close()
    return '\nГотово! Информация успешно выведена'


def new_contact():
    file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
                '\\Semenars\\phone_numbers.txt', 'a+', encoding='UTF-8')
    new_name = input('Введите имя нового контакта: ')
    new_number = input('Введите номер телефона: ')
    new_info = input('Введите доп. информацию: ')
    create_contact = file.write(f'\n{new_name}; {new_number}; {new_info};')
    file.close()
    return 'Готово!'


def delete_contact():
    file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
                '\\Semenars\\phone_numbers.txt', 'r+', encoding='UTF-8')
    lines = file.read().split('\n')
    remove_contact = input('Введите ФИО контакта: ')
    file.seek(0)
    file.truncate()
    for i in lines:
        if remove_contact not in i:
            file.write(f'\n{i}')
    for line in file:
        if not line.isspace():
            file.write(line)
    file.close()


def change_contact():
    file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
                '\\Semenars\\phone_numbers.txt', 'r+', encoding='UTF-8')
    contacts = file.read()
    if contacts.endswith(';'):
        contacts = contacts.rstrip(contacts[-1])
    contacts_structured = contacts.split(';')
    dict1 = {}
    index1 = 1
    index2 = 2

    for i in range(0, len(contacts_structured), 3):
        dict1.setdefault(contacts_structured[i],
                         (contacts_structured[index1],
                          contacts_structured[index2]))
        i += 3
        index1 += 3
        index2 += 3

    file.close()

    file1 = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
                 '\\Semenars\\phone_numbers.txt', 'r+', encoding='UTF-8')

    lines = file1.read().split('\n')
    remove_contact = input('\nВведите ФИО редактируемого контакта: ')
    file1.seek(0)
    file1.truncate()
    for i in lines:
        if remove_contact not in i:
            file1.write(f'\n{i}')
    for line in file1:
        if not line.isspace():
            file1.write(line)

    info_to_change = input('\nКакие данные будем менять? (ФИО, номер, инфа): ')
    if info_to_change.upper() == 'ФИО':
        new_name = input('\nКакими будут новые ФИО?: ')
        file1.write(f'\n{new_name}; ')
        for k, v in dict1.items():
            if remove_contact in k:
                ph_inf = dict1.get(k)
                file1.write(f'{ph_inf[0]}; {ph_inf[1]};')
    elif info_to_change.upper() == 'НОМЕР':
        new_phone = input('Напишите новый номер: ')
        file1.write(f'\n{remove_contact}; {new_phone};')
        for k, v in dict1.items():
            if remove_contact in k:
                inf_write = dict1.get(k)[1]
                file1.write(f'{inf_write};')
    elif info_to_change.upper() == 'ИНФА':
        new_info = input('Напишите новые данные: ')
        file1.write(f'\n{remove_contact}')
        for k, v in dict1.items():
            if remove_contact in k:
                phone_write = dict1.get(k)[0]
                file1.write(f'{phone_write}; {new_info};')

    file1.close()
    return '\nОперация выполнена!'


def search_contact():
    file = open('C:\\Users\\Sasha\\PycharmProjects\\pythonProject'
                '\\Semenars\\phone_numbers.txt', 'r+', encoding='UTF-8')
    contacts = file.read()
    if contacts.endswith(';'):
        contacts = contacts.rstrip(contacts[-1])
    contacts_structured = contacts.split(';')

    dict1 = {}
    index1 = 1
    index2 = 2

    for i in range(0, len(contacts_structured), 3):
        dict1.setdefault(contacts_structured[i],
                         (contacts_structured[index1],
                          contacts_structured[index2]))
        i += 3
        index1 += 3
        index2 += 3

    user_search = input('\nВведите ФИО искомого контакта: ')
    for k, v in dict1.items():
        if user_search in k:
            print(f'Данные этого пользователя следующие: '
                  f'\n\tТелефон: {dict1.get(k)[0]}'
                  f'\n\tДоп. инфа: {dict1.get(k)[1]}')

    file.close()