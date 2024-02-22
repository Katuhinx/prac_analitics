from random import randint, choice
from datetime import datetime, date, timedelta
from json import dumps
import csv
import math



name_ship = ["Dream-", "Laguna-", "Vera-", "Artemida-", 
                "Maximus-", "Lev-", "Maria-", "Svoboda-", "Freedom-", 
                "Gelius-", "Kutuzov-", "Pobeda-", "Dendy-", "Slava-",
                "Bingo-", "Turbo-", "Boss-", "Nadezhda-", "Memory-",
                "Lavanda-", "Makarov-", "Adam-", "Black-", "Leon-", "White-", 
                "Sea-", "Dimond-", "Elithabet-", "Planet-", "Skill-"]
        
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", 
                "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "Beautiful","Little",
                "Big","Round","Brown","Red","Blue","Yellow","Green", "Wooden","Lovely","Hunting", "Expencive", "A", "B", 
                "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
                "U", "V", "W", "X", "Y", "Z", "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1", "M1", "N1", 
                "O1", "P1", "Q1", "R1", "S1", "T1", "U1", "V1", "W1", "X1", "Y1", "Z1", "A5", "B5", 
                "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5", "K5", "L5", "M5", "N5", 
                "O5", "P5", "Q5", "R5", "S5", "T5", "U5", "V5", "W5", "X5", "Y5", "Z5", "Zh","NAU","SH","VORONT","ER",
                "DR","GN","S1000","LOGIN","S200000","KAP","LL","MOI", "ELIS","KOSH","KOT","GOR","NUTS","EFR","ISA","EV",
                "KALA","KAB","SOCKS","YU","KU","LAP"]


countries = ["Russia","China","Turkey","Ukrain","Germany","USA","India","Pakestan","Kazahstan","Belgium","Australia","Canada",
           "Greece","Egypt", "Ireland","Spain","Italy","Norway","Japan"]

cities = [
    ["Saint Petersburg", "Novorossiisk", "Magadan", "Sochi", "Vladivastok","Arkchangelsk","Murmansk"],
    ["Shanghai","Ningbo","Dalian","Tianjin","Qingbao","Shanzen","Guangzhou","Fuzhou"],
    ["Ambarili","Gebze","Gemlik","Istanbul","Izmir","Izmit","Mersin"],
    ["Nikolaev","Odessa","Chernomorsk"],
    ["Bremerhaven","Hamburg","Kiel","Wilhelmshaven"],
    ["Baltimore","Boston","Charleston","Houston","Jacksonville","Long Beach","Los Angeles","Miami"],
    ["Chennai","Jawaharlal Nehru","Mundra","Pipavav"],
    ["Karachi"],
    ["Actau","Kyruk"],
    ["Antwerp","Zeebrugge"],
    ["Adelaide","Bell Bay","Brisbane","Fremantle","Melbourne","Sydney","Townsville"],
    ["Halifax","Montreal","Vancouver"],
    ["Piraeus","Thessaloniki","Volos"],
    ["Alexandria","Damietta","El Dekheila","Port-Said"],
    ["Larn","Belfast","Uorrenpoint","Dublin","Rossler"],
    ["La Corunie","Aresiffe","Barselona","Cadisa","Cartakchenu","Ibizza","Las Palmas","Malagi"],
    ["Cagliari","Genova","Gioia Tauro","La Spezia","Livorno","Napoli","Palermo","Ravenna"],
    ["Brevik","Fredrikstad","Lavrik","Moss","Oslo"],
    ["Kobe","Nagoya","Osaka","Shimizu","Yokohama"]

]

firstname = ["Mikhail", "Alexander", "Maxim", "Artem", 
                "Mark", "Lev", "Matvey", "Ivan", "Dmitry", 
                "Dmitry", "Evgeny", "Denis", "Anton", "Igor",
                "Yuri", "Oleg", "Vyacheslav", "Vasily", "Stanislav",
                "Vadim", "Makar", "Adam", "Bogdan", "Leon", "Platon", 
                "Savely", "Demid", "Luka", "Miroslav", "Savva"]
        
