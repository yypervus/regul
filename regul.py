import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


def updated_phone_numbers(list_list, regular, new):
    pattern = re.compile(regular)
    final = [[pattern.sub(new, string) for string in list_] for list_ in list_list]
    return final

def name_correct(list_list):
    result = [' '.join(employee[0:3]).split(' ')[0:3] + employee[3:7] for employee in list_list]
    return result

def remove_duble(correct_name_list):
    new_list = []
    for compared in correct_name_list:
        for employee in correct_name_list:
            if compared[0:2] == employee[0:2]:
                list_employee = compared
                compared = list_employee[0:2]
                for i in range(2, 7):
                    if list_employee[i] == '':
                        compared.append(employee[i])
                    else:
                        compared.append(list_employee[i])
        if compared not in new_list:
            new_list.append(compared)
    return new_list


final_name_list = name_correct(contacts_list)
final_num_list = updated_phone_numbers(final_name_list, r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})', r'+7(\2)\3-\4-\5')
final_num_addit_list = updated_phone_numbers(final_num_list, r'\(?доб.\s(\d{4})\)?', r'доб.\1')
final_list = remove_duble(final_num_addit_list)


with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(final_list)

