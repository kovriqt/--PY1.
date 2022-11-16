import random
import string
def get_random_password(n=None) -> str:
    if n is None:
        password ='error'
    else:
        book=''.join([string.ascii_uppercase, string.ascii_lowercase, string.octdigits])
        password =''.join(random.sample(book, n))
    return password
      #TODO написать функцию генерации случайных паролей
print(get_random_password(7))
