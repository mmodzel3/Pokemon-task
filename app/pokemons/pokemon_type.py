import requests


class PokemonType:
    def __init__(self, type_name):
        self._type = type_name

    @property
    def type(self):
        return self._type

    def __str__(self):
        return str(self._type)

    def __repr__(self):
        return str(self._type)

    def _get_data(self):
        url = 'https://pokeapi.co/api/v2/type/{}'.format(self._type)

        response = requests.get(url)
        return response.json()
