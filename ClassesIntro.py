class Animal:
    """Animal class"""
    def __init__(self, name, type):
        self.__name = name
        self.__type = type
        
    @property
    def type(self):
        return self.__type
    
    @property
    def name(self):
        return self.__name
    
    def move(self):
        print('Moving...')
        
class Book():
    """Book class"""
    def __init__(self, name, author, year):
        self.__name = name
        self.__author = author
        self.__year = year
        
    @property
    def name(self):
        return self.__name
    
    @property
    def author(self):
        return self.__author
    
    @property
    def year(self):
        return self.__year
    
class Vehicle():
    """Vehicle class"""
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    
    @property
    def make(self):
        return self.__make
    
    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year