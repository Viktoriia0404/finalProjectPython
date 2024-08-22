import myfunc

while True:
    query = input('Вывод самых популярных запросов - top\n'
                  'Поиск по категории - 1\n'
                  'Поиск по году выпуска  - 2\n'
                  'Поиск по имени или фамилии актера - 3\n'
                  'Поиск по названию - 4\n'
                  'Поиск по ключ.слову - 5 \n'
                  'Выход - 0\n'
                  'Сделайте ваш выбор: ').lower()

    if query == '0':
        break
    elif query == 'top':
        myfunc.get_top_result()
    elif query == '1':
        category = input('Введите категорию: ')
        myfunc.search_category(category)
    elif query == '2':
        try:
            year = int(input('Введите год: '))
            myfunc.search_year(year)
        except ValueError:
            print('Год должен быть числовым значением!')
    elif query == '3':
        actor = input('Введите имя или фамилию: ')
        myfunc.search_actor(actor)
    elif query == '4':
        title = input('Введите название фильма: ')
        myfunc.search_title(title)
    elif query == '5':
        keyword = input('Введите категорию: ')
        myfunc.get_result_keyword(keyword)
