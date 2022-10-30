def get_count_char(main_str):
    dict = {}
    for i in main_str.lower():
        if i.isalpha()== True and  i in dict.keys()::
              number = dict[i]+1
              dict[i] = number
            else:
              dict[i] = 1
    return dict
def persent(main_str):
    main_str = get_count_char(main_str)
    total = sum(main_str.values())
    for key in main_str:
       main_str[key]= round(main_str[key] * 100 / total)
    return main_str

main_str = """
Данное предложение будет разбиваться на отдельные слова.
В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(persent(main_str))
