import random

def generate_email():
    student_name = 'tarasov_anton'
    cohort_number = "23"  
    random_digits = str((random.randint(100, 999)))
    email_domain = '@yandex.ru'
    return f"{student_name}_{cohort_number}_{random_digits}{email_domain}"

def generate_password():
    return f"Qwerty{random.randint(100, 999)}"