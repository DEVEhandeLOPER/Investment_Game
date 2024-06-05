## Oyunu biz basit yazicaz 
## Classlar ile daha derli toplu bir hale getireceksiniz 

## Yatirim Oyunu
## OPEN WITH ile yatirim portifoylerini kaydedelim
## Objet veri tipini kullanalim
## Zorluk Seviyeleri Kolay Orta

## Oyun esnasinda olusturdugumuz player listten herhangi bir player'i cekip 
## O player'in oyun statlarini kullanabilelim.
## Invesment Change her piyasa ekranina girildiginde degistirilecek.
## while en basina koydugumuzda her islemde value lari degismesini sagliyabiliriz.
## bilgisayar saatine gore her dakika degistiginde valuelar da degisebilir.
## 1 - Olusturulan kullanicilarin kaydi icin ayri bir fonksiyon uretilmeli

import json
import os
import random as rm

def difficulties_creator(choice,player):
    stock_paper_values = 0
    invesment_budged = 0

    if choice == "k":
        stock_paper_values = rm.randint(3,10)
        invesment_budged = rm.randint(50000,200000)
    elif choice == "o":
        stock_paper_values = rm.randint(3,7)
        invesment_budged = rm.randint(25000,100000)
    elif choice == "z":
        stock_paper_values = rm.randint(1,7)
        invesment_budged = rm.randint(10000,20000)

    player["stock_paper_total"] = stock_paper_values
    player["invesment_budged"] = invesment_budged

    return player

def create_caracter(player_name, difficulties_lvl):
    PLAYERS = []

    try:
        # Dosyanin olup olmadigi kontrol ediyoruz eger dosya varsa 
        # Players icine dosya verilerini cekiyoruz.
        with open("user_stats.json","r") as file:
            PLAYERS = file.read()
            PLAYERS = json.loads(PLAYERS)
    
    except FileNotFoundError or FileExistsError as err:
        print("Dosya bulunmamaktadir.",err )

    finally:
        # Player dosyasi var ya da yok bu bolum calisacaktir.

        player = {
            "player_name": player_name,
            "difficulties": difficulties_lvl
        }

        if len(PLAYERS) > 0:
            # Eger Player dosyasi varsa PLAYERS constant variable ici dolu olacaktir o yuzden
            # Bu bolum calisacaktir.
            player = difficulties_creator(difficulties_lvl,player)
            PLAYERS.append(player)
            with open("user_stats.json", "w") as file:
                json.dump(PLAYERS, file)
        else:
            # Diger durumlarda yani dosya yoksa bu bolum calisacaktir.
            # difficulties_creator bize bir obje donecektir bu yuzden 
            # list parantezleriyle sarmalayıp. json formatina uygun olmasini sagladik.
            player = [difficulties_creator(difficulties_lvl,player)]
            with open("user_stats.json", "w") as file:
                json.dump(player, file)


def invesment_change():
    try:
        if os.path.exists("invesment_area.json"):
            with open("invesment_area.json","r") as file:
                invesment_data = json.load(file)
        else:
            invesment_data = {
                "DOAS": {"id":0, "value": 20000000, "each_price": 697}, 
                "TUPRS": {"id":1, "value": 21000000, "each_price": 751}, 
                "TURKT": {"id":2, "value": 19000000, "each_price": 710}, 
                "BIM": {"id":3, "value": 26000000, "each_price": 1199},
                "ENSA": {"id":4, "value": 11000000, "each_price": 547}, 
                "IZNEN": {"id":5, "value": 1000000, "each_price": 30}
            }
            with open("invesment_area.json","w") as invest:
                json.dump(invesment_data,invest)

        with open("invesment_area.json","r") as file:
                invesment_data = json.load(file)

        for key, val in invesment_data.items():
            try:
                max_price = int(val["value"] * 0.00005)
                min_price = int(val["each_price"] - (val["each_price"] * 0.25))
                result = rm.randint(min_price, max_price)
                val["each_price"] = result
            except KeyError as key:
                print(f"KeyError: {key}\n Girdiğiniz anahtar kelime hatalıdır.")

        with open("invesment_area.json", "w") as invest:
            json.dump(invesment_data, invest)
        
        display_investment_data(invesment_data)    
        
    except Exception as exc:
        print(f"Oooppss!!!\nBeklenmedik bir hata oluştu\n{exc}")

def display_investment_data(invesment_data):
    print("Invesment Data:")
    print("-"*62)
    print("{:<7} {:<20} {:<20} {:<20}".format("ID","NAME","VALUE","EACH PRICE"))
    print("-"*62)
    for key, val in invesment_data.items():
        name = key
        id = val["id"]
        value = val["value"]
        each_price = val["each_price"]
        print("{:<7} {:<20} {:<20} {:<20}".format(id,name,value,each_price))
    print("-"*62)

def get_user (file_name):
    PLAYERS = []

    with open(file_name, "r") as users:
        user = users.read()
        user = json.loads(user)
        for i in user:
            PLAYERS.append(i)

    return PLAYERS


def display_users (PLAYERS):
    count = 0
    print("-"*100)
    print("{:<7} {:<20}".format("ID","NAME"))
    print("-"*100)
    for i in PLAYERS:
        count += 1
        print("{:<7} {:<20}".format(count,i['player_name']))
    print("-"*100)
    count = 0


def change_values (file_name):

    # Bu bolum stock itmenstment areadan satin alim oldukca calismali
    #fonksiyon cagrildiginda display_investment_data calissin
    # daha sonra kullanici borsa kagidinin id sini girdiginde
    # onun guncel fiyatina gore elindeki para kadar alim yapabilsin
    # elindeki para yetmez ise, o para ile o kagittan max ne kadar alabilecegini bize bidirsin.

    display_users(get_user(file_name))
    command = int(input("Hangi oyuncunun stock paper degerini degistireceksiniz: "))
    users = get_user(file_name)
    print(users[command - 1])

    new_value = int(input("Yeni stock degerini giriniz: "))
    users[command - 1]["stock_paper_total"] = new_value

    with open(file_name, "w") as file:
        json.dump(users, file)

          
