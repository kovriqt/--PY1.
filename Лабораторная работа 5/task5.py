import random
def get_random_password(n=None) -> str:
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    if n is None:
        password = (''.join(map(str, random.sample(''.join([uppercase, lowercase, digits]), 8))))
    else:
        password = (''.join(map(str,random.sample(''.join([uppercase, lowercase, digits]), n) )))
    return password
      #TODO написать функцию генерации случайных паролей
print(get_random_password())
