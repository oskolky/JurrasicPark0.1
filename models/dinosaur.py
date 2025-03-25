class Dinosaur:
    def __init__(self, name, scientific_name, period):
        self.name = name
        self.scientific_name = scientific_name
        self.period = period

    def __str__(self):
        return f"🦖 {self.name} ({self.scientific_name}), период: {self.period}"

    @classmethod
    def add_dinosaur(cls, dinosaurs):
        """Method to add a new dinosaur to the dinosaurs collection."""
        print("\n=== 🦕 Добавление нового динозавра ===")

        # Collect user inputs for the new dinosaur
        name = input("Введите название динозавра: ").strip()
        latin_name = input("Введите латинское название: ").strip()
        period = input("Введите период (например, 'Юрский период'): ").strip()

        # Validate inputs
        if not name or not latin_name or not period:
            print("❌ Ошибка: все поля должны быть заполнены!")
            return None

        # Check if the dinosaur is already in the collection
        if name in dinosaurs:
            print("⚠️ Этот динозавр уже есть в базе!")
            return None

        # Create the new dinosaur and add it to the dictionary
        dinosaur = cls(name, latin_name, period)
        dinosaurs[name] = dinosaur
        print(f"✅ Динозавр {name} ({latin_name}) добавлен в список!")
        return dinosaur