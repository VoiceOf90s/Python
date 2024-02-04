
class Tree:
    def __init__(self, type_tree: str, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :type_tree: Вид дерева
        :height: Высота

        Примеры:
        >>> Oak = Tree("Oak", 27.3)  # инициализация экземпляра
        """

        if not isinstance(type_tree, (str)):
            raise TypeError("Название растения должно быть типа str")
        self.type_tree = type_tree

        if not isinstance(height, (int, float)):
            raise TypeError("Допустимо значение типа int или float")
        if height <= 0:
            raise ValueError("Высота не может быть отрицательной")
        self.height = height

    def growth(self, growth_rate: float) -> None:
        """
        Функция, выставляющая заданную скорость роста.

        Примеры:
        >>> Oak = Tree("Oak", 9.11)
        >>> Oak.growth(1.1)
        """
        if not isinstance(growth_rate, (int, float)):
            raise TypeError("Допустимо значение типа int или float")
        if growth_rate < 0:
            raise ValueError("Скорость не может быть отрицательной")
        ...


    def get_info(self) -> str:
        """
        Функция, возвращающая вид растения

        :return: Возвращает название вида растения

        Примеры:
        >>> Oak = Tree("Oak", 9.11)
        >>> Oak.get_info()
        """
        ...

class Album:
    def __init__(self, title: str, author: str, tracks: int):
        """
        Инициализация объекта "Альбом".

        :title: Название альбома
        :author: Автор альбома
        :tracks: Количество комозиций

        Примеры:
        >>> album = Album("Deep Purple", "Machine Head", 7)
        """

        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        self.author = author

        if not isinstance(tracks, int):
            raise TypeError("Количество комозиций должно быть целым числом")
        if tracks <= 0:
            raise ValueError("Количество комозиций не может быть отрицательным")
        self.tracks = tracks

    def listen(self, tracks: int) -> None:
        """
        Функция, представляющая чтение книги.

        :pages: Количество страниц для чтения

        Примеры:
        >>> album = Album("Deep Purple", "Machine Head", 7)
        >>> album.listen(5)
        """
        ...

    def get_recording(self) -> str:
        """
        Функция, возвращающая описание альбома

        :return: Строка с описанием

        Примеры:
        >>> album = Album("Deep Purple", "Machine Head", 7)
        >>> album.get_recording()
        """
        ...


class Movie:
    def __init__(self, title: str, year: int, duration: float, director: str, screenwriter:str, main_role:str):
        """
        Инициализация объекта "Фильм".

        :title: Название фильма
        :year: Год издания
        :duration: Продолжительность фильма в минутах
        :director: Режиссер
        :screenwriter: Сценарист
        :main_role: Главная роль

        Примеры:
        >>> movie = Movie("Inception", 2010, 148, "Christopher Nolan", "Christopher Nolan", "Leonardo DiCaprio")
        """

        if not isinstance(title, str):
            raise TypeError("Название фильма должно вводиться строкой")
        self.title = title

        if not isinstance(year, int):
            raise TypeError("Год должен быть целым числом")
        self.year = year

        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        self.duration = duration

        if not isinstance(director, str):
            raise TypeError("Режиссер должен вводиться строкой")
        self.director = director

        if not isinstance(screenwriter, str):
            raise TypeError("Сценарист должен вводиться строкой")
        self.screenwriter = screenwriter

        if not isinstance(main_role, str):
            raise TypeError("Главная роль должна вводиться строкой")
        self.main_role = main_role

    def start_playing(self) -> None:
        """
        Функция, воспроизводящая фильм

        Примеры:
        >>> movie = Movie("Inception", 2010, 148, "Christopher Nolan", "Christopher Nolan", "Leonardo DiCaprio")
        >>> movie.start_playing()
        """
        ...

    def rewind(self) -> None:
        """
        Функция, перематывающая фильм

        Примеры:
        >>> movie = Movie("Inception", 2010, 148, "Christopher Nolan", "Christopher Nolan", "Leonardo DiCaprio")
        >>> movie.rewind()
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации