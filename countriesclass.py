class country:
    def __init__(self,country,currency,countid):
        self.country = country
        self.currency = currency
        self.countid = countid
    def newcurrency(self,vara,varb):
        self.currency = vara
        self.countid = varb
    def print(self):
        print("el valor de la moneda ",self.currency," en el pais ",self.country," en ",self.countid)



