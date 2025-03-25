from models.dinosaurmodels import DinosaurModeler
from models.evolution import EvolutionResearch

class Researcher:
    def __init__(self, name, field):
        self.name = name
        self.field = field
        self.modeler = DinosaurModeler()
        self.evolution_research = EvolutionResearch()

    def analyze_excavation(self, excavation):
        fossils = excavation.found_fossils
        if not fossils:
            return "🚜 В этом месте ничего не найдено."

        dino_result = self.modeler.reconstruct_dinosaur(fossils)
        return f"🔎 Исследование формации {excavation.formation.name} ({excavation.formation.age} млн лет)\n{dino_result}"

    def study_evolution(self, dinosaurs, dino1_name, dino2_name):
        """Метод для исследования эволюции двух динозавров."""
        if dino1_name in dinosaurs and dino2_name in dinosaurs:
            dino1 = dinosaurs[dino1_name]
            dino2 = dinosaurs[dino2_name]
            return self.evolution_research.study_evolution(dino1, dino2, None)
        else:
            return "❌ Неверный ввод динозавров."

    def __str__(self):
        return f"🔬 {self.name} – специалист в области {self.field}"
