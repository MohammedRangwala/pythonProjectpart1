#Mohammed Rangwala

import csv
import os
from datetime import datetime

#ElectronicsStoreInventory class
class ElectronicsStoreInventory:
    #Items list to store the dictionary of all input data
    ItemsList = []
    def __init__(self):
        self.getInput()                     #calls function to get input data from file
        self.callInventoryFunctions()       #calls function to generate different inventories
#Functions to generate different inventories
    #Function to generate full inventory
    def FullInventory(self):
        sortedItemslist = sorted(self.ItemsList, key = lambda i: i['Manufacturer Name'])    #Sorts the itemslist by manufacturer name
        for dictt in sortedItemslist:
            with open('Output/FullInventory.csv', 'a', newline='') as csvfile:     #reads the items from the full inventory file row wise
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(dictt.values())                                      #write these extracted items from full inventory file 

    #Function to generate damaged items inventory
    def DamagedInventory(self):
        sortedItemslist = sorted(self.ItemsList, key = lambda i: i['Price'],reverse=True)       #Sorts the items by price from most expensive to least expensive
        for dictt in sortedItemslist:
            if(dictt.get("Item Status") == "damaged"):                  #checks item status (if item is damaged or not)
                with open('Output/DamagedInventory.csv', 'a', newline='') as csvfile:      #reads the items from the damaged inventory file row wise
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())                                 #write these extracted items from damaged inventory file 
                    
    #Function to generate laptop inventory       
    def LaptopInventory(self):
        sortedItemslist = sorted(self.ItemsList, key = lambda i: i['id'])   #Sorts the data by item id
        for dictt in sortedItemslist:
            if(dictt.get("Item Type") == "laptop"):                     #checks items from dictionary (if item is laptop or not)
                with open('Output/LaptopInventory.csv', 'a', newline='') as csvfile:       #reads the items from the laptop inventory file row wise
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())                         #write these extracted items from laptop inventory file 

    #Function to generate past service date inventory
    def ServiceDateInventory(self):
        sortedItemslist = sorted(self.ItemsList, key = lambda i: i['Service Date'])     #Sorts the data by service date
        for dictt in sortedItemslist:
            date_object= datetime.strptime(dictt.get("Service Date"), "%m/%d/%Y")              #Gets date from dictionary iand converts it into date object
            now = datetime.today()                                                             #Gets the current date when program executes
            if(now > date_object):
                with open('Output/PastServiceDateInventory.csv', 'a', newline='') as csvfile:      #items service date past from program executed date
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())  
            if(now < date_object and dictt.get("Item Status") == ""):                                   #items service date not past from program executed date
                with open('Output/ValidInventory.csv', 'a', newline='') as csvfile:            #Generates a valid items not past from the program executed date
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values()) 

    #Function to generate tower inventory
    def TowerInventory(self):
        sortedItemslist = sorted(self.ItemsList, key = lambda i: i['id'])       #Sorts the data by item id
        for dictt in sortedItemslist:
            if(dictt.get("Item Type") == "tower"):                              #checks items from dictionary (if item is tower or not)
                with open('../../../PycharmProjects/FinalProject/Output/TowerInventory.csv', 'a', newline='') as csvfile:        #reads the items from the tower inventory file row wise
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())

    #Function to generate phone inventory
    def PhoneInventory(self):
        sortedItemslist = sorted(self.ItemsList, key = lambda i: i['id'])           #Sorts the data by item id
        for dictt in sortedItemslist:
            if(dictt.get("Item Type") == "phone"):                                  #checks items from dictionary (if item is phone or not)
                with open('Output/PhoneInventory.csv', 'a', newline='') as csvfile:        #reads the items from the tower inventory file row wise
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())

    #Function to get input from the inventory files
    def getInput(self):
        file = "InputFiles/ManufacturerList.csv"            #manufacturer list path is given
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')      #Reads Manufacturer list file and gets all the data
            for row in spamreader:
                    stringItem = "".join(row)                                       #Makes a list by joining all the items to a string
                    iteminfo = stringItem.split(",")                                     #Makes a list by splitting it with ","
                    #Dictionary to store all the data
                    dict = {"id": iteminfo[0],"Manufacturer Name": iteminfo[1],"Item Type": iteminfo[2],"Price": "", "Service Date": "", "Item Status":iteminfo[3] }
                    self.ItemsList.append(dict)                                         #Puts dictionary into items list


        #Gets data from price list and makes a list of the prices
        priceList = []
        file = "InputFiles/PriceList.csv"           #price list path is given
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')      #Reads price list file and gets all the data
            for row in spamreader:
                stringItem = "".join(row)                       #Makes a list by joining all the items to a string
                iteminfo = stringItem.split(",")                #Makes a list by splitting it with ","
                priceList.append(iteminfo)

        #Compares data by item's id and defines its price
        for Id, price in priceList:
            for dictionary in self.ItemsList:
                if(Id == dictionary.get("id")):
                    dictionary["Price"] = price

        #Getting data from ServiceDateList and making a list of dates
        serviceList = []
        file = "InputFiles/ServiceDatesList.csv"    #service list path is given
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                stringItem = "".join(row)               #Makes a list by joining all the items to a string
                iteminfo = stringItem.split(",")         #Makes a list by splitting it with ","
                serviceList.append(iteminfo)
        #Comparing the data by it's id and defining its date
        for Id, date in serviceList:
            for dictionary in self.ItemsList:
                if(Id == dictionary.get("id")):
                    dictionary["Service Date"] = date

        #Removing the inventory files if exists so the new data can be created
        try:
            os.remove("Output/FullInventory.csv")
            os.remove("Output/DamagedInventory.csv")
            os.remove("Output/LaptopInventory.csv")
            os.remove("Output/PhoneInventory.csv")
            os.remove("Output/PastServiceDateInventory.csv")
            os.remove("Output/TowerInventory.csv")
            os.remove("Output/ValidInventory.csv")
        except Exception as e:
            pass

    #Functions calls to all inventories functions
    def callInventoryFunctions(self):
        self.FullInventory()
        self.DamagedInventory()
        self.LaptopInventory()
        self.ServiceDateInventory()
        self.TowerInventory()
        self.PhoneInventory()

    #Function to get the details of specific item 
    def getItem(self, name):
        #Reading the details from valid inventory and comparing the values and returning valid item dictionary and recommendeded item dictionary
        validItemList = []
        file = "Output/ValidInventory.csv"
        with open(file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                stringItem = "".join(row)
                iteminfo = stringItem.split(",")
                dict = {"Item ID": iteminfo[0],"Manufacturer Name": iteminfo[1],"Item Type": iteminfo[2],"Price": iteminfo[3], "Service Date": iteminfo[4], "Item Status":iteminfo[5] }
                validItemList.append(dict)
        matcheditemslist = []
        itemNamesList =  []
        itemTypeList = []
        for dictt in validItemList:
            itemNamesList.append(dictt.get("Manufacturer Name"))
            itemTypeList.append(dictt.get("Item Type"))
        stringList = name.split()
        manufacturerName = ""
        itemType_ = ""

        for i in range(len(stringList)):
            for j in range(len(itemNamesList)):
                if(stringList[i].lower() == itemNamesList[j].lower()):
                    manufacturerName = itemNamesList[j]
                if(stringList[i] == itemTypeList[j]):
                    itemType_ = itemTypeList[j]
        #print
        for dictt in validItemList:
            if(dictt.get("Manufacturer Name") == manufacturerName and dictt.get("Item Type") == itemType_):
                matcheditemslist.append(dictt)
            if(dictt.get("Manufacturer Name") != manufacturerName and dictt.get("Item Type") == itemType_):
                recommended = dictt
        if(len(matcheditemslist) >0 ):
            sortedItemslist = sorted(matcheditemslist, key = lambda i: i['Price'])
            return sortedItemslist[0], recommended

ElectronicsStoreInventory
            




