
class DinosaurModeler:
    def __init__(self):
        self.possible_species = {
            "Ти-рекс": ["череп", "большие зубы", "массивные ноги"],
            "Велоцираптор": ["когти", "перья", "гибкость"],
            "Трицератопс": ["рога", "фрагменты черепа", "клюв"],
            "Брахиозавр": ["длинная шея", "огромные кости"],
            "Стегозавр": ["пластины", "шипы на хвосте"],
            "Анкилозавр": ["бронированный панцирь", "большая костяная булава"],
            "Диплодок": ["длинный хвост", "длинная шея", "четыре массивные ноги"]
        }

    def identify_species(self, fossils):
        if not fossils:
            return "❌ Недостаточно данных для определения вида динозавра."

        traits = [f.name.lower() for f in fossils]
        matched_species = None

        for species, required_traits in self.possible_species.items():
            if all(trait in traits for trait in required_traits):
                matched_species = species
                break

        return matched_species if matched_species else "🤔 Вид динозавра определить сложно."

    def reconstruct_dinosaur(self, fossils):
        species = self.identify_species(fossils)
        if species.startswith("❌") or species.startswith("🤔"):
            return species
        return f"✅ На основе ископаемых удалось реконструировать {species}!"

