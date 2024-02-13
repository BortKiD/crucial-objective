class BaseRace:
    """ Базовый класс гонок """
    def __init__(self, name: str, distance: float):
        """
        Создание и подготовка к работе объекта "Гонка"

        :param name: Название заезда
        :param distance: Дистанция заезда

        Примеры:
        >>> race = BaseRace('Race', 100.101)
        """
        self._name = name
        self.distance = distance
        self._participants = []

    def __str__(self) -> str:
        return f"Заезд {self.name}. Дистанция {self.distance}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, distance={self.distance!r}"

    def add_participant(self, participant: str) -> None:
        """
        Добавление участника заезда

        :param participant: Имя участника

        Примеры:
        >>> race = BaseRace('Race', 100.101)
        >>> race.add_participant('Schumacher')
        """
        self._participants.append(participant)

    def get_description(self) -> str:
        """
        Вывод описания заезда

        :return: Описание заезда

        Примеры:
        >>> race = BaseRace('Race', 100.101)
        >>> description = race.get_description()
        """
        return f"{self.name} гонка с дистанцией {self.distance} км"

    @property
    def name(self) -> str:
        """
        Возвращает название заезда

        :return: Название заезда

        Примеры:
        >>> race = BaseRace('Race', 100.101)
        >>> race_name = race.name
        """
        return self._name

    @property
    def distance(self) -> float:
        """
        Возвращает дистанцию заезда

        :return: Дистанция заезда

        Примеры:
        >>> race = BaseRace('Race', 100.101)
        >>> race_distance = race.distance
        """
        return self._distance

    @distance.setter
    def distance(self, distance) -> None:
        """
        Устанавливает дистанцию заезда

        :raise TypeError: Если вводимый аргумент не является числом с плавающей точкой,
                          то возвращет ошибку
        :raise ValueError: Если вводимая дистанция не является положительным числом,
                           то возвращает ошибку

        Примеры:
        >>> race = BaseRace('Race', 100.101)
        >>> race.distance = 111
        """
        if not isinstance(distance, float):
            raise TypeError('Расстояние должно быть типа float')
        if distance <= 0:
            raise ValueError('Расстояние должно быть положительным')
        self._distance = distance

    @property
    def participants(self) -> list:
        """
        Возвращает список участников заезда

        :return: Список участников

        Примеры:
        >>> race = BaseRace('Race', 100.101)
        >>> race.add_participant('Schumacher')
        >>> race_participants = race.participants
        """
        return self._participants


class LapRace(BaseRace):
    """ Дочерний класс кольцевых гонок """
    def __init__(self, name: str, distance: float, laps: int):
        """
        Создание и подготовка к работе объекта "Кольцевая Гонка"

        :param name: Название заезда
        :param distance: Дистанция заезда
        :param laps: Количество кругов в заезде

        Примеры:
        >>> race = LapRace('LapRace', 100.101, 2)
        """
        super().__init__(name, distance)
        self._laps = laps

    def __str__(self):
        return f"Заезд {self.name}. Дистанция {self.distance}. Круги {self._laps})"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, distance={self.distance!r}, laps={self._laps!r})"

    def calculate_lap_distance(self) -> float:
        """
        Функция для подсчета дистанции одного круга

        :return: Дистанция одного круга

        Примеры:
        >>> race = LapRace('LapRace', 100.101, 2)
        >>> lap_distance = race.calculate_lap_distance()
        """
        return round(self.distance / self.laps, 3)

    def get_description(self):
        """
        Вывод описания заезда

        :return: Описание заезда

        Примеры:
        >>> race = LapRace('LapRace', 100.101, 2)
        >>> description = race.get_description()
        """
        lap_distance = self.calculate_lap_distance()
        return f"{self.name} гонка с {self.laps} кругами и общим расстоянием {self.distance:.3f} км. " \
               f"Дистанция одного круга занимает {lap_distance:.3f}"

    @property
    def laps(self) -> float:
        """
        Возвращает количество кругов

        :return: Количество кругов
        """

        return self._laps

    @laps.setter
    def laps(self, laps):
        """
        Устанавливает количество кругов

        :raise TypeError: Если вводимый аргумент не является целым числом,
                          то возвращет ошибку
        :raise ValueError: Если вводимое количество кругов не является положительным числом,
                           то возвращает ошибку

        Примеры:
        >>> race = BaseRace('Race', 100.101)
        >>> race.distance = 111
        """
        if not isinstance(laps, int):
            raise TypeError('Distance must be float')
        if laps <= 0:
            raise ValueError('Distance must be positive')
        self._laps = laps


if __name__ == "__main__":
    # Write your solution here
    pass
