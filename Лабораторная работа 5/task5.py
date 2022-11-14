import random
import string
def get_random_password(n=None) -> str:
    if n is None:
        password = (''.join(map(str, random.sample(''.join([string.ascii_uppercase, string.ascii_lowercase, string.octdigits]), 8))))
    else:
        password = (''.join(map(str,random.sample(''.join([string.ascii_uppercase, string.ascii_lowercase, string.octdigits]), n) )))
    return password
      #TODO написать функцию генерации случайных паролей
print(get_random_password())
