# Дан словарь, создать новый словарь при помощи конструкции
# генератор словаря, поменяв местами ключ и значение.


chess_players = {
    "Carlsen, Magnus": 2865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 2792,
    "Nepomniachtchi, Ian": 2773
}
print(chess_players)
new_sps = {chess_players[k]: k for k in chess_players}
print(new_sps)
