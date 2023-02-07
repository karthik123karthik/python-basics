class Vehicle:
    def __init__(self, model, type):
        self.model = model
        self.type = type


car = Vehicle("2013", "4 wheeler")
print(dir(car))
print(car.__dict__)
print(help(Vehicle))
