
class player_class:
    def Player_Data(self, name, currency=0, health=0, mana=50, planet="",unlocked_planets=None):
        self.name = name
        self.currency = currency
        self.health = health
        self.planet = planet
        self.unlocked_planets = []

    def inventory(self, planet, Pickaxes=None, Drills=None, Ores=None, Bars=None):
        self.Pickaxes = {}
        self.Drills = {}
        self.Ores = {
            "Copper Ore": {
                "Amount": 20,
                "Value": 3
            }
        }
        self.Bars = {
            "Copper Bar": {
                "Amount": 0,
                "Value": 10
            }
        }

