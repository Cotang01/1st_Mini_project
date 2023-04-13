import text_fields as txt


def main_menu() -> int:
    print(txt.main_menu)
    while True:
        choice = input(txt.choice)
        if choice.isdigit() and 0 < int(choice) < 6:  # Именно в таком порядке
            return int(choice)


def new_contact() -> str:
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    info = input(txt.new_info)
    return f'\n{name};{phone};{info};'


def change_contact() -> list:
    remove_contact = input(txt.change_contact)
    info_to_change = input(txt.info_to_change)
    name_change = input(txt.name_change)
    phone_change = input(txt.phone_change)
    info_change = input(txt.info_change)
    return [remove_contact, info_to_change, name_change, phone_change,
            info_change]


def delete_contact() -> str:
    del_contact = input(txt.remove_contact)
    return del_contact


def find_contact() -> str:
    contact_search = input(txt.find_contact)
    return contact_search
