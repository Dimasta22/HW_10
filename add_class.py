from collections import UserDict


class Field:
    ...


class Name(Field):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Phone(Field):
    def __init__(self, phone: str):
        self.phone = phone

    def __str__(self):
        return self.phone


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone.phone)

    def __repr__(self):
        return f'{self.name}, {self.phones}'

    def add_rec(self, addit_phone: Phone = None):
        add_to_dict = AddressBook({self.name.name: self.phones})
        add_to_dict.add_record(addit_phone)
        return add_to_dict

    def change_rec(self, pre_phone: Phone, post_phone: Phone):
        change_in_dict = AddressBook({self.name.name: self.phones})
        change_in_dict.change_record(pre_phone, post_phone)
        return change_in_dict

    def del_rec(self, delete_phone: Phone):
        del_in_dict = AddressBook({self.name.name: self.phones})
        del_in_dict.del_record(delete_phone)
        return del_in_dict


class AddressBook(UserDict):
    def add_record(self, add_phone: Phone = None):
        if add_phone is None:
            self.data.update()
        else:
            [self.data[key].append(add_phone.phone) for key in self.data.keys()]

    def change_record(self, previous_phone: Phone, future_phone: Phone):
        for key, value in self.data.items():
            for num_index in range(len(value)):
                if value[num_index] == previous_phone.phone:
                    value[num_index] = future_phone.phone

    def del_record(self, del_phone: Phone):
        for key, value in self.data.items():
            value.remove(del_phone.phone)


if __name__ == '__main__':

    person_name = Name('Jeka')
    person_phone = Phone('2598')
    person_1 = Record(person_name, person_phone)

    print(person_1)

    print(person_1.add_rec(Phone('1122')))
    print(person_1.add_rec())
    print(person_1.add_rec(Phone('2222')))
    print(person_1.change_rec(Phone('2598'), Phone('3300')))
    print(person_1.del_rec(Phone('2222')))
    print(person_1)




