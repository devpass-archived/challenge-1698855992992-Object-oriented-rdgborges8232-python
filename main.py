class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_on = False

    def start_engine(self):
        self.engine_on = True

    def stop_engine(self):
        self.engine_on = False

if __name__ == '__main__':
    car = Car('Tesla', 'Model S', 2022)
    print(car.make)  # Expected: Tesla
