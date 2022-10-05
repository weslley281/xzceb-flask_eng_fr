import unittest
from translator import french_to_english, english_to_french

class TestTranslatorModule(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
    def test_englishToFrenchNot(self):
        self.assertNotEqual(english_to_french("Hello"), "Bonjr")

    def test_frenchToEnglishNot(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Helo")

if __name__ == '__main__':
    unittest.main()