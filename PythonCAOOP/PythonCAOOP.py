class robot:
    name = ""
    hp = 100 
    ep = 0
    cele = []
    def __init__(self, name="nie mam imienia", hp=100, ep=0, cele= None):
        print("Robot has been created!\n")
    def atakuj(self, cel):
        if cel in self.cele:
            print("zaatakowa³em" + cel)
        else:
            print("nikogo nie mo¿esz atakowaæ!" )
    def szukajWrogow(self):

class wojownik(robot):
    def __init__(self, name="wojownik",hp=100, ep=0, cele=["robot"]):
        print("Warior has been created")
    def walcz(self):
        if self.hp < 50:
            print("nigdzie nie ide")
        else:
            print("ide bic")
            self.atakuj("ktos")



Transformers = robot()
WojownikWody = wojownik()
print(Transformers.atakuj("kupa"))
WojownikWody.walcz()