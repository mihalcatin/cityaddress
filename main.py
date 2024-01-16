class City:
    def __init__(self, city_name, region_name, country_name, citizens_number, zip_code, area_code ):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.citizens_number = citizens_number
        self.zip_code = zip_code
        self.area_code = area_code


    def full_address(self):
        print(f"Kompletná adresa je: {self.city_name}, {self.region_name}, {self.country_name}, pocet obyvatelov je {self.citizens_number}  (2021), postove smerove cislo je: {self.zip_code}, a predvolba je {self.area_code}, ")


Bratislava = City(f"Bratislava", "Bratislavský kraj", "Slovensko", "475 500", "811 01", "+421")
Trnava = City(f"Trnava", "Trnavský kraj", "Slovensko", "62 393 (2022)", "917 01", "+421")
Praha = City(f"Praha", "Praha", "Ceska republika", "1 286 120 (2022)", "100 00", "+420")
Bratislava.full_address()
Praha.full_address()
print(Trnava.citizens_number)