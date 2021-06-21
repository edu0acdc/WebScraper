from shop import Shop

if __name__ == '__main__':
    s = Shop('Test Shop', url='https://webscraper.io/test-sites/e-commerce/allinone')
    for p in s.products:
        print(p, "\n-------------")
