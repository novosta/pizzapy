from pizzapy import Customer, StoreLocator

customer = Customer("Jacob", "Gallardo-Quintero", "jacobgallardoquinteroreal@gmail.com", "5179023105", "10955 E Passion Flower Ln, Tucson, AZ, 85747")

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)

print(my_local_dominos)