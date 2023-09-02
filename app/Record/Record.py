from app.Fields import NameField, PhoneField
from app.address_utils import find_index

class Record:
    def __init__(self, name: str, phones: list = [] ) -> None:
        self.name = NameField(name)
        self.phones = list(map(lambda phone: PhoneField(phone), phones))

    def get_phone_index(self, id):
        return find_index(lambda phone: phone.id == int(id), self.phones)

    def has_phone(self, phone_id: str):
        index = self.get_phone_index(phone_id)
        return index != -1

    def add_phone(self, phone: str) -> None:
        self.phones.append(PhoneField(phone))

    def remove_phone(self, phone_id: str) -> None:
        index = self.get_phone_index(phone_id)
        if index != -1:
            self.phones.pop(index)
            return True
        return False

    def update_phone(self, phone_id: str, phone_number: str) -> None:
        index = self.get_phone_index(phone_id)
        if index != -1:
            self.phones[index].value = phone_number
            return True
        return False