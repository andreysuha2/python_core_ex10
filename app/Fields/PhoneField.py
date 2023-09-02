from .Field import Field

class PhoneField(Field):
    current_id = 1
    
    def __init__(self, value: str) -> None:
        super().__init__(value)
        self.id = PhoneField.current_id
        PhoneField.current_id += 1