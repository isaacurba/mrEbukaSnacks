from unittest import TestCase

import simple_arithmetic_app

class TesArithmeticApp(TestCase):

    def test_to_generate_two_random_subtraction_numbers(self):
        first_number, second_number = simple_arithmetic_app.random_subtraction_number()
        error_message = "The second number is greater than the first number"
        self.assertGreaterEqual(first_number, second_number, error_message)

    def test_to_check_there_are_no_negative_numbers(self):
        first_number, second_number = simple_arithmetic_app.random_subtraction_number()
        result = first_number - second_number
        self.assertGreaterEqual(result, 0)

    def test_to_get
