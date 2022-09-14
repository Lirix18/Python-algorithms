"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# сложность O(1)
def aut1(users, name, password):
    if users.get(name):
        if users[name]['password'] == password and users[name]['activation']:
            return "Access is allow!"
        elif users[name]['password'] == password and not users[name]['activation']:
            return 'Access is denied! Complete activation.'
        elif users[name]['password'] != password:
            return "Incorrect password!"
    else:
        return 'User is not found!'


# сложность O(n)
def aut2(users, name, password):
    for k, v in users.items():
        if k == name:
            if v['password'] == password and v['activation']:
                return "Access is allow!"
            elif v['password'] == password and not v['activation']:
                return 'Access is denied! Complete activation.'
            elif v['password'] != password:
                return "Incorrect password!"
        else:
            return 'User is not found!'
