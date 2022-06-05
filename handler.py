from parser import parser
from input_error import input_error
from add_class import Record, AddressBook, Name, Phone


@input_error
def handler(sentence: str, phone_dict={}):
    def all_function(sentence: str):

        if parser(sentence) == 'HELLO':
            return "How can I help you?"

        if parser(sentence) == 'SHOW ALL':
            return '\n'.join(f'{key}: {value}' for key, value in phone_dict.items())

        if parser(sentence) in ['EXIT', 'CLOSE', 'GOOD BYE']:
            return False

        if parser(sentence) is None:
            return 'Введите команду из списка доступных команд!'

        if parser(sentence) == 'ADD':
            _, name, number, *args = sentence.split(' ')
            name = Name(name)
            phone = Phone(number)
            record = Record(name, phone)
            record.add_rec()
            phone_dict.update({record.name.name: record.phones})

        if parser(sentence) == 'PHONE':
            _, name, *args = sentence.split(' ')
            return phone_dict.get(name, 'Такого пользователья нет')

        if parser(sentence) == 'CHANGE':
            _, name, new_number, *args = sentence.split(' ')
            phone_dict[name] = new_number
            # Тут будет изменен подход: другой ввод: change (del_num, add_num, change_num), имя и номер
            # Имя и номер идут в рекорд, а пока, код работает в add_class

        return 'Операция прошла успешно'
    return all_function(sentence)


if __name__ == '__main__':
    sentence = 'add Vlad 067 Vlad 050 vfd    ljh'
    print(handler(sentence))