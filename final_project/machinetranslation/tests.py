import unittest
from  translator import frenchToEnglish, englishToFrench
class TestStringMethods(unittest.TestCase):

    def test_null(self):
        self.assertEqual(frenchToEnglish(None),"")
        self.assertEqual(englishToFrench(None),"")

    def test_translation(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertEqual(englishToFrench("Hello"),"Bonjour")


if __name__ == '__main__':
    unittest.main()