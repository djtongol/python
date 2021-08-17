#Basic OOP

class Beach:
    #location= 'Cape Cod'
    
    def __init__(self, location, water, temperature):
        self.location= location #instance variable
        self.water= water
        self.temperature= temperature
        self.heat = 'hot' if temperature >80 else 'cool'
        self.parts= ['water' 'sand']
    
    def add_parts(self, parts):
        self.parts.append(parts)


def main():
    update = 'Update on '
    Boracay = Beach('Boracay', 'clear', 90)
    Boracay.add_parts('Shells')
    Baler= Beach('Baler', 'dark blue', 100)
    Baler.add_parts('rocks')
    Bohol= Beach('Bohol', 'crystal', 70)
    Baler.add_parts('tarsiers')
    hot_not_rocky= []

    for beach in [Boracay, Baler, Bohol]:
        if beach.heat == 'hot' and 'rock' not in beach.parts:
            hot_not_rocky.append(Beach)
    
    return hot_not_rocky

# if __name__ == '__main__':
#     beaches=main()
#     print([beach.location for beach in beaches])
    
#print(update, Boracay.location, Boracay.water, Boracay.temperature, Boracay.heat, ' '.join(Boracay.parts) + '\n')
#print(update, Baler.location, Baler.water, Baler.temperature, Baler.heat, ' '.join(Baler.parts) + '\n')

#print(update, Bohol.location, Bohol.water, Bohol.temperature, Bohol.heat, ' '.join(Bohol.parts))


#Inheritance and Polymorphism in Classes

class Dog:
    def __init__(self, name, age, friendliness):
        self.name= name
        self.age= age
        self.friendliness= friendliness
    
    def likes_walks(self):
        return True
    
    def bark(self):
        return "Woof!"

class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)
    
    def bark(self):
        return "arf arf"

class Poodle(Dog): 
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return "Aroooo!"

    def shedding_amount(self):
        return 0


class Bulldog(Dog): 
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)
    
    def fetch_ability(self): 
        if self.age < 2:
            return 8
        elif self.age <10:
            return 10
        else: return 7

class Budle (Poodle, Bulldog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

# sammy = Samoyed('Sammy', 2, 10)
# print(sammy.name, sammy.age, sammy.friendliness)
# print(sammy.likes_walks())

barker= Budle('barker', 10, 10)
maxie =Dog('maxie', 12, 5)
teddy = Samoyed('teddy', 4, 10)

print(barker.bark(), maxie.bark(), teddy.bark())




