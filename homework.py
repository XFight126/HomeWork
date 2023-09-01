def is_palindrome(s):
    # Переворачиваем строку
    s = s.lower()
    s = s.replace(" ", "")
    s = s[::-1]
    # Проверяем, является ли строка палиндромом
    if s == s[::-1]:
        return True
    else:
        return False