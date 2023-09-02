import json
import os
from pathlib import Path
from typing import Optional
from collections import UserDict
from ..Record import Record


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
DICTIONARY_PATH = Path(os.path.join(__location__, "data.json"))

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        dictionary = {}
        try:
            with open(DICTIONARY_PATH, 'r', encoding='utf-8') as dictionary_file:
                dictionary = json.load(dictionary_file)
        except FileNotFoundError:
            print('Dictionary file not found, file will be create when you finishing your work!')
        for name, phones in dictionary.items():
            self.add_record(name, phones)

    def save_book(self):
        dictionary = {}
        for record in self.data.values():
            dictionary[record.name.value] = [ phone.value for phone in record.phones ]
        with open(DICTIONARY_PATH, "w") as dictionary_file:
            json.dump(dictionary, dictionary_file) 

    def add_record(self, name: str, phones: list = []) -> None:
        if not name in self.data:
            self.data[name] = Record(name, phones)

    def get_record(self, name: str) -> Optional[Record]:
        if name in self.data:
            return self.data[name]