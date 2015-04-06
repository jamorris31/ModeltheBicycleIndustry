import bicycles


def main():
    # create larry's bike shop
    larry_bike_shop = bicycles.BikeShop("Larry's Bicycle Shop")

    larry_bike_shop.hello()
    print "\n"

    # create list of bicycles
    red_racer = bicycles.Bicycle("Red Racer", 60, 100)
    blue_screamer = bicycles.Bicycle("Blue Screamer", 65, 150)
    green_goblin = bicycles.Bicycle("Green Goblin", 70, 350)
    white_lightning = bicycles.Bicycle("White Lightning", 40, 450)
    silver_bullet = bicycles.Bicycle("Silver Bullet", 35, 550)
    purple_thunder = bicycles.Bicycle("Purple Thunder", 30, 800)

    # create some customers
    lana = bicycles.Customers("Lana", 200)
    derin = bicycles.Customers("Derin", 500)
    adam = bicycles.Customers("Adam", 1000)

    # ship bikes to bike store
    larry_bike_shop.add_to_inventory(red_racer)
    larry_bike_shop.add_to_inventory(blue_screamer)
    larry_bike_shop.add_to_inventory(green_goblin)
    larry_bike_shop.add_to_inventory(white_lightning)
    larry_bike_shop.add_to_inventory(silver_bullet)
    larry_bike_shop.add_to_inventory(purple_thunder)

    # display inventory
    larry_bike_shop.display_inventory()
    print "\n"

    # lana walks in and wants to know her options
    lana.hello()
    lana_bike_list = larry_bike_shop.find_affordable_bike(lana.budget)
    print "Your bike list has {} possibilities".format(len(lana_bike_list))
    # print "the {} and the {}".format(lana_bike_list)

    # Lana buys a bike
    if len(lana_bike_list) >= 1:
        purchased_bike = lana_bike_list[0]
        lana.buy_bike(purchased_bike)
        larry_bike_shop.sell_bike(purchased_bike)
        print "Thanks for purchasing the {} for ${}, {}! You now have ${} left in your budget".format(
            purchased_bike.model, purchased_bike.retail, lana.name, lana.budget)
        print "\n"
    # Derin walks in and wants to know his options
    derin.hello()

    derin_bike_list = larry_bike_shop.find_affordable_bike(derin.budget)

    # Derin buys a bike
    if len(derin_bike_list) >= 1:
        purchased_bike = derin_bike_list[0]
        derin.buy_bike(purchased_bike)
        larry_bike_shop.sell_bike(purchased_bike)
        print "Thanks for purchasing the {} for ${}, {}! You now have ${} left in your budget".format(
            purchased_bike.model, purchased_bike.retail, derin.name, derin.budget)
        print "\n"

    # Adam walks in and wants to know his options
    adam.hello()

    adam_bike_list = larry_bike_shop.find_affordable_bike(adam.budget)

    # Adam buys a bike
    if len(adam_bike_list) >= 1:
        purchased_bike = adam_bike_list[0]
        adam.buy_bike(purchased_bike)
        larry_bike_shop.sell_bike(purchased_bike)
        print "Thanks for purchasing the {} for ${}, {}! You now have ${} left in           your budget".format(
            purchased_bike.model, purchased_bike.retail, adam.name, adam.budget)

    print "\n"
    larry_bike_shop.show_profit()
    print "\n"
    larry_bike_shop.display_inventory()


if __name__ == "__main__":
    main()