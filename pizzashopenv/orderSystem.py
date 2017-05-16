#this is the main class to be used for ordering the Pizza form with the HElp of APi
from urllib import urlopen
import json
import requests
from urllib2 import Request, urlopen, URLError

class Pizza():

    def __init__(self, menuid):
        response = requests.get("https://f10fl1j22j.execute-api.us-east-1.amazonaws.com/Nakshay/menu/"+ menuid)
        try:

	        pizza_menu = response.json()
        except URLError, e:
            print 'No Menu', e
        self.menu_id = pizza_menu.get('Items')[0].get('menu_id')
        self.pizza_option = pizza_menu.get('Items')[0].get('selection')
        self.pizza_size = pizza_menu.get('Items')[0].get('size')
        self.pizza_cost = pizza_menu.get('Items')[0].get('price')
        self.pizza_store_hours = pizza_menu.get('Items')[0].get('store_hours')
        # store name = pizzaMenu.get('Items')[0].get('store_name')

    def getMenu(self):
        return self.menu_id

    def getSizes(self):
        return self.pizza_size

    def getOptions(self):
        return self.pizza_option


class Order():

    def __init__(self, size, selection, person):
        self.size = size
        self.selection = selection
        self.person =person
        self.info = None
        self.order = None

    def getInfo(self):
        return self.person

    def setInfo(self, info):
        self.info = info

    def setSize(self, size):
        self.size = size

    def setOption(self, selection):
        self.selection = selection

    def getOrder(self):
        return self.order

    def placeOrder(self, size, selection, person, price):
        return "Response with orderId"



class Person():

    def __init__(self, person_name, person_phone, person_email):
        self.person_name = person_name
        self.person_phone = person_phone
        self.person_email = person_email

    def getPersonName(self):
        return self.person_name

    def getPersonPhone(self):
        return self.person_phone

    def getPersonEmail(self):
        return self.person_email


def main():

    order = Pizza("UUID-generated-by-client")
    MrJack = Person("Jack Gomez", "+1 669 856 7856", "jack.gomez@gmail.com")
    strn = "Hello " + str(MrJack.getPersonName()) + "would you like to place an order from the following Menu" + str(order.getMenu())
    i = raw_input(strn)
    if i == "Y" or i =="y" :
        input_option = raw_input("Please select an option from the following " + str(order.getOptions()))
        input_size = raw_input("Please select any Size form the following" + str(order.getSizes()))
    print "Your Order reciept"
    orderreciept = {}
    orderreciept['name'] = str(MrJack.getPersonName())
    orderreciept['selcted'] = input_option
    orderreciept['size'] = input_size
    orderreciept['price'] = '$25'
    print orderreciept

main()



