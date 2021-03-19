import unittest
import json
from unittest import mock

from app.pokemons import PokemonServer


class PokemonServerTest(unittest.TestCase):
    def mock_server_response(self):
        return json.loads("""
            {"damage_relations": {"double_damage_to": [{"name": "fire"}, {"name": "water"}],
                                "half_damage_to": [{"name": "ice"}],
                                "no_damage_to": [{"name": "grass"}]}}
        """)

    @mock.patch.object(PokemonServer, '_get_data_from_server', mock_server_response)
    def test_when_get_data_from_server_then_got_damage_relations_processed(self):
        data = PokemonServer.get_type_data("fire")

        self.assertEqual(2, len(data['double_damage_to']))
        self.assertEqual('fire', data['double_damage_to'][0])
        self.assertEqual('water', data['double_damage_to'][1])
        self.assertEqual(1, len(data['half_damage_to']))
        self.assertEqual('ice', data['half_damage_to'][0])
        self.assertEqual(1, len(data['no_damage_to']))
        self.assertEqual('grass', data['no_damage_to'][0])


