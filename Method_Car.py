# Создай объект Машина, которому можно задать свойства цвет и 
# марку при создании. 
# И методы ехать и остановиться. 
# А также можно будет заменить владельца авто.

class Car:
    def __init__ (self, brand, color):
        self.brand = brand              
        self.color = color

    def drive(self, drive = 'I\`m runned!'):
        self.drive = drive

    def stop(self, stop = 'I\`m stoped!!!'):
        self.stop = stop
        return 'I\`m stoped!!!'
    
    def change_owner(self, change = 'What?'):
        self.change_owner = change
        return 'What?'


# car = Car('Toyota', 'black')
# car.drive('hi')

# print(car.brand, car.color)
# print(car.drive()) # I'm runned
# print(car.stop()) # I'm stoped
# print(car.change_owner())
# print(car.change_owner('New owner'))

class Auto:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print('I am running')

    def stop(self):
        print('I`m stopped!')

    def change_owner(self, name='Unknown'):
        self.owner = name
        print(f'Change owner to {self.owner}')
    

toyota = Auto('Toyota', 'Black') # {}
toyota.drive()
toyota.stop()
toyota.change_owner('Artem')
toyota.change_owner('Dima')

java = Auto('Czezet', 'Red')

print(toyota.__dict__, java.__dict__)