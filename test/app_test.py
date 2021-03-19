import unittest

from app.app import parse_input_to_attacking_pokemons
from app.exceptions import InvalidInputException


class AppTest(unittest.TestCase):

    def test_when_parse_valid_input_then_got_correct_attacking_pokemons_with_types(self):
        lines = [' fire -> grass ',
                 ' fighting -> ice rock ']

        attacking_pokemons = parse_input_to_attacking_pokemons(lines)

        self.assertEqual('fire', attacking_pokemons[0][0].type)
        self.assertEqual(1, len(attacking_pokemons[0][1]))
        self.assertEqual('grass', attacking_pokemons[0][1][0].type)
        self.assertEqual('fighting', attacking_pokemons[1][0].type)
        self.assertEqual(2, len(attacking_pokemons[1][1]))
        self.assertEqual('ice', attacking_pokemons[1][1][0].type)
        self.assertEqual('rock', attacking_pokemons[1][1][1].type)

    def test_when_parse_invalid_input_with_more_than_two_pokemons_then_got_invalid_input_exception(self):
        lines = [' fire -> grass -> ice',
                 ' fighting -> ice rock ']

        with self.assertRaises(InvalidInputException) as context:
            parse_input_to_attacking_pokemons(lines)

    def test_when_parse_invalid_input_with_less_than_two_pokemons_then_got_invalid_input_exception(self):
        lines = [' fire ',
                 ' fighting -> ice rock ']

        with self.assertRaises(InvalidInputException) as context:
            parse_input_to_attacking_pokemons(lines)
