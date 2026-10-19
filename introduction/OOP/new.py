class character :
    def __init__(self,name,health,attack,blood):
        self.name = name
        self.health = health
        self.attack = attack
        self.blood = blood

    def attack_enemy(self):
        print(f'{self.name} attacks with power {self.attack} {self.blood}')

warrior = character('Thor', 100,50,'red')

mage = character('Gandalf', 80,70,'black')

archer = character('archer', 80,90,'white')

warrior.attack_enemy()
mage.attack_enemy()
archer.attack_enemy

