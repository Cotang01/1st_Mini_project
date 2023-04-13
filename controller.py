import view
import model
import text_fields as txt


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.show_all()
                print(txt.pb_open)
            case 2:
                contact = view.new_contact()
                model.new_contact(contact)
            case 3:
                contact_changes = view.change_contact()
                model.change_contact(contact_changes)
                print(txt.pb_change_contact)
            case 4:
                del_contact = view.delete_contact()
                model.delete_contact(del_contact)
                print(txt.pb_delete_contact)
            case 5:
                find_contact = view.find_contact()
                model.search_contact(find_contact)
                print(txt.pb_search_contact)
