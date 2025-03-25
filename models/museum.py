class MuseumExhibition:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.exhibits = []

    def organize_exhibition(self, excavation, researcher):
        if not excavation.found_fossils:
            return f"🚫 Невозможно организовать выставку: в {excavation.formation.name} ничего не найдено."

        reconstructed_dino = researcher.modeler.reconstruct_dinosaur(excavation.found_fossils)
        exhibit = {
            "formation": excavation.formation.name,
            "age": excavation.formation.age,
            "reconstruction": reconstructed_dino,
            "researcher": researcher.name  # Добавляем имя ученого
        }
        self.exhibits.append(exhibit)

        return f"🏛️ Организована выставка в {self.location}!\n🌍 Формация: {exhibit['formation']}\n🦖 {exhibit['reconstruction']}\n👨‍🔬 Ученый: {exhibit['researcher']}"

    def list_exhibitions(self):
        if not self.exhibits:
            return "🏛️ В музее пока нет выставок."

        return "\n\n".join(
            f"🌍 {exhibit['formation']}\n🦖 {exhibit['reconstruction']}\n👨‍🔬 Ученый: {exhibit['researcher']}"
            for exhibit in self.exhibits
        )

    def choose_exhibition_and_organize(self, researchers, excavations):
        if not excavations:
            print("🚫 Нет раскопок для организации выставки.")
            return

        print("\nВыберите ученого для организации выставки:")
        # Выводим исследователей с их номерами
        for key, researcher in researchers.items():
            print(f"{key}. {researcher.name} - {researcher.field}")

        try:
            # Запрашиваем выбор ученого по номеру (ключу)
            researcher_choice = input("Введите номер ученого: ")
            if researcher_choice in researchers:
                selected_researcher = researchers[researcher_choice]
                print(f"Выбран ученый: {selected_researcher.name}, область: {selected_researcher.field}")
            else:
                print("❌ Неверный выбор ученого.")
                return
        except ValueError:
            print("❌ Ошибка: введите правильный номер.")
            return

        print("\nВыберите раскопки для выставки:")
        excavation_list = list(excavations.values())
        for i, excavation in enumerate(excavation_list, start=1):
            print(f"{i}. {excavation.formation.name} ({excavation.formation.age} млн лет)")

        try:
            excavation_choice = int(input("Введите номер раскопок: ")) - 1
            if 0 <= excavation_choice < len(excavation_list):
                excavation = excavation_list[excavation_choice]
                print("\n" + self.organize_exhibition(excavation, selected_researcher))
            else:
                print("❌ Неверный выбор раскопок.")
        except ValueError:
            print("❌ Ошибка: введите числовой номер.")

    def __str__(self):
        return f"🏛️ Музей {self.name} в {self.location}"
