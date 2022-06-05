from handler import handler


def main():
    print('Вас приветствует Бот-помощник')
    print('Комманды доступные Вам: hello, add, change, phone, show all, exit, good bye, close')
    print('Правильная запись: комманда, параметри')
    print('Все пишеться через пробел')
    print('Параметры add: Имя телефон')
    print('Параметры change: Имя и новый телефон')
    print('Параметр phone: Имя')

    while True:
        command = input('Введите название комманды и параметры: ')
        if handler(command) is False:
            print('До новых встреч!')
            break
        print(handler(command))


if __name__ == '__main__':
    main()


