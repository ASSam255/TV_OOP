from Telecast import Telecast
from Client import Client 
from Ad import Ad 

TelecastArray = [
        Telecast(1, "Импривизация", 10, 500000),
        Telecast(2, "Галилео", 7, 100000),
        Telecast(3, "Camedy club", 5, 50000)
]

ClientArray = [
        Client(1, "Банк", "6435546", 89770351523, "Алексей Дмитриевич"),
        Client(2, "Фокс кид", "19465", 89854886611, "Павел Эдуардович"),
        Client(3, "Кроок", "1982518", 89268886644, "Карен Ашотович")
]

AdArray = [
        Ad(1, TelecastArray[0], ClientArray[2], "12.05.2020", 3),
        Ad(2, TelecastArray[1], ClientArray[0], "09.12.2021", 4),
        Ad(3, TelecastArray[2], ClientArray[1], "13.07.2022", 5)
]

print("\nПередачи:\n")
for ITEM in TelecastArray: print(ITEM,'\n')

print("\nКлиенты:\n")
for ITEM in ClientArray: print(ITEM,'\n')

print("\nРеклама:\n")
for ITEM in AdArray: print(ITEM,'\n')
