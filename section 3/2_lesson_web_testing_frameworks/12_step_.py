import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Shoould be positive") # success

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Shoould be positive") # fail

    def test_abs3(self):
        self.assertEqual(abs(-42), 42, "Shoould be positive") # success

if __name__ == "__main__":
    unittest.main() # Запуск юнит тестов
    print("All tests passed!")
