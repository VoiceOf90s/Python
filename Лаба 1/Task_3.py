list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
leng = len(list_players)
print(list_players[0:int(leng/2):1])
print(list_players[int(leng/2):int(leng):1])