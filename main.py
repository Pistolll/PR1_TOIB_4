import re

def check_password(password):
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

def validate_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()  # Убираем лишние пробелы и символы новой строки
        if check_password(password):
            print(f'Пароль соответствует требованиям: {password}')

file_path = 'passwords.txt'
validate_passwords(file_path)
