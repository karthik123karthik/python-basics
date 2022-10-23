# creating a class
class Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership

    def take_membership(self):
        self.membership = True

# creating an object


c1 = Customer("karthik", False)
print(c1.membership)
# take membership
c1.take_membership()
print(c1.membership)


