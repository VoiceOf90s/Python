def find_common_participants(a, b, c=','):
    unique_members = list(set(a.split(c)).intersection(set(b.split(c))))
    return sorted(list(unique_members))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group,participants_second_group))
print(find_common_participants(participants_first_group,participants_second_group, ';'))
