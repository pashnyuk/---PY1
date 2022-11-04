def get_count_char(str_):
    str_ = "".join(str_.lower().split())  # Привоим строку к нижнему регистру и объединяем
    char_dict = {}

    for el in str_:
        if el.isalpha():
            if el in char_dict:
                char_dict[el] += 1
            else:
                char_dict[el] = 1
    return char_dict


def get_percent_char(dict_):
    number = sum(dict_.values())
    for i in dict_:
        dict_[i] = round(dict_.get(i) * 100 / number, 1)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_percent_char(get_count_char(main_str)))
