# TODO Напишите функцию find_common_participants
def find_common_participants(first_p, second_p, separator =','):
    first_list_group = first_p.split(separator)
    second_list_group = second_p.split(separator)
    common_participants = list(set(first_list_group).intersection(set(second_list_group)))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

participants = find_common_participants(participants_first_group,participants_second_group)
print(f'Общие участники: \n {participants}')