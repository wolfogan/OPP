class Customer:

    # Constructor class, initialize attributes
    def __init__(self, name, membreship_type):
        self.name = name
        self.membership_type = membreship_type

    # Redefine el método de lectura de un objeto
    def __str__(self):
        return f"{self.name},{self.membership_type}"

c1 = Customer("Victor","Stone")
c2 = Customer("Leonardo","Fire")
customers = [Customer("Susana","Gold"), Customer("Dudmint","Silver"),c1,c2]

for customer in customers:
    print(customer)