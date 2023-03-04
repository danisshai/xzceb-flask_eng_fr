import unittest
from  translator import french_to_english, english_to_french
class TestStringMethods(unittest.TestCase):

    def test_null(self):
        self.assertEqual(french_to_english(None),"no text provided")
        self.assertEqual(english_to_french(None),"no text provided")

    def test_translation(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(english_to_french("Hello"),"Bonjour")

if __name__ == '__main__':
    unittest.main()