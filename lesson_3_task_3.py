from address import Address
from mailing import Mailing

to_address = Address(
    index="123456",
    city="Москва",
    street="Ленина",
    house="10",
    apartment="15"
)

from_address = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский",
    house="5",
    apartment="7"
)

shipment = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=2500.75,
    track="AB123456789RU"
)

print(f"Отправление {shipment.track} из {shipment.from_address.index}, {shipment.from_address.city}, "
      f"{shipment.from_address.street}, {shipment.from_address.house} - {shipment.from_address.apartment} "
      f"в {shipment.to_address.index}, {shipment.to_address.city}, {shipment.to_address.street}, "
      f"{shipment.to_address.house} - {shipment.to_address.apartment}. Стоимость {shipment.cost} рублей.")