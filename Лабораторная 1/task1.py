import doctest


class Book:
    def __init__(self, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param name:  Название книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book('Book', 100)
        """
        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError('Количество страниц в книге должен быть типа int')
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages

    def rename_book(self, name: str) -> None:
        """
        Функция которая меняет название книги

        :param name: Новое название книги

        Примеры:
        >>> book = Book('Book', 100)
        >>> book.rename_book('Hitchhiker')
        """
        ...

    def publish_book(self) -> int:
        """
        Функция которая публикует книгу

        :return: Идентификатор новой публикации

        Примеры:
        >>> book = Book('Book', 100)
        >>> publication_id = book.publish_book()
        """
        ...


class Shape:
    def __init__(self, name: str, color: str, dimension: int):
        """
        Создание и подготовка к работе объекта "Фигура"

        :param name:  Название фигуры
        :param color: Цвет фигуры
        :param dimension: Размерность фигуры

        Примеры:
        >>> circle = Shape('Circle', 'Blue', 2)
        """
        if not isinstance(name, str):
            raise TypeError('Название фигуры должно быть типа str')
        self.name = name

        if not isinstance(color, str):
            raise TypeError('Цвет фигуры должен быть типа str')
        self.color = color

        if not isinstance(dimension, int):
            raise TypeError('Размерность фигуры должна быть типа int')
        if dimension <= 0:
            raise ValueError("Размерность фигуры должна быть положительным числом")
        self.dimension = dimension

    def change_color(self, color: str) -> None:
        """
        Функция которая меняет цвет фигуры

        :param color: Новый цвет фигуры

        Примеры:
        >>> circle = Shape('Circle', 'Blue', 2)
        >>> circle.change_color('Red')
        """
        ...

    def get_name(self) -> str:
        """
        Функция которая возвращает название фигуры

        :return: Название фигуры

        Примеры:
        >>> circle = Shape('Circle', 'Blue', 2)
        >>> circle.get_name()
        """
        ...


class Airplane:
    def __init__(self, model: str, weight: int):
        """
        Создание и подготовка к работе объекта "Самолет"

        :param model: Модель самолета
        :param weight: Вес самолета, кг
        :param speed: Скорость самолета

        Примеры:
        >>> plane = Airplane('Heinkel', 4000)
        """
        if not isinstance(model, str):
            raise TypeError('Модель самолета должна быть типа str')
        self.model = model

        if not isinstance(weight, int):
            raise TypeError('Вес самолета должен быть типа int')
        if weight <= 0:
            raise ValueError("Вес самолета должен быть положительным числом")
        self.weight = weight

        self.speed = 0

    def load_cargo(self, weight: int) -> None:
        """
        Функция которая добавляет груз увеличивает вес

        :param weight: Число на которое увеличивается вес самолета
        :raise ValueError: Если число на которое нужно увеличить вес самолета меньше нуля
                           то возвращаем ошибку

        Примеры:
        >>> plane = Airplane('Heinkel', 4000)
        >>> plane.load_cargo(100)
        """
        if not isinstance(weight, int):
            raise TypeError('Число на которое увеличивается вес самолета должно быть типа int')
        if weight <= 0:
            raise ValueError("Число на которое увеличивается вес самолета должно быть положительным числом")
        ...

    def accelerate(self, speed: int) -> int:
        """
        Функция которая увеличивает скорость самолета на заданное число

        :param speed: Число на которое нужно увеличить скорость самолета
        :raise ValueError: Если число на которое нужно увеличить скорость самолета меньше нуля
                           то возвращаем ошибку

        :return: Новая скорость самолета

        Примеры:
        >>> plane = Airplane('Heinkel', 4000)
        >>> plane.accelerate(600)
        """
        if not isinstance(speed, int):
            raise TypeError('Число на которое нужно увеличить скорость самолета должно быть типа int')
        if speed <= 0:
            raise ValueError("Число на которое нужно увеличить скорость самолета должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass





