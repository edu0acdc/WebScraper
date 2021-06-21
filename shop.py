from scraper import scrapShop


class Shop():
    '''
    A Class that represents a simple Shop
    '''

    def __init__(self, name, url=None):
        self.name = name
        if url:
            # Scraper
            self.products = scrapShop(url)
        else:
            self.products = []
