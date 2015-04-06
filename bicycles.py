class Bicycle(object):
    def __init__(self, model, weight, wholesale):  # constructor method
        self.model = model
        self.weight = weight
        self.wholesale = wholesale
        self.retail = 0

    def hello(self):
        print "the {}, which weighs {} pounds and retails for ${} dollars.".format(self.model, self.weight, self.retail)

    def set_retail_price(self, retail):
        self.retail = retail


class BikeShop(object):
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.total_profit = 0
        self.profit_factor = 0.2

    def hello(self):
        print "Welcome to {} :)".format(self.name)

    def add_to_inventory(self, new_bike):
        retail_price = self.calculate_retail_price(new_bike)
        new_bike.set_retail_price(retail_price)
        self.inventory.append(new_bike)

    def display_inventory(self):
        print "Our inventory now includes:"
        for bike in self.inventory:
            bike.hello()

    def find_affordable_bike(self, customer_budget):
        bikes_in_budget = []
        for bike in self.inventory:
            if bike.retail <= customer_budget:
                bikes_in_budget.append(bike)
                print "The {} is in your budget.".format(bike.model)
            else:
                print "The {} is not in your budget.".format(bike.model)
        return bikes_in_budget

    def sell_bike(self, bike):
        one_bike_profit = self.calculate_profit(bike)
        self.total_profit += one_bike_profit
        self.inventory.remove(bike)

    def show_profit(self):
        print "Total Profit is $" + str(self.total_profit)

    def calculate_retail_price(self, bike):
        retail = (1.0 + self.profit_factor) * bike.wholesale
        return int(retail)

    def calculate_profit(self, bike):  # calculate profit is called by add_to_inventory, calculate 20% profit
        retail = self.calculate_retail_price(bike)
        cost = bike.wholesale
        profit = retail - cost
        return profit


class Customers(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.purchased_bikes = []

    def print_budget(self, bike):
        pass

    def buy_bike(self, bike):
        self.budget = self.budget - bike.retail
        self.purchased_bikes.append(bike)

    def hello(self):
        print "Hello! my name is {} and I have {} dollars in my budget. Which bikes         can I buy based on my budget?".format