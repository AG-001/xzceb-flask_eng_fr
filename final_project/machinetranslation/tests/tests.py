import unittest

from machinetranslator import translator
from ptranslator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test(self): 
        self.assertNotEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test(self): 
        self.assertNotEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()