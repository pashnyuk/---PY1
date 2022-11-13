import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def get_random_password() -> str:
    random_password = ""
    i = random.sample(alphabet, 8)
    random_password += str(i)
    return random_password


print(get_random_password())
