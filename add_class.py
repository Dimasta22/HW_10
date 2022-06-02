from collections import UserDict


class Name:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Phone:
    def __init__(self, phone: list):
        self.phone = phone

    def __str__(self):
        return self.phone


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f'{self.name}, {self.phone}'

    def add_rec(self, value: dict):
        value.update({self.name.name: self.phone.phone})

    def change_rec(self, value: dict, change_phone: Phone):
        value[self.name.name] = change_phone.phone

    def del_rec(self, value: dict):
        value.pop(self.name.name)


class AddressBook(UserDict):
    def add_record(self, value: Record):
        self.data.update({value.name.name: value.phone.phone})

    def change_record(self, value: Record, change_phone: Phone):
        self.data[value.name.name] = change_phone.phone

    def del_record(self, value: Record):
        self.data.pop(value.name.name)


if __name__ == '__main__':

    data_2 = {'Dima': ['067', '550']}

    person_name = Name('Jeka')
    person_phone = Phone(['067', '550'])
    person_1 = Record(person_name, person_phone)

    person_1.add_rec(data_2)

    print(data_2)

    new_person_phone = Phone(['380'])
    person_1.change_rec(data_2, new_person_phone)
    print(data_2)

    remove_person_name = Name('Dima')
    person_1 = Record(remove_person_name)
    person_1.del_rec(data_2)
    print(data_2)

    ###################################################################

    data_1 = {'Jeka': ['067', '550']}

    person_name = Name('Dima')
    person_phone = Phone(['067'])
    person_2 = Record(person_name, person_phone)

    record = AddressBook(data_1)
    record.add_record(person_2)
    print(record)

    new_phone = Phone(['78956'])
    person_2 = Record(person_name, new_phone)

    record = AddressBook(data_1)
    record.add_record(person_2)
    print(record)

    del_name = Name('Jeka')
    person_2 = Record(del_name)

    record = AddressBook(record)
    record.del_record(person_2)
    print(record)