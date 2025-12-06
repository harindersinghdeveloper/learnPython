import unittest
import cap

class TestCap(unittest.TestCase):
    def test_capitalize(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual('Python', result,)

    def test_multiple_words_capitalize(self):
        text = 'python is the best language'
        result = cap.cap_text(text)
        self.assertEqual('Python Is The Best Language', result)

if __name__ == '__main__':
    print("Running this file")
    unittest.main()
else:
    print("This file is not running directly")