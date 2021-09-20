class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def change_coords(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coords(self):
        return self.x, self.y, self.z


class Point:
    def __init__(self, object = Point3D(0,0,0)):
        self.x = object.x
        self.y = object.y
        self.z = object.z
        

point3D = Point3D(2, 4, 5)
point3D_1 = Point3D(0, 4, 9)
point3D_2 = Point3D(3, 5, 7)
# {'x': 2, 'y': 4, 'z': 5}
# {'x': 0, 'y': 4, 'z': 9}
point = Point(point3D)
point2 = Point()
print(point.__dict__, point2.__dict__)

# print(point3D.__dict__, point3D_1.__dict__, point3D_2.__dict__, sep='\n')

# point3D.change_coords(1,2,3)
# point3D.name = 'my object'
# point3D_1.change_coords(1,2,3)
# point3D_2.change_coords(5, 5, 5)

# print('Get method:')
# print(point3D.get_coords())


# Создай объект Машина, которому можно задать свойства цвет и 
# марку при создании. 
# И методы ехать и остановиться. 
# А также можно будет заменить владельца авто.

class Car:
    def __init__ ():
        pass


car = Car('Toyota', 'black')
print(car.color, car.brand)
car.method_drive() # I'm runned
car.method_stop() # I'm stoped
car.method_change_owner()
print(car.change_owner('New owner'))


