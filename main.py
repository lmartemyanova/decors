from tests.test_1 import test_1
from tests.test_2 import test_2
from phonebook.phonebook import get_contacts_list, format_initials, format_phone, delete_duplicates, fill_phonebook


if __name__ == '__main__':
    test_1()
    test_2()
    contacts_list = get_contacts_list()
    for i, contact in enumerate(contacts_list):
        contacts_list[i] = format_initials(contact)
        contacts_list[i][5] = format_phone(contact[5])
    correct_phonebook = delete_duplicates(contacts_list)
    fill_phonebook(correct_phonebook)
