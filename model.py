PATH = 'phone_book.txt'


def show_all():
    with open(PATH, 'r', encoding='UTF-8') as file:
        contacts = file.read().strip()
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
        print(f"\nПользователь №{index3} {k}", end=' --- ')
        print(f"{v[0]}", end=' --- ')
        print(f"{v[1]}")
        index3 += 1

    return ''


def new_contact(contact: str):
    with open(PATH, 'a+', encoding='UTF-8') as file:
        file.write(contact)


def change_contact(book: list):
    file = open(PATH, 'r+', encoding='UTF-8')
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

    file1 = open(PATH, 'r+', encoding='UTF-8')
    lines = file1.read().split('\n')
    file1.seek(0)
    file1.truncate()
    for i in lines:
        if book[0] not in i:
            file1.write(f'\n{i}')
    for line in file1:
        if not line.isspace():
            file1.write(line)

    if book[1].upper() == 'ФИО':
        file1.write(f'\n{book[2]}; ')
        for k, v in dict1.items():
            if book[0] in k:
                ph_inf = dict1.get(k)
                file1.write(f'{ph_inf[0]}; {ph_inf[1]};')
    elif book[1].upper() == 'НОМЕР':
        file1.write(f'\n{book[0]}; {book[3]};')
        for k, v in dict1.items():
            if book[0] in k:
                inf_write = dict1.get(k)[1]
                file1.write(f'{inf_write};')
    elif book[1].upper() == 'ИНФА':
        file1.write(f'\n{book[0]}')
        for k, v in dict1.items():
            if book[0] in k:
                phone_write = dict1.get(k)[0]
                file1.write(f'{phone_write}; {book[4]};')
    file1.close()


def delete_contact(del_contact):
    file = open(PATH, 'r+', encoding='UTF-8')
    lines = file.read().split('\n')
    file.seek(0)
    file.truncate()

    for i in lines:
        if del_contact not in i:
            file.write(f'\n{i}')

    for line in file:
        if not line.isspace():
            file.write(line)

    file.close()
    return ''


def search_contact(find_contact):
    file = open(PATH, 'r', encoding='UTF-8')
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

    for k, v in dict1.items():
        if find_contact in k:
            print(f'\nДанные этого пользователя следующие: '
                  f'\n\tТелефон: {dict1.get(k)[0]}'
                  f'\n\tДоп. инфа: {dict1.get(k)[1]}')

    file.close()
