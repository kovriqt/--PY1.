import random
import string
def get_random_password(n=None) -> str:
    if n is None:
        password ='error'
    else:
        password =''.join(random.sample(''.join([string.ascii_uppercase, string.ascii_lowercase, string.octdigits]), n))
    return password
      #TODO написать функцию генерации случайных паролей
print(get_random_password(7))
