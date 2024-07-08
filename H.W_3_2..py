#створюю список
my_list = [1, 2, 3, 4, 5]
print(my_list)
#робимо умову, але не більше 4 в даному випадку
if len(my_list) > 1:
#видаляємо останній елемент за допомогою pop
    last_element = my_list.pop()
#вставляємо елемент за індексом
    my_list.insert(0,last_element)
    print(my_list)