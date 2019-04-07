#imports the pizzapi library
from pizzapi import *

#Fills in the customer class by asking the user various questions
first_name = raw_input("What is your first name: ")
last_name = raw_input("What is your last name: ")
email = raw_input("What is your email: ")
phone = raw_input("What is your phone number: ")
customer = Customer(first_name, last_name, email, phone)

#Finishes the adress class
first_address_line = raw_input("What is the first line of your adress: ")
State = raw_input("What State do you live in (Use shortened version like NY or CA): ")
City = raw_input("What city do you live in: ")
ZipCode = raw_input("What is your ZipCode: ")
address = Address(first_address_line, City, State, ZipCode)
store = address.closest_store()

#stores the menu in the variable "menu"
menu = store.get_menu()

#asks the user which menu items they would like to see
i=0
while(True):
	print("When asking to look at menu items use the most vague terms you can like \"Piza\" or  \"Coke\"")
	show_menu = raw_input("What menu items would you like to see: ")
	print(menu.search(Name=show_menu))
	choice = raw_input("Would you like to look at another menu item (y/n): ")
	if(choice == "n"):
		break

#Asks the customer for their order, and then places their order
i = 0
orderArray = []
order = Order(store, customer, address)
while(True):
	orderArray.append(raw_input("What would you like to order: "))
	yesono = raw_input("Is {} the correct menu item (y/n): ".format(orderArray[i]))
	if(yesono == "y"):
		order.add_item(orderArray[i])
		i = i+1
		question = raw_input("Are you done with your order (y/n): ")
		if(question == "y"):
			break
	else:
		order.remove_item(orderArray[i])
print("This is your order: ")
print(orderArray)

#Asks the user for their card and then places the order
card = PaymentObject(raw_input("What is your card number: "), raw_input("When is your expiration date (no slashes. ex: 0115): "), raw_input("What is your CVV: "), ZipCode)
abort = raw_input("Would you like to abort this payment (y/n): ")
if(abort == "y"):
	print("Your order in camcelled")
else:
	print("Your order has been placed")
	order2.place(card)
