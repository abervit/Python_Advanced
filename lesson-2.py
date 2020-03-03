# Первая задача с главным классом Машины, двумя подклассами - легковые и грузовые,
# дополнительным классом Drive() и использование переопределение метода главного класса как и инскапуляциия метода
class Vehicle():
    """Our main atributes of our class and future objects"""

    def __init__(self, brand, model, year, engine, wheels):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.wheels = wheels
        self.mileage = 0  # the mileage of our future car
        # print ('It look like we have everything we need to drive our car')

    """description of our car characteristics"""

    # it will help us to get all information about our vehicle by using one function
    def self_desc(self):
        desc = self.brand.title() + ' ' + self.model.title() + ' ' + str(self.year) \
               + ' ' + self.engine + ' ' + self.wheels
        return desc

    """we gonna use the encapsulation method in order to keep this data for us"""

    def __odometer(self, miles):
        self.mileage += abs(miles)  # using abs() will help us to avoid some problems with negative numbers
        print('This model has only ', self.mileage, 'miles')

    def speed(self, speed=1500):
        print('We reached our maximum speed and it was over', speed, ' k/h')


car1 = Vehicle('bmw', 'm5', 2017, 'v8 440hp', '4 wheels')
print(car1.self_desc())
car1._Vehicle__odometer(10)
car1._Vehicle__odometer(-200)
print(car1.__dict__)


class Drive():
    def start(self, to):
        self.to = to
        print(f'Ok, it`s time to drive our car to {to}')
        return self.to

    def stop(self, destiny):
        self.destiny = destiny
        print(f'I think we`ll stop for a night at {destiny}')
        return self.destiny


class Car(Vehicle):
    """ Attributes initialization of our main Car class"""

    def __init__(self, brand, model, year, engine, wheels):
        super().__init__(brand, model, year, engine, wheels)
        self.drive = Drive()

    """Method overriding, which allows us to change the implementation of methods of our main class """

    def car_speed(self, speed=200):
        self.speed = speed
        print('The maximum speed in Ukraine is ', speed)


class Track(Vehicle):
    def __init__(self, brand, model, year, engine, wheels, trailer):
        super().__init__(brand, model, year, engine, wheels)
        self.trailer = trailer

    """Method overriding, which allows us to change the implementation of methods of our main class """

    def self_desc(self):
        desc = self.brand.title() + ' ' + self.model.title() + ' ' + str(self.year) \
               + ' ' + self.engine  # we removed wheels
        return desc


# car1 = Car('bmw','x5',2003,'v6 diesel','4 wheels')
# print(car1.self_desc())
# car1.car_speed()
# print(car1.drive.start('Berlin'))
# print(car1.drive.stop('Chicago'))

volvo = Track('volvo', 'pobeda', 2001, 'v10 400 h/p', '6x6', '20t capacity trailer')
volvo.self_desc()
print(volvo.self_desc())
volvo._Vehicle__odometer(300)
print(volvo.__dict__)


# Создаем класс Магазин

class Store():
    all_stores = 0

    def __init__(self, name, place, sold_goods):
        self.name = name
        self.place = place
        self.sold_goods = sold_goods

        Store.all_stores += self.sold_goods

    def description(self):
        desc = 'Our new brand store ' + self.name.title() + ' is opened in ' \
               + self.place + ' everyone is wellcome!!!'
        return desc

    # def sold(self):
    #     print('This store has sold ' + str(self.sold_goods) + ' which is not too bad')

    def update_sold(self, sold):
        # if sold:
        self.sold = sold
        self.sold_goods += sold
        print('We updated our "sold" book', self.sold_goods)
    # else:
    #     print('Stop cheating')


store1 = Store('Wallet', 'Dubai', 300)
print(store1.__dict__)
store2 = Store('Alda', 'Swansea', 400)
print(store2.__dict__)
print(Store.all_stores)
store1.update_sold(200)
store1.update_sold(200)
print(Store.all_stores)


# Point class

class Point:
    """Our Class Point will have 3 attributes - x, y, z"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    """Next 3 update functions, will help us to get and change new attributes for x,y,z"""

    def update_x(self, new):
        self.x = new
        return self.x

    def update_y(self, new):
        self.y = new
        return self.y

    def update_z(self, new):
        self.z = new
        return self.z

    """Below methods we use for mathematical operations such us 
    - addition, subtraction, multiplication and true division"""

    def __add__(self, other):
        # add = self.x + other.x, self.y + other.y, self.z + other.z
        # return add
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        sub = self.x - other.x, self.y - other.y, self.z - other.z
        return sub

    def __mul__(self, other):
        mul = self.x * other.x, self.y * other.y, self.z * other.z
        return mul

    def __truediv__(self, other):
        truediv = self.x / other.x, self.y / other.y, self.z / other.z
        return truediv

    # def __pow__(self, other):
    #     pow  = self.x ** other.x, self.y ** other.y, self.z ** other.z
    #     return pow
    """Now we gonna use some unary methods"""

    def __round__(self):
        roun = round(self.x), round(self.y), round(self.z)
        return roun

    def __abs__(self):
        abs_abs = abs(self.x), abs(self.y), abs(self.z)
        return abs_abs


p1 = Point(33, 22, 311)
print(p1.update_x(-1.34))
print(p1.update_y(2.56))
print(p1.update_z(3))

print(p1.__dict__)
p2 = Point(1, 2, 3)
print(p2.__dict__)
print(p1.__add__(p2))
print(p1.__sub__(p2))
print(p1.__mul__(p2))
print(p1.__truediv__(p2))
print(p2.__truediv__(p1))
# print(p2.__pow__(p1))
print(p1.__round__())
print(p1.__abs__())
