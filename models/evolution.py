import random
from models.dinosaur import Dinosaur

class EvolutionResearch:
    def __init__(self):
        self.traits_db = {
            "Археоптерикс": ["перья", "лёгкие кости", "хищник"],
            "Велоцираптор": ["перья", "гибкость", "хищник"],
            "Ти-рекс": ["огромные челюсти", "мощные ноги", "хищник"],
            "Трицератопс": ["рогатая голова", "клюв", "травоядный"],
            "Брахиозавр": ["длинная шея", "травоядный", "огромный рост"],
            "Игуанодон": ["клюв", "травоядный", "гибкие конечности"],
            "Пситтакозавр": ["клюв", "маленький размер", "травоядный"],
            "Дейноних": ["перья", "сильные когти", "хищник"]
        }

        self.ancestor_map = {
            "Археоптерикс": "Велоцираптор",
            "Велоцираптор": "Ти-рекс",
            "Пситтакозавр": "Трицератопс",
            "Игуанадон": "Брахиозавр",
            "Дейноних": "Велоцираптор"
        }

    def study_evolution(self, dinosaur1: Dinosaur, dinosaur2: Dinosaur):
        if dinosaur1.period == dinosaur2.period:
            return f"❌ {dinosaur1.name} и {dinosaur2.name} жили в одно время, эволюционная связь маловероятна."

        evidence = []
        shared_traits = self.compare_traits(dinosaur1, dinosaur2)
        if shared_traits:
            evidence.append(f"🔍 Общие черты: {', '.join(shared_traits)}.")
        if self.is_potential_ancestor(dinosaur1, dinosaur2):
            evidence.append(f"🧬 Генетический анализ показывает возможную родственную линию.")
        if random.choice([True, False, False]):
            evidence.append("🔬 Новые исследования показывают возможное сходство в структуре костей.")

        if evidence:
            return f"✅ {dinosaur1.name} ({dinosaur1.period}) мог эволюционировать в {dinosaur2.name} ({dinosaur2.period}). Подтверждения:\n" + "\n".join(evidence)
        else:
            return f"⚠️ Связь между {dinosaur1.name} и {dinosaur2.name} не найдена."

    def compare_traits(self, dinosaur1: Dinosaur, dinosaur2: Dinosaur):
        traits1 = self.traits_db.get(dinosaur1.name, [])
        traits2 = self.traits_db.get(dinosaur2.name, [])
        return list(set(traits1) & set(traits2))

    def is_potential_ancestor(self, dinosaur1: Dinosaur, dinosaur2: Dinosaur):
        return self.ancestor_map.get(dinosaur1.name) == dinosaur2.name
