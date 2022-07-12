# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):

    def __init__(self, *args):
        pass


class NotEmailError(Exception):

    def __init__(self, *args):
        pass


class RegistrationLogParser:

    def __init__(self, file_name):
        self.file_name = file_name

    def parser(self):
        with open(file=self.file_name, mode='r', encoding='utf8') as log:
            for line in log:
                try:
                    name, email, age = line[:-1].split(' ')
                    with open(file='registrations_good.log', mode='a', encoding='utf8') as file_log:
                        if name.isalpha():
                            if '@' and '.' in email:
                                if int(age) in range(10, 100):
                                    file_log.write(line)
                                else:
                                    raise ValueError(f'Неправильный возраст!')
                            else:
                                raise NotEmailError(f'Неправильный E-mail!')
                        else:
                            raise NotNameError(f'Имя должно состоять только из букв!')
                except ValueError as exc:
                    with open(file='registrations_bad.log', mode='a', encoding='utf8') as bad_line:
                        bad_line.write(f'В строке "{line[:-1]}" {exc.args[0]}\n')
                        continue
                except NotEmailError as exc:
                    with open(file='registrations_bad.log', mode='a', encoding='utf8') as bad_line:
                        bad_line.write(f'В строке "{line[:-1]}" {exc.args[0]}\n')
                        continue
                except NotNameError as exc:
                    with open(file='registrations_bad.log', mode='a', encoding='utf8') as bad_line:
                        bad_line.write(f'В строке "{line[:-1]}" {exc.args[0]}\n')
                        continue
                except Exception as exc:
                    with open(file='registrations_bad.log', mode='a', encoding='utf8') as bad_line:
                        bad_line.write(f'В строке "{line[:-1]}" что-то совсем плохо!\n')
                        continue


parser = RegistrationLogParser(file_name='registrations.txt')
parser.parser()
