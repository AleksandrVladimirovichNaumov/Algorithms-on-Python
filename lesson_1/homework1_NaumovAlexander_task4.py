"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

users = {
    'Obama': ['first_afro-american_president', False],
    'Trump': ['rich_president', False],
    'Biden': ['current_president', True]
}


def white_house_authentication_1(login, password):
    """
    function checks login, password and status of incomer
    :param login: login of incomer
    :param password: password of incomer
    :return: 'Passed.', 'Incorrect password or login.', 'Account is deactivated. Please win president's leadership.'
    T(n) = 1 + 1 + 1 + n + max(max((1 + 1), (1 + 1)), (1 + 1)) = 5 + n
    O(n) = n
    """
    if users.get(login, [None])[0] == password:         # O(1) + O(1) + O(1) + O(n)
        if users.get(login)[1]:                         # O(1) + O(1)
            return login + ', you passed.'              # O(1) + O(1)   // did not find info about stings sum.
        else:
            return login + ", your account is deactivated. Please win a president's leadership."  # O(1) + O(1)
    else:
        return login + ', incorrect password or login.'  # O(1) + O(1)


def white_house_authentication_2(login, password):
    """
    function checks login, password and status of incomer
    :param login: login of incomer
    :param password: password of incomer
    :return: 'Passed.', 'Incorrect password or login.', 'Account is deactivated. Please win president's leadership.'
    T(n) = 1 + n + 1 + 1 + max((1 + 1), (1 + 1)) + 1 + n + 1 + 1 = 2 * n + 8
    O(n) = n
    """
    if users.get(login, None) == [password, True]:          # O(1) + O(n) + O(1) + O(1)
        return login + ', you passed.'                      # O(1) + O(1)
    elif users.get(login, None) == [password, False]:       # O(1) + O(n) + O(1) + O(1)
        return login + ", your account is deactivated. Please win a president's leadership." # O(1) + O(1)
    else:
        return login + ', incorrect password or login.'     # O(1) + O(1)


"""
Results:
1) both functions have same complexity O(n) = n
2) first function will work faster because coefficient before n is smaller than for second function n < 2 * n
"""


print(white_house_authentication_1('Putin', 'Surprised?'))
print(white_house_authentication_1('Obama', 'first_afro-american_president'))
print(white_house_authentication_1('Trump', 'still_rich_president'))
print(white_house_authentication_1('Biden', 'forgot_my_password'))
print(white_house_authentication_1('Biden', 'current_president'))
print('*' * 100)
print(white_house_authentication_2('Putin', 'Surprised?'))
print(white_house_authentication_2('Obama', 'first_afro-american_president'))
print(white_house_authentication_2('Trump', 'still_rich_president'))
print(white_house_authentication_2('Biden', 'forgot_my_password'))
print(white_house_authentication_2('Biden', 'current_president'))