secondname = ["SMIRNOV", "IVANOV", "KUZNETSOV", "POPOV",
                "SOKOLOV", "LEBEDEV", "GOATS", "NOVIKOV", "MOROZOV",
                "PETROV", "VOLKOV", "SOLOVIEV", "VASILIEV", "ZAYTSEV", 
                "PAVLOV", "SEMYONOV", "GOLUBEV", "BOGDANOV", "TARASOV",
                "VOROBYOV", "FEDOROV", "MIKHAILOV", "BELYAEV", "BELOV",
                "KOMAROV", "ORLOV", "KISELEV", "MAKAROV", "ANDREEV", "KOVALYOV", 
                "ILYIN", "GUSEV", "TITOV", "KUZMIN", "KUDRYAVTSEV", "BARANOV", 
                "KULIKOV", "ALEXEEV", "STEPANOV", "YAKOVLEV", "SOROKIN", "SERGEYEV", 
                "ROMANOV", "ZAKHAROV", "BORISOV","KOROLEV", "GERASIMOV","PONOMAROV",
                "GRIGORIEV","LAZAREV","MEDVEDEV","ERSHOV","NIKITIN","SOBOLEV","RYABOV",
                "POLYAKOV","FLOWERS","DANILOV", "ZHUKOV", "FROLOV", "ZHURAVLYOV", 
                "NIKOLAEV", "KRYLOV", "MAKSIMOV", "SIDOROV", "OSIPOV", "BELOUSOV", 
                "FEDOTOV", "DOROFEEV", "EGOROV", "MATVEEV", "BOBROV", "DMITRIEV", 
                "KALININ", "ANISIMOV", "ANTONOV", "TIMOFEEV", "NIKIFOROV", "VESELOV", 
                "FILIPPOV", "MARKOV", "BOLSHAKOV", "SUKHANOV", "MIRONOV", "SHIRYAEV", 
                "ALEXANDROV", "KONOVALOV", "SHESTAKOV", "KAZAKOV", "EFIMOV", "DENISOV", 
                "GROMOV", "FOMIN", "DAVYDOV", "MELNIKOV", "SHCHERBAKOV", "KOLESNIKOV", 
                "KARPOV", "AFANASYEV", "VLASOV", "MASLOV", "ISAKOV", "TIKHONOV", "AKSYONOV", 
                "GAVRILOV", "RODIONOV", "KOTOV", "GORBUNOV", "KUDRYASHOV", "BYKOV",
                "ZUEV", "TRETYAKOV", "SAVELIEV", "PANOV","RYBAKOV","SUVOROV","ABRAMOV","VORONOV","MUKHIN",
                "ARKHIPOV","TROFIMOV","MARTYNOV","GORSHKOV","CHERNOV","OVCHINNIKOV","SELEZNEV",
                "PANFILOV","KOPYLOV","MIKHEEV","GALKIN","NAZAROV","LOBANOV","LUKIN","BELYAKOV",
                "POTAPOV","NEKRASOV","KHOKHLOV","Zhdanov","NAUMOV","SHILOV","VORONTSOV","ERMAKOV",
                "DROZDOV","IGNATIEV","SAVIN","LOGINOV","SAFONOV","KAPUSTIN","KIRILLOV","MOISEEV",
                "ELISEEV","KOSHELEV","KOSTIN","GORBACHEV","NUTS","EFREMOV","ISAEV","EVDOKIMOV",
                "KALASHNIKOV","KABANOV","SOCKS","YUDIN","KULAGIN","LAPIN"]

properties = ['weight', 'quantity', 'height', 'width', 'length']

seasons = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]

ship_num = 1000000
product_num = 1000000
visit_num = 2000000
berth_num = 20

#generate_ship_csv
# with open("ship.csv", "w", encoding="utf-8", newline='') as ship_csv:
#         writer = csv.writer(ship_csv)
#         for i in range(1, ship_num + 1):
#             team_names = "{"
#             for j in range(randint(2, 50)):
#                 if j > 0:
#                     team_names+=", "
#                 team_names+=f'"{choice(firstname).upper()} {choice(secondname).upper()}"'

#             team_names+= "}"
#             writer.writerow([randint(100,100000), randint(1000,100000), team_names])
#             if i % 100000 == 0:       
#                 print(f"Done: { i / visit_num * 100 }%")

# #generate_product_csv
# with open("product.csv", "w", encoding="utf-8", newline='') as product_csv:
#         writer = csv.writer(product_csv)
#         for i in range(1, product_num + 1):
#             writer.writerow([f"Продукт {i}"])

