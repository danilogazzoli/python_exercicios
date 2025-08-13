#Dependency Inversion Principle (DIP)
#Abstractions should not depend upon details. Details should depend upon abstractions.

#That sounds pretty complex. Here’s an example that will help to clarify it. 
# Say you’re building an application and have a FrontEnd class to display data to the users in a friendly way.
#  The app currently gets its data from a database, so you end up with the following code:

class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"
    

#the FrontEnd class depends on the BackEnd class and its concrete implementation. 
# You can say that both classes are tightly coupled. This coupling can lead to scalability issues. 
# For example, say that your app is growing fast, and you want the app to be able to read data from a REST API.    

# To fix the issue, you can apply the dependency inversion principle and make your classes depend on abstractions rather than on concrete implementations 
# like BackEnd. 
# In this specific example, you can introduce a DataSource class that provides the interface to use in your concrete classes:

# app_dip.py

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"
    

db_front_end = FrontEnd(Database())
db_front_end.display_data()


api_front_end = FrontEnd(API())
api_front_end.display_data()    