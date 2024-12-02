users = [
    {
        'username': 'NurlanBEK',
        'password': '123456789',
        'role': 'user',
        'cart': [],
    },
    {
        'username': 'uyutikk',
        'password': '1',
        'role': 'admin',
    }
]

books = [
    {
        'title': 'Грокаем алгоритмы. Иллюстрированное пособие для программистов и любопытствующих',
        'author': 'Бхаргава Адитья',
        'price': 700,
        'rating': 4.4,
        'year': 2024,
        'genre': 'Программирование',
        'annotation': 'Принято считать, что программирование – это очень сложно. Особенно если раз за разом наступать на одни и те же грабли, пытаться сделать по-своему то, что уже и так было придумано до нас. Ведь практически для любой задачи есть готовый алгоритм решения, осталось только найти его и правильно использовать.'
    },
    {
        'title': 'True believer. Взлёт и падение Стэна Ли',
        'author': 'Абрахам Рисмен',
        'price': 350,
        'rating': 4.7,
        'year': 2021,
        'genre': 'Биография',
        'annotation': 'Всё для того чтобы добиться успеха'
    },
    {
        'title': 'Самый богатый человек в Вавилоне',
        'author': 'Джордж Самюэль Клейсон',
        'price': 300,
        'rating': 4.8,
        'year': 1926,
        'genre': 'Личные финансы',
        'annotation': 'Самый богатый человек в Вавилоне — книга американского писателя Джорджа Самюэля Клейсона, впервые изданная в 1926 году и содержащая советы по ведению личных финансов, изложенные в виде занимательных рассказов-притч о событиях, происходивших более четырёх тысяч лет назад в древнем Вавилоне.'
    },
    {
        'title': 'Искусство войны',
        'author': 'Сунь-цзы',
        'price': 325,
        'rating': 4.9,
        'year': 1972,
        'genre': 'Трактат',
        'annotation': 'Древнекитайский трактат «Искусство войны» содержит тринадцать глав, каждая из которых посвящена отдельной стороне ведения успешной битвы. Его автором принято считать стратега и мыслителя Сунь-цзы. Писатель ратует за победу над войском противника без сражения и людских потерь.'
    },
    {
        'title': 'Продавец обуви. История компании NIKE',
        'author': 'Фил Найт',
        'price': 500,
        'rating': 4.7,
        'year': 2016,
        'genre': 'Биография',
        'annotation': 'Когда-то молодой, неудержимый, только что окончивший бизнес-школу Фил Найт занял у отца 50 долларов, чтобы открыть собственную компанию с одной простой миссией: импортировать недорогую и высококачественную обувь из Японии.'
    },
    {
        'title': 'Классика Marvel. Человек-паук',
        'author': 'Стэн Ли',
        'price': 1100,
        'rating': 5.0,
        'year': 2021,
        'genre': 'Фантастика',
        'annotation': 'Легендарное первое появление Человека-Паука, "Удивительное Фэнтези" #15. Первые появления Хамелеона, Стервятника, Доктора Осьминога, Ящера, Песочного Человека и многих других культовых злодеев.'
    },
    {
        'title': 'Классика Marvel. Железный человек',
        'author': 'Стэн Ли',
        'price': 1500,
        'rating': 4.9,
        'year': 2020,
        'genre': 'Фантастика',
        'annotation': 'Первое появление Железного Человека! Промышленник-оружейник сам становится живым оружием, мифы Холодной войны воплощаются в героев и злодеев, которым однажды удастся захватить киноэкраны по обе стороны Атлантики. Сборник комиксов, в которых впервые звучит грохочущая поступь Железного Человека.'
    },
    {
        'title': 'Король Лир',
        'author': 'Уильям Шекспир',
        'price': 790,
        'rating': 4.8,
        'year': 1606,
        'genre': 'Трагедия',
        'annotation': 'Древняя Британия. На Склоне лет Король Лир решает удалиться от дел и разделить государство между тремя взрослыми дочерьми - Гонерильей, Реганой и Корделией - в обмен на их признание в любви. Ослепленный льстивыми речами старших наследниц, Лир поспешно отрекается от младшей, искренней и преданной ему Корделии. В результате на сцене торжествуют ложь и предательство, а бедный король изгнан и объявлен безумцем. Сердце Лира разбито, он жаждет справедливости и отмщения. Но плата за ошибки непомерно высока...'
    },
    {
        'title': 'Отелло',
        'author': 'Уильям Шекспир',
        'price': 980,
        'rating': 4.9,
        'year': 1603,
        'genre': 'Трагедия',
        'annotation': 'История трагической любви дочери венецианского сенатора Дездемоны и мавра Отелло, состоящего у Венеции на военной службе. Являясь заслуженным полководцем, Отелло, в чине наместника, направлен на остров Кипр, дабы отразить нападение турецкого флота. На остров же приезжает и его молодая жена Дездемона.'
    }
]

def show_books():
    print("\nСписок доступных книг:")
    for book in books:
        print(f"Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Жанр: {book['genre']}, Цена: {book['price']}, Рейтинг: {book['rating']}")

def view_book_annotation():
    title = input("\nВведите название книги для просмотра аннотации: ")
    book = next((b for b in books if b['title'].lower() == title.lower()), None)
    if book:
        print("\nПодробная информация о книге:")
        print(f"Название: {book['title']}")
        print(f"Аннотация: {book['annotation']}")
    else:
        print("Книга не найдена.")

def add_to_cart(user, book_title):
    book = next((b for b in books if b['title'].lower() == book_title.lower()), None)
    if book:
        user['cart'].append(book)
        print(f"Книга '{book_title}' добавлена в корзину.")
    else:
        print("Книга не найдена.")

def view_cart(user):
    print("\nВаша корзина:")
    if user['cart']:
        total_price = 0
        for book in user['cart']:
            print(f"Название: {book['title']}, Цена: {book['price']}")
            total_price += book['price']
        print(f"Общая стоимость: {total_price:.2f}")
    else:
        print("Корзина пуста.")

def filter_books():
    filtered_books = books[:]
    while True:
        print("\nВыберите критерий сортировки или фильтрации:")
        print("1. Цена (по возрастанию)")
        print("2. Цена (по убыванию)")
        print("3. Рейтинг (по возрастанию)")
        print("4. Рейтинг (по убыванию)")
        print("5. Название (от А до Я)")
        print("6. Название (от Я до А)")
        print("7. Фильтровать по году (введите диапазон)")
        print("8. Фильтровать по жанру")
        print("9. Вернуться в главное меню")

        choice = input("Ваш выбор: ")
        if choice == "1":
            filtered_books = sorted(filtered_books, key=lambda x: x['price'])
        elif choice == "2":
            filtered_books = sorted(filtered_books, key=lambda x: x['price'], reverse=True)
        elif choice == "3":
            filtered_books = sorted(filtered_books, key=lambda x: x['rating'])
        elif choice == "4":
            filtered_books = sorted(filtered_books, key=lambda x: x['rating'], reverse=True)
        elif choice == "5":
            filtered_books = sorted(filtered_books, key=lambda x: x['title'])
        elif choice == "6":
            filtered_books = sorted(filtered_books, key=lambda x: x['title'], reverse=True)
        elif choice == "7":
            try:
                start_year = int(input("Введите начальный год (от 1700): "))
                if start_year < 1700 or start_year > 2024:
                    raise ValueError("Начальный год должен быть в диапазоне от 1700 до 2024.")
                
                end_year = int(input("Введите конечный год (до 2024): "))
                if end_year < 1700 or end_year > 2024:
                    raise ValueError("Конечный год должен быть в диапазоне от 1700 до 2024.")
                
                if end_year < start_year:
                    raise ValueError("Конечный год не может быть меньше начального года.")
                
                filtered_books = list(filter(lambda x: start_year <= x['year'] <= end_year, filtered_books))
            except ValueError as e:
                print(f"Ошибка: {e}. Попробуйте снова.")
                continue
        elif choice == "8":
            genre = input("Введите жанр для фильтрации: ").lower()
            filtered_books = [b for b in filtered_books if b['genre'].lower() == genre]
        elif choice == "9":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
            continue

        print("\nРезультаты сортировки и фильтрации:")
        if filtered_books:
            for book in filtered_books:
                print(f"Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Жанр: {book['genre']}, Цена: {book['price']}, Рейтинг: {book['rating']}")
        else:
            print("Нет книг, соответствующих заданным критериям.")

def add_book():
    global books
    title = input("Введите название книги: ")
    author = input("Введите имя автора: ")
    price = float(input("Введите цену книги: "))
    rating = float(input("Введите рейтинг книги: "))
    year = int(input("Введите год написания книги: "))
    genre = input("Введите жанр книги: ")
    annotation = input("Введите аннотацию к книге: ")

    new_book = {
        'title': title,
        'author': author,
        'price': price,
        'rating': rating,
        'year': year,
        'genre': genre,
        'annotation': annotation
    }
    books.append(new_book)
    print(f"Книга '{title}' добавлена в каталог.")

def delete_book():
    global books
    title = input("Введите название книги, которую хотите удалить: ")
    books = [book for book in books if book['title'].lower() != title.lower()]
    print(f"Книга '{title}' удалена из каталога.")

def edit_book():
    global books
    title = input("Введите название книги, которую хотите изменить: ")
    book = next((b for b in books if b['title'].lower() == title.lower()), None)
    if book:
        new_title = input(f"Введите новое название (текущее: {book['title']}): ")
        new_author = input(f"Введите нового автора (текущий: {book['author']}): ")
        new_price = float(input(f"Введите новую цену (текущая: {book['price']}): "))
        new_rating = float(input(f"Введите новый рейтинг (текущий: {book['rating']}): "))
        new_year = int(input(f"Введите новый год написания (текущий: {book['year']}): "))
        new_genre = input(f"Введите новый жанр (текущий: {book['genre']}): ")
        new_annotation = input(f"Введите новую аннотацию (текущая: {book['annotation']}): ")

        book.update({
            'title': new_title,
            'author': new_author,
            'price': new_price,
            'rating': new_rating,
            'year': new_year,
            'genre': new_genre,
            'annotation': new_annotation
        })
        print(f"Информация о книге '{title}' обновлена.")
    else:
        print("Книга не найдена.")

def login():
    username = input("Логин: ")
    password = input("Пароль: ")

    user = next((u for u in users if u['username'] == username and u['password'] == password), None)
    if user:
        print(f"Добро пожаловать, {username}!")
        return user
    else:
        print("Неверный логин или пароль.")
        return None

def user_menu(user):
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть доступные книги")
        print("2. Просмотреть аннотацию книги")
        print("3. Добавить книгу в корзину")
        print("4. Просмотреть корзину")
        print("5. Фильтровать и сортировать книги")
        print("6. Выйти")

        choice = input("Ваш выбор: ")
        if choice == "1":
            show_books()
        elif choice == "2":
            view_book_annotation()
        elif choice == "3":
            book_title = input("Введите название книги: ")
            add_to_cart(user, book_title)
        elif choice == "4":
            view_cart(user)
        elif choice == "5":
            filter_books()
        elif choice == "6":
            print("До свидания!")
            break

def admin_menu():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Изменить информацию о книге")
        print("4. Просмотреть все книги")
        print("5. Фильтровать и сортировать книги")
        print("6. Выйти")

        choice = input("Ваш выбор: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            edit_book()
        elif choice == "4":
            show_books()
        elif choice == "5":
            filter_books()
        elif choice == "6":
            print("До свидания!")
            break

def main():
    user = login()
    if user:
        if user['role'] == 'admin':
            admin_menu()
        else:
            user_menu(user)

if __name__ == "__main__":
    main()