#             if i % 100000 == 0:       
#                 print(f"Done: { i / product_num * 100 }%")

#generate_cargo_csv
with open("cargo.csv", "w", encoding="utf-8", newline='') as cargo_csv:
        writer = csv.writer(cargo_csv)
        for i in range(1000001, visit_num + 1):
            products_list = []
            products = []

            for j in range(0, randint(10, 30)):
                product = randint(1, product_num)
                while product in products_list:
                    product = randint(1, product_num)

                products_list.append(product)

                product_properties = '{'

                for k in range(0, randint(1, 5)):
                    if k > 0:
                        product_properties+=', '  

                    product_properties+=f'"{properties[k]}": {str(randint(1, 10000))}'
                
                product_properties+= '}'

                category = ''

                if product >= 0 and product < 50000:
                    category = 'Нефтепродукты'
                elif product >= 50000 and product < 150000:
                    category = 'Электроника'
                elif product >= 150000 and product < 250000:
                    category = 'Автомобили'
                elif product >= 250000 and product < 280000:
                    category = 'Производственное оборудование'
                elif product >= 280000 and product < 350000:
                    category = 'Медикаменты'
                elif product >= 350000 and product < 400000:
                    category = 'Фурнитура'
                elif product >= 400000 and product < 418000:
                    category = 'Металлы'
                elif product >= 418000 and product < 490000:
                    category = 'Текстиль'
                elif product >= 490000 and product < 550000:
                    category = 'Бытовая химия'
                elif product >= 550000 and product < 650000:
                    category = 'Стройматериалы'
                elif product >= 650000 and product < 750000:
                    category = 'Косметические средства'
                elif product >= 750000 and product < 800000:
                    category = 'Обувь'
                elif product >= 800000 and product < 880000:
                    category = 'Напикти'
                elif product >= 880000:
                    category = 'Продкуты питания'
                

                writer.writerow([f"{i}", category, f"Продукт {product}", product_properties])

            if i % 100000 == 0:       
                print(f"Done: { i / visit_num * 100 }%")

# generate_visit_csv
# with open("visit.csv", "w", encoding="utf-8", newline='') as visit_csv:
#     writer = csv.writer(visit_csv)
#     for i in range(1, visit_num + 1):
#         country_departure = randint(0, len(countries) - 1)
#         city_departure = randint(0, len(cities[country_departure]) - 1)

#         country_arrival = randint(0, len(countries) - 1)
#         city_arrival = randint(0, len(cities[country_arrival]) - 1)

#         while (country_departure == country_arrival) and (city_departure == city_arrival):
#             country_arrival = randint(0, len(countries) - 1)
#             city_arrival = randint(0, len(cities[country_arrival]) - 1)

#         place_departure = '{"country": "' + countries[country_departure] + '", "city": "' + cities[country_departure][city_departure] + '", "port": "port ' + str(randint(1, 3)) + '"}'
#         place_arrival = '{"country": "' + countries[country_arrival] + '", "city": "' + cities[country_arrival][city_arrival] + '", "port": "port ' + str(randint(1, 3)) + '"}'
            
#         date_departure = datetime.strptime(f"{randint(2000, 2023)}-{randint(1, 12)}-{randint(1, 28)}", '%Y-%m-%d')
#         date_arrival = date_departure + timedelta(days=(randint(1,20)))

#         writer.writerow([place_departure, date_departure.strftime("%Y-%m-%d"), date_departure.year, seasons[date_departure.month - 1], place_arrival, date_arrival.strftime("%Y-%m-%d"), date_arrival.year, seasons[date_arrival.month - 1], randint(11, ship_num)])

#         if i % 100000 == 0:       
#             print(f"Done: { i / visit_num * 100 }%")






# f= open('update_query.txt', 'w')
# for i in range(900001, 1000100 + 1):
#     team_names = "'{"
#     for j in range(randint(2, 50)):
#         if j > 0:
#             team_names+=", "
#         team_names+=f'"{choice(firstname).upper()} {choice(secondname).upper()}"'

#     team_names+= "}'"

#     f.write(f"UPDATE analitics.ship SET team = {team_names} WHERE id = {str(i)};\n")

#     if i % 100000 == 0:       
#         print(f"Done: { i / visit_num * 100 }%")

# f.close()