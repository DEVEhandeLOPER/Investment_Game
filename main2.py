import json
import os
import random as rm

class Player:
    def __init__(self, name, difficulties_lvl):
        self.name = name
        self.difficulties_lvl = difficulties_lvl
        self.stock_paper_total = 0
        self.investment_budget = 0

    def create_character(self):
        try:
            with open("user_stats.json", "r") as file:
                players = json.load(file)
        except (FileNotFoundError, FileExistsError) as err:
            print("Dosya bulunmamaktadir.", err)
        else:
            player = {
                "player_name": self.name,
                "difficulties": self.difficulties_lvl
            }

            if isinstance(players, list):
                players.append(player)
            else:
                players = [player]

            with open("user_stats.json", "w") as file:
                json.dump(players, file)

    def difficulties_creator(self):
        if self.difficulties_lvl == "k":
            self.stock_paper_total = rm.randint(3, 10)
            self.investment_budget = rm.randint(50000, 200000)
        elif self.difficulties_lvl == "o":
            self.stock_paper_total = rm.randint(3, 7)
            self.investment_budget = rm.randint(25000, 100000)
        elif self.difficulties_lvl == "z":
            self.stock_paper_total = rm.randint(1, 7)
            self.investment_budget = rm.randint(10000, 20000)

class Investment:
    def __init__(self):
        self.data_file = "investment_area.json"

    def change_values(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as file:
                    investment_data = json.load(file)
            else:
                investment_data = {
                    "DOAS": {"id": 0, "value": 20000000, "each_price": 697},
                    "TUPRS": {"id": 1, "value": 21000000, "each_price": 751},
                    "TURKT": {"id": 2, "value": 19000000, "each_price": 710},
                    "BIM": {"id": 3, "value": 26000000, "each_price": 1199},
                    "ENSA": {"id": 4, "value": 11000000, "each_price": 547},
                    "IZNEN": {"id": 5, "value": 1000000, "each_price": 30}
                }
                with open(self.data_file, "w") as invest:
                    json.dump(investment_data, invest)

            for key, val in investment_data.items():
                max_price = int(val["value"] * 0.00005)
                min_price = int(val["each_price"] - (val["each_price"] * 0.25))
                result = rm.randint(min_price, max_price)
                val["each_price"] = result

            with open(self.data_file, "w") as invest:
                json.dump(investment_data, invest)

            self.display_investment_data(investment_data)

        except Exception as exc:
            print(f"Oooppss!!!\nBeklenmedik bir hata oluştu\n{exc}")

    def display_investment_data(self, investment_data):
        print("Invesment Data:")
        print("-" * 62)
        print("{:<7} {:<20} {:<20} {:<20}".format("ID", "NAME", "VALUE", "EACH PRICE"))
        print("-" * 62)
        for key, val in investment_data.items():
            name = key
            id = val["id"]
            value = val["value"]
            each_price = val["each_price"]
            print("{:<7} {:<20} {:<20} {:<20}".format(id, name, value, each_price))
        print("-" * 62)

    def get_user(self):
        players = []

        with open("user_stats.json", "r") as users:
            user = json.load(users)
            for i in user:
                players.append(i)

        return players

    def display_users(self):
        count = 0
        print("-" * 100)
        print("{:<7} {:<20}".format("ID", "NAME"))
        print("-" * 100)
        for i in self.get_user():
            count += 1
            print("{:<7} {:<20}".format(count, i['player_name']))
        print("-" * 100)
        count = 0

    def change_values(self):
        self.display_users()
        command = int(input("Hangi oyuncunun stock paper degerini degistireceksiniz: "))
        users = self.get_user()
        print(users[command - 1])

        new_value = int(input("Yeni stock degerini giriniz: "))
        users[command - 1]["stock_paper_total"] = new_value

        with open("user_stats.json", "w") as file:
            json.dump(users, file)


if __name__ == "__main__":
    player1 = Player("Emir", "C")
    player1.create_character()
    player1.difficulties_creator()