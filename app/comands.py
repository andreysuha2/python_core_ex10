from app.AddressBook import AddressBook

ADDRESS_BOOK = AddressBook()

def input_error(handler):
    def inner(args):
        try:
            result = handler(*args)
            return result
        except KeyError:
            return f"Contact {args[0]} doesn't exist!"
        except ValueError:
            return "You are trying to set invalid value"
        except IndexError:
            return "You are sending invalid count of parameters. Please use help comand for hint"
    return inner

@input_error
def add_contact(*args):
    name, phones = args[0], args[1:]
    if name in ADDRESS_BOOK:
        return f'Contact with name "{name}" already exists.'
    ADDRESS_BOOK.add_record(name, phones)
    return f'Contact "{name}" added to conctacts.'

@input_error
def add_phones(*args):
    name, phones = args[0], args[1:]
    record = ADDRESS_BOOK.get_record(name)
    if record and len(phones):
        for phone in phones:
            record.add_phone(phone)
        return f'Phones {", ".join(phones)} added to contact "{name}"'
    elif record and not len(phones):
        return "You send empty phones list"
    return f'Contact with name {name} doesn\'t exist'

@input_error
def change(*args):
    name, phone_id, phone_number = args[0], args[1], args[2]
    record = ADDRESS_BOOK.get_record(name)
    if record:
        result = record.update_phone(phone_id, phone_number)
        results = (
            f'Phone with id "{phone_id}" doen\'t exist for contact {name}',
            f'Contact phone with id "{phone_id}" was changed to {phone_number} for contact "{name}"!'
        )
        return results[bool(result)]
    return f'Contact with name "{name}" doesn\'t exist.'

@input_error
def phones (*args):
    name = args[0]
    record = ADDRESS_BOOK.get_record(name)
    if record:
        string = f"Contact '{record.name.value}':\n"
        for phone in record.phones:
            string += f"{phone.id}: {phone.value}\n"
        return string
    return f'Contact with name "{name}" doesn\'t exist.'

@input_error
def remove_phone(*args):
    name, phone_id = args[0], args[1]
    record = ADDRESS_BOOK.get_record(name)
    if record:
        result = record.remove_phone(phone_id)
        results = (
            f'Phone with id "{phone_id}" doen\'t exist for contact {name}',
            f'Contact phone with id "{phone_id}" was removed from contact "{name}"!'
        )
        return results[bool(result)]
    return f'Contact with "{name}" doesn\'t exist.'

@input_error
def remove_contact(*args):
    name = args[0]
    if name in ADDRESS_BOOK:
        ADDRESS_BOOK.pop(name)
        return f'Contact "{name}" removed from address book'
    return f'Contact "name" does\'t exists in address book'

@input_error
def show_all(*args):
    if len(args):
        raise IndexError
    output = "---CONTACTS---\n"
    if len(ADDRESS_BOOK):
        for record in ADDRESS_BOOK.values():
            phones = ", ".join([ phone.value for phone in record.phones ])
            output += f"{record.name.value} : {phones}\n"
        return output[:-1]
    else:
        output += "Contacts are empty"
        return output
    
@input_error    
def help(*args):
    return """
        --- CONTACTS HELP ---
        syntax: add contact {name} {phone(s)}
        description: adding number to contacts list 
        example: add contact ivan +380999999999 +380777777777

        syntax: add phones {name} {phone(s)}
        description: adding number to contacts list 
        example: add phones ivan +380999999999 +380777777777

        syntax: change {name} {phone_id} {phone}
        description: changing phone number for contact
        example: change ivan 1 +380999999999

        syntax: phones {name}
        description: finding phones numbers by contact name
        example: phone ivan

        syntax: remove contact {name}
        description: removing contact from contacts list
        example: remove ivan

        syntax: remove phone {name} {id}
        description: removing contact from contacts list
        example: remove ivan 1

        syntax: show all
        description: showing list of contacts
        example: show all
    """

CLOSE_COMANDS = ("good bye", "close", "exit")
HANDLERS = {
    "add contact": add_contact,
    "add phones": add_phones,
    "change": change,
    "phones": phones,
    "remove phone": remove_phone,
    "remove contact": remove_contact,
    "show all": show_all,
    "help": help
}