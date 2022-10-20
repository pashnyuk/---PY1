src = not False and True or False and not True

#по приоритету логический оператор not идет первее среди имеющихся
result = (True and True) or (False and False) #при использовании оператора and выбираем последнее истинное и первое ложное
result = True or False #находим истинное значение
result = True

print(src == result)
