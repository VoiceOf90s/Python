users = ["user1", "user2", "user3", "user1", "user4", "user2"]

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
diction = {"Общее количество": 0, "Уникальные посещения": 0}
uni_users = set(users)
diction["Общее количество"] = int(len(users))
diction["Уникальные посещения"] = int(len(uni_users))
print(diction)