class Car:
    def __init__(self, color, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def car_info(self):
        print(f'This car is a {self.color} {self.make} {self.model}. It is a {self.year} version.')

my_car = Car('White', 'Toyota', 'Corolla', 2004)

my_car.car_info()


        



















