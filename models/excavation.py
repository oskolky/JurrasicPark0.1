
from models.fossil import Fossil
from models.formation import GeologicalFormation

class Excavation:
    def __init__(self, formation: GeologicalFormation):
        self.formation = formation
        self.found_fossils = []

    def dig(self, fossil_name, age_million_years):
        fossil = Fossil(fossil_name, age_million_years, self.formation.location)
        self.found_fossils.append(fossil)
        return f"🦴 Найдено ископаемое: {fossil}"

    def list_fossils(self):
        if not self.found_fossils:
            return "🚜 В этом месте пока ничего не найдено."
        return "\n".join(str(fossil) for fossil in self.found_fossils)

    def __str__(self):
        return f"⛏️ Раскопки в {self.formation.location}, геологическая формация: {self.formation.name}."

    def to_dict(self):

        return {
            "formation": self.formation.name,
            "found_fossils": list(self.found_fossils),  # Преобразуем set в список
        }

    @classmethod
    def start_excavation(cls, formations, excavations):
        """Метод для начала раскопок."""
        print("\nВыберите геологическую формацию:")
        for key, formation in formations.items():
            print(f"{key}. {formation.name} ({formation.age} млн лет)")

        formation_choice = input("Введите номер формации: ")
        if formation_choice in formations:
            formation = formations[formation_choice]

            excavation = cls(formation)
            excavations[formation.name] = excavation
            print(f"⛏️ Начаты раскопки в формации {formation.name}!")

            excavation.dig_fossils()
        else:
            print("❌ Ошибка: неверный выбор формации!")

    def dig_fossils(self):
        """Метод для добавления ископаемых в раскопки."""
        while True:
            fossil_name = input("Введите название ископаемого (или 'стоп' для завершения): ")
            if fossil_name.lower() == "стоп":
                break
            try:
                age = int(input("Введите возраст находки (млн лет): "))
                self.dig(fossil_name, age)
                print(f"✅ Найдено: {fossil_name} ({age} млн лет)")
            except ValueError:
                print("❌ Ошибка: введите числовое значение для возраста!")