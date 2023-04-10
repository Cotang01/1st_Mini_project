import app


def main_menu():
    print('\nГлавное меню\n')
    print('\t1. Показать всю книгу')
    print('\t2. Добавить новый контакт')
    print('\t3. Редактировать контакт')
    print('\t4. Удаление контакта')
    print('\t5. Поиск контакта')
    print('\t6. Показать главное меню')


if __name__ == '__main__':
    main_menu()


while True:
    choice = input('\nВведите пункт меню: ')
    if 0 < choice.isdigit() < 7:
        if int(choice) == 1:
            print(app.show_all())
        if int(choice) == 2:
            app.new_contact()
        if int(choice) == 3:
            app.change_contact()
        if int(choice) == 4:
            app.delete_contact()
        if int(choice) == 5:
            app.search_contact()
        if int(choice) == 6:
            main_menu()
    else:
        print('\nВводимое должно быть числом, попробуйте снова ')
