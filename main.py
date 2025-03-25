from models.formation import GeologicalFormation
from models.researcher import Researcher
from models.dinosaur import Dinosaur
from models.excavation import Excavation
from models.museum import MuseumExhibition
import storage

def main():
    museum, excavations, dinosaurs, researchers, formations = storage.load_state()

    if not museum:
        museum = MuseumExhibition("Национальный музей природы", "Москва")


    if not researchers:
        researchers = {
            "1": Researcher("Иванов И.И.", "Палеонтолог"),
            "2":Researcher("Петров П.П.", "Эволюционист")
        }

    if not formations:
        formations = {
            "1": GeologicalFormation("Ляонин", 125, "Сланец", "Китай"),
            "2": GeologicalFormation("Хелл-Крик", 66, "Осадочные породы", "Монтана, США"),
            "3": GeologicalFormation("Джадохта", 75, "Песчаник", "Монголия"),
        }

    if not excavations:
        excavations = {}

    if not dinosaurs:
        dinosaurs = {
            "Археоптерикс": Dinosaur("Археоптерикс", "Archaeopteryx", "Юрский период"),
            "Велоцираптор": Dinosaur("Велоцираптор", "Velociraptor", "Меловой период"),
            "Ти-рекс": Dinosaur("Ти-рекс", "Tyrannosaurus Rex", "Меловой период"),
            "Трицератопс": Dinosaur("Трицератопс", "Triceratops", "Меловой период"),
        }

    while True:
        print("\n=== 🦖 Меню программы 'Юрский Парк' ===")
        print("1. Провести раскопки")
        print("2. Вывести список найденных ископаемых")
        print("3. Исследовать эволюцию динозавров")
        print("4. Добавить нового динозавра")
        print("5. Просмотреть список известных динозавров")
        print("6. Организовать музейную выставку")
        print("7. Показать список выставок")
        print("8. Добавить новую геологическую формацию")
        print("9. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            Excavation.start_excavation(formations, excavations)

        elif choice == "2":
            if not excavations:
                print("🚜 Раскопок пока не было.")
            else:
                for excavation in excavations.values():
                    print(f"\n🔎 {excavation}")
                    print(excavation.list_fossils())


        elif choice == "3":
            print("\nВыберите динозавров для исследования эволюции:")
            for name in dinosaurs.keys():
                print(f"- {name}")
            dino1_name = input("Введите первый вид динозавра: ")
            dino2_name = input("Введите второй вид динозавра: ")
            result = researchers.study_evolution(dinosaurs, dino1_name, dino2_name)
            print(result)

        elif choice == "4":
            Dinosaur.add_dinosaur(dinosaurs)

        elif choice == "5":
            print("\n📜 Список известных динозавров:")
            for dino in dinosaurs.values():
                print(f"🦖 {dino.name} ({dino.scientific_name}) – {dino.period}")

        elif choice == "6":
           museum.choose_exhibition_and_organize(researchers, excavations)

        elif choice == "7":
            print("\n📜 Текущие выставки в музее:")
            print(museum.list_exhibitions())


        elif choice == "8":
            formations = GeologicalFormation.add_formation(formations)


        elif choice == "9":
            storage.save_state(museum, excavations, dinosaurs, researchers, formations)  # Сохраняем перед выходом
            print("🚪 Выход из программы...")
            break

        else:
            print("❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
