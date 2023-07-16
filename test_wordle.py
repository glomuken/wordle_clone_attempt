import unittest
import wordle as worldle
from unittest.mock import patch
from io import StringIO

class TestWordle(unittest.TestCase):
    def test_text_flie(self):
        file=worldle.get_words()
        self.assertIn("Shush",file)
        self.assertIn("Alive",file)
    @patch("sys.stdin",StringIO("who\nif\nwhe4s\nwhere"))
    @patch("sys.stdout",new_callable=StringIO)
    def test_input(self,output):
        var=1
        worldle.get_word(var)
        self.assertEqual(output.getvalue().strip(),"Guess 1 : Your word should be 5 letters long\nGuess 1 : "+\
            "Your word should be 5 letters long\nGuess 1 : Please enter a word.\nGuess 1 :")
        
    def test_check(self):
        check=worldle.check_word("tooth","there")
        self.assertEqual(check,(False, ', t', ', e, r, e', ', h'))
    
