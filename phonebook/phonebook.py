import os.path
import re
import csv
from logger_2 import logger


@logger('phonebook.log')
def get_contacts_list():

    """
    Reads the raw phonebook CSV file and returns a list of contacts.
    Each contact is represented as a list of strings.
    :return: list of contacts (list of lists of strings)
    """

    with open(os.path.join(os.getcwd(), 'phonebook', "phonebook_raw.csv"), encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


@logger('phonebook.log')
def format_initials(contact):

    """
    Formats the name fields of a contact to have three parts: last name, first name, and middle name.
    :param contact (list of strings).
    :return: list of strings representing the formatted contact.
    """

    fields = contact[3:]
    names = ' '.join(contact[:3]).split()
    while len(names) != 3:
        names.append('')
    normal_contact = names + fields
    return normal_contact


@logger('phonebook.log')
def delete_duplicates(contacts_list):

    """
    Removes duplicate contacts from a list of contacts.
    :param contacts_list (list of lists of strings).
    :return: contacts(list of lists of strings): A list of contacts with duplicates removed.
    """

    merged = {}
    for contact in contacts_list:
        name = f'{contact[0]} {contact[1]}'
        if name in merged:
            for i, field in enumerate(contact):
                if field == '':
                    continue
                merged[name][i] = field
        else:
            merged[name] = contact
    contacts_list = [field for field in merged.values()]
    return contacts_list


@logger('phonebook.log')
def format_phone(old_phone):

    """
    Formats a phone number to a standard format.
    :param old_phone (string)
    :return: string representing the formatted phone number.
    """

    phone_pattern = r'(\+?[7|8])\s*\(?(\d{3,3})\)?\s*\-?(\d{3,3})\-?(\d{2,2})\-?(\d{2,2})\s*\(?[доб.]*\s*(\d+)?\)?'
    if "доб." not in old_phone:
        new_phone_pattern = r'+7(\2)\3-\4-\5'
    else:
        new_phone_pattern = r'+7(\2)\3-\4-\5 доб.\6'
    normal_phone = re.sub(phone_pattern, new_phone_pattern, old_phone)
    return normal_phone


@logger('phonebook.log')
def fill_phonebook(correct_phonebook):

    """
    Writes the corrected phonebook to a CSV file.
    :param correct_phonebook (list of lists of strings) contacts with duplicates removed and phone numbers formatted.
    :return: None
    """

    with open(os.path.join(os.getcwd(), 'phonebook', "correct_phonebook.csv"), "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(correct_phonebook)
        return
