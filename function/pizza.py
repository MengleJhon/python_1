def make_pizza(size,*toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the fpllowing toppings:")
    for topping in toppings:
        print("- " + topping)

# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')