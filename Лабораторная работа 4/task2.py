def get_count_char(main_str):
    m=main_str.lower()
    dict = {}
    for i in m:
        if i.isalpha():
            if i in dict.keys():
              number = dict[i]
              number+=1
              dict[i] = number
            else:
              dict[i] = 1
    return dict
def persent(addit_str):
    addit_str = get_count_char(addit_str)
    total = sum(addit_str.values())
    for key in addit_str:
       addit_str[key]/= total
       addit_str[key]*=100
       addit_str[key] = round(addit_str[key])
    return addit_str

main_str = """
Данное предложение будет разбиваться на отдельные слова.
В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(persent(main_str))
