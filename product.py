class Product():
    ''' 
    A Class that represent a simple Product for web scraping
    '''

    def __init__(self, name, price, currency, description=None, link=None):
        self.name = name
        self.price = price
        self.description = description
        self.currency = currency
        self.link = link

    def setDescription(self, description):
        self.description = description

    def __str__(self):
        return "Name : "+self.name+"\nPrice : "+str(self.price)+self.currency+"\nDescription : "+self.description+"\nLink : "+self.link

    def __repr__(self):
        return self.__str__()
