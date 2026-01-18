def is_palindrome(s):
    """
    Проверяет, является ли строка палиндромом.
    Игнорирует регистр и пробелы.
    """
    s = s.replace(" ", "").lower()
    return s == s[::-1]


def factorial(n):
    """
    Вычисляет факториал числа n.
    Если n < 0, возвращает None.
    """
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
