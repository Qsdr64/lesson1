from smartphone import Smartphone
catalog = [
    Smartphone("APPLE","Iphone 13"," " "+79270000000"),
    Smartphone("Samsung","Galxy 23"," " "+79021111111"),
    Smartphone("XIAOMI", "12lite"," " "+79092222222"),
    Smartphone("Nokia","3310"," " "+79273333333"),
    Smartphone("Honor","8X"," " "+79274444444")

]
for smartphone in catalog:
    print(f"{smartphone.phonebrand} - {smartphone.phonemodel}.{smartphone.subscribernumber}")