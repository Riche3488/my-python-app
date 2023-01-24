from unittest import TestCase

import gender_converter


class Test(TestCase):
    def test_convert_gender_when_male(self):
        expected = "MALE"
        actual = gender_converter.convert_gender("M")

        self.assertEqual(actual, expected)

    def test_convert_gender_when_female(self):
        expected = "FEMALE"
        actual = gender_converter.convert_gender("F")

        self.assertEqual(actual, expected)
