import unittest
from unittest.mock import patch
from models.dinosaur import Dinosaur
from models.dinosaurmodels import DinosaurModeler
from models.excavation import Excavation
from models.formation import GeologicalFormation
from models.researcher import Researcher
from models.evolution import EvolutionResearch

class TestDinosaur(unittest.TestCase):
    def setUp(self):
        self.dinosaurs = {}
        self.dinosaur = Dinosaur("Тираннозавр", "Tyrannosaurus rex", "Меловой период")

    def test_dinosaur_creation(self):
        self.assertEqual(self.dinosaur.name, "Тираннозавр")
        self.assertEqual(self.dinosaur.scientific_name, "Tyrannosaurus rex")
        self.assertEqual(self.dinosaur.period, "Меловой период")

    def test_dinosaur_string_representation(self):
        expected_string = "🦖 Тираннозавр (Tyrannosaurus rex), период: Меловой период"
        self.assertEqual(str(self.dinosaur), expected_string)

    @patch('builtins.input', side_effect=["Трицератопс", "Triceratops horridus", "Меловой период"])
    @patch('builtins.print')  # Мокируем print
    def test_add_dinosaur_success(self, mock_print, mock_input):
        Dinosaur.add_dinosaur(self.dinosaurs)
        self.assertIn("Трицератопс", self.dinosaurs)

    @patch('builtins.input', side_effect=["Тираннозавр", "Tyrannosaurus rex", "Меловой период"])
    @patch('builtins.print')  # Мокируем print
    def test_add_dinosaur_duplicate(self, mock_print, mock_input):
        self.dinosaurs["Тираннозавр"] = self.dinosaur
        Dinosaur.add_dinosaur(self.dinosaurs)
        self.assertEqual(len(self.dinosaurs), 1)

    @patch('builtins.input', side_effect=["", "", ""])
    @patch('builtins.print')  # Мокируем print
    def test_add_dinosaur_with_missing_fields(self, mock_print, mock_input):
        original_count = len(self.dinosaurs)
        Dinosaur.add_dinosaur(self.dinosaurs)
        self.assertEqual(len(self.dinosaurs), original_count)

class TestDinosaurModeler(unittest.TestCase):
    def setUp(self):
        self.modeler = DinosaurModeler()

    def test_identify_species_success(self):
        fossils = [
            type("Fossil", (), {"name": "рога"}),
            type("Fossil", (), {"name": "фрагменты черепа"}),
            type("Fossil", (), {"name": "клюв"})
        ]
        result = self.modeler.identify_species(fossils)
        self.assertEqual(result, "Трицератопс")

    def test_identify_species_not_enough_data(self):
        fossils = []
        result = self.modeler.identify_species(fossils)
        self.assertEqual(result, "❌ Недостаточно данных для определения вида динозавра.")

    def test_identify_species_unknown(self):
        fossils = [
            type("Fossil", (), {"name": "кость"}),
            type("Fossil", (), {"name": "зуб"})
        ]
        result = self.modeler.identify_species(fossils)
        self.assertEqual(result, "🤔 Вид динозавра определить сложно.")

    def test_reconstruct_dinosaur_success(self):
        fossils = [
            type("Fossil", (), {"name": "рога"}),
            type("Fossil", (), {"name": "фрагменты черепа"}),
            type("Fossil", (), {"name": "клюв"})
        ]
        result = self.modeler.reconstruct_dinosaur(fossils)
        self.assertEqual(result, "✅ На основе ископаемых удалось реконструировать Трицератопс!")

class TestResearcher(unittest.TestCase):
    def setUp(self):
        """Настройка тестовой среды."""
        self.researcher = Researcher("Доктор Алан Грант", "палеонтология")
        self.dino1 = Dinosaur("Ти-рекс", "Tyrannosaurus rex", "Меловой период")
        self.dino2 = Dinosaur("Велоцираптор", "Velociraptor", "Меловой период")
        self.dinosaurs = {
            "Ти-рекс": self.dino1,
            "Велоцираптор": self.dino2
        }
        self.formation = GeologicalFormation("Хелл-Крик", 68, "rock", "USA")
        self.excavation = Excavation(self.formation)

    def test_analyze_excavation_no_fossils(self):
        """Тест анализа раскопок: ископаемые не найдены."""
        result = self.researcher.analyze_excavation(self.excavation)
        self.assertEqual(result, "🚜 В этом месте ничего не найдено.")

    @patch.object(EvolutionResearch, 'study_evolution', return_value="✅ Ти-рекс мог эволюционировать в Велоцираптор.")
    def test_study_evolution_success(self, mock_study):
        """Тест изучения эволюции: оба динозавра существуют."""
        result = self.researcher.study_evolution(self.dinosaurs, "Ти-рекс", "Велоцираптор")
        self.assertEqual(result, "✅ Ти-рекс мог эволюционировать в Велоцираптор.")

    def test_study_evolution_failure(self):
        """Тест изучения эволюции: один из динозавров отсутствует."""
        result = self.researcher.study_evolution(self.dinosaurs, "Ти-рекс", "Неизвестный")
        self.assertEqual(result, "❌ Неверный ввод динозавров.")

    def test_str_representation(self):
        """Тест строкового представления исследователя."""
        result = str(self.researcher)
        self.assertEqual(result, "🔬 Доктор Алан Грант – специалист в области палеонтология")

if __name__ == '__main__':
    unittest.main()