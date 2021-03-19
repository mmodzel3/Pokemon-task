import unittest
from unittest import mock

from app.pokemons import PokemonType
from app.pokemons.pokemon_server import PokemonServer


class PokemonTypeTest(unittest.TestCase):
    def setUp(self):
        self._type = PokemonType('ice')

    def mock_server_get_type_data(self):
        return {'double_damage_to': ['fire'],
                'half_damage_to': ['water'],
                'no_damage_to': ['ice']}

    @mock.patch.object(PokemonServer, 'get_type_data', mock_server_get_type_data)
    def test_when_calculate_multiplier_for_double_damage_type_then_got_two(self):
        multiplier = self._type.calculate_attack_multiplier([PokemonType('fire')])

        self.assertEqual(2, multiplier)

    @mock.patch.object(PokemonServer, 'get_type_data', mock_server_get_type_data)
    def test_when_calculate_multiplier_for_half_damage_type_then_got_half(self):
        multiplier = self._type.calculate_attack_multiplier([PokemonType('water')])

        self.assertEqual(0.5, multiplier)

    @mock.patch.object(PokemonServer, 'get_type_data', mock_server_get_type_data)
    def test_when_calculate_multiplier_for_no_damage_type_then_got_zero(self):
        multiplier = self._type.calculate_attack_multiplier([PokemonType('ice')])

        self.assertEqual(0, multiplier)

    @mock.patch.object(PokemonServer, 'get_type_data', mock_server_get_type_data)
    def test_when_calculate_multiplier_for_multiple_types_then_got_correct_multiplier(self):
        multiplier = self._type.calculate_attack_multiplier([PokemonType('fire'), PokemonType('water')])

        self.assertEqual(1, multiplier)
