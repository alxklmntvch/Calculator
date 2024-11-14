def main():

    # Ввод данных пользователя
    user_input = input()

    # Разделяем строку по знаку операции
    if '+' in user_input:
        numbers = user_input.split('+')
        operation = '+'
    elif '-' in user_input:
        numbers = user_input.split('-')
        operation = '-'
    elif '*' in user_input:
        numbers = user_input.split('*')
        operation = '*'
    elif '/' in user_input:
        numbers = user_input.split('/')
        operation = '/'
    else:
        return 'throws Exception // т.к. формат математической операции не удовлетворяет заданию - два операнда и ' \
               'один оператор(+, -, /, *)'

    # Проверяем колличество введённых операндов.
    if len(numbers) == 3:
        return 'throws Exception // т.к. формат математической операции не удовлетворяет заданию - два операнда и ' \
               'один оператор(+, -, /, *)'

    # Проверяем, можно ли перевести строки в числа
    try:
        num1 = int(numbers[0].strip())
        num2 = int(numbers[1].strip())
    except ValueError:
        return 'throws Exception'

    # Проверяем условия: операнды не больше 10
    # Если арифм. знак '/' и второй операнд не равен 0.
    if (num1 > 10 or num2 > 10) or (operation == '/' and num2 == 0):
        return 'throws Exception'

    # Если условия ввода верны то делаем вычисления и выводим ответ
    if '+' in user_input:
        result = num1 + num2
        return result
    elif '-' in user_input:
        result = num1 - num2
        return result
    elif '*' in user_input:
        result = num1 * num2
        return result
    elif '/' in user_input:
        result = num1 // num2
        return result


print(main())

