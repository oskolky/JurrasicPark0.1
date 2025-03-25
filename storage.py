import json
import os
from models.museum import MuseumExhibition
from models.excavation import Excavation
from models.formation import GeologicalFormation
from models.dinosaur import Dinosaur
from models.researcher import Researcher
from models.fossil import Fossil

SAVE_FILE = "save_data.json"

def save_state(museum, excavations, dinosaurs, researchers, formations):
    data = {
        "museum": {
            "name": museum.name,
            "location": museum.location,
            "exhibits": museum.exhibits,
        },
        "excavations": {
            name: {
                "formation": excavation.formation.name,
                "found_fossils": [fossil.to_dict() for fossil in excavation.found_fossils]  # Преобразуем Fossil в dict
            }
            for name, excavation in excavations.items()
        },
        "dinosaurs": {
            name: {"scientific_name": dino.scientific_name, "period": dino.period}
            for name, dino in dinosaurs.items()
        },
        "researchers": {
            name: {
                "name": researcher.name,
                "field": researcher.field,
            }
            for name, researcher in researchers.items()
        },
        "formations": {
            name: {
                "name": formation.name,
                "age": formation.age,
                "rock_type": formation.rock_type,
                "location": formation.location
            }
            for name, formation in formations.items()
        }
    }

    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("💾 Данные успешно сохранены!")

def load_state():
    """Загружает данные из JSON-файла."""
    if not os.path.exists(SAVE_FILE):
        return None, {}, {}, None, {}

    with open(SAVE_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Загружаем музей
    museum = MuseumExhibition(data["museum"]["name"], data["museum"]["location"])
    museum.exhibits = data["museum"]["exhibits"]

    # Загружаем формации
    formations = {
        key: GeologicalFormation( info["name"], info["age"], info["rock_type"], info["location"])
        for key, info in data["formations"].items()
    }

    # Загружаем раскопки
    excavations = {
        name: Excavation(GeologicalFormation(
            excavation["formation"], 0, "", ""))
        for name, excavation in data["excavations"].items()
    }

    # Восстановление found_fossils как объектов типа Fossil
    for name, excavation in excavations.items():
        excavation.found_fossils = {Fossil(fossil["name"], fossil["age"], fossil["location"]) for fossil in
                                    data["excavations"][name]["found_fossils"]}

    # Загружаем динозавров
    dinosaurs = {
        name: Dinosaur(name, info["scientific_name"], info["period"])
        for name, info in data["dinosaurs"].items()
    }

    formations = {
        key: GeologicalFormation(info["name"], info["age"], info["rock_type"], info["location"])
        for key, info in data["formations"].items()
    }

    # Загружаем исследователя
    researchers = {
        key: Researcher(info["name"], info["field"])
        for key, info in data ["researchers"].items()
    }

    print("📂 Данные загружены!")
    return museum, excavations, dinosaurs, researchers, formations
