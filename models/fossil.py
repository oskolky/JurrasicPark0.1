class Fossil:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def __str__(self):
        return f"{self.name}, {self.age}, {self.location}"

    def to_dict(self):
        """Метод для сериализации объекта в словарь"""
        return {
            "name": self.name,
            "age": self.age,
            "location": self.location
        }