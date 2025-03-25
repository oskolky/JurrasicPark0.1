
class GeologicalFormation:
    def __init__(self, name, age, rock_type, location):
        self.name = name
        self.age = age
        self.rock_type = rock_type
        self.location = location

    def __str__(self):
        return f"Формация {self.name} ({self.age} млн лет) – {self.rock_type}, {self.location}"

    @classmethod
    def add_formation(cls, formations):
        """Метод для добавления новой геологической формации с авто-генерацией ключа."""

        # Генерация нового ключа (цифры)
        if formations:
            # Находим максимальный номер из текущих ключей
            max_key = max([int(key) for key in formations.keys() if key.isdigit()])
            new_key = str(max_key + 1)  # Новый ключ будет на 1 больше
        else:
            # Если формации пустые, начинаем с 1
            new_key = '1'

        # Ввод данных для новой формации
        name = input("Введите название формации: ")
        age = int(input("Введите возраст формации (млн лет): "))
        rock_type = input("Введите тип горных пород: ")
        location = input("Введите место расположения: ")

        # Создаем новую геологическую формацию
        new_formation = cls(name, age, rock_type, location)

        # Добавляем новую формацию в коллекцию
        formations[new_key] = new_formation
        print(f"✅ Новая формация '{name}' добавлена с ключом {new_key}.")

        return formations