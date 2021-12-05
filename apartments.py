
# discount from the developer = 5%
# average price of apartments

class Apartment:
    # use the dict
    def __init__(self,dict):
        self.city=dict['city']
        self.price_per_meter=dict['price_per_meter']
        self.area=dict['area']

    def full_price(self):
        return round(self.area*self.price_per_meter*0.95,2)

    def print_description(self):
        print(self.city,self.full_price(),'tys zlotych')

    def __repr__(self):
        return self.city+" "+str(self.full_price())
# Example no1
flat_1=Apartment({'city':'Warsaw','price_per_meter':13,'area':50.29})
print(flat_1)
full=flat_1.full_price()
# Example no1
flat_2=Apartment({'city':'Gdansk','price_per_meter':14,'area':62.21})
flat_2.print_description()

if flat_1.full_price()>flat_2.full_price():
    print('More expensive apartments are in',flat_1.city)
else:
    print('More expensive apartments are in',flat_2.city)