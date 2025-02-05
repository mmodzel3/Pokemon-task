import requests


class PokemonServer:

    @classmethod
    def get_type_data(cls, type_name):
        data = cls._get_data_from_server(type_name)

        damage_relations = data['damage_relations']
        double_damage_to = [pokemon_type['name'] for pokemon_type in damage_relations['double_damage_to']]
        half_damage_to = [pokemon_type['name'] for pokemon_type in damage_relations['half_damage_to']]
        no_damage_to = [pokemon_type['name'] for pokemon_type in damage_relations['no_damage_to']]

        return {'double_damage_to': double_damage_to,
                'half_damage_to': half_damage_to,
                'no_damage_to': no_damage_to}

    @classmethod
    def _get_data_from_server(cls, type_name):
        url = 'https://pokeapi.co/api/v2/type/{}'.format(type_name)

        response = requests.get(url)
        return response.json()
