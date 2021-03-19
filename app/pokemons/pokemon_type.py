from app.pokemons.pokemon_server import PokemonServer


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

    def calculate_attack_multiplier(self, pokemon_types):
        data = PokemonServer.get_type_data(self._type)

        attack_multiplier = 1
        for pokemon_type in pokemon_types:
            if pokemon_type.type in data['double_damage_to']:
                attack_multiplier *= 2
            elif pokemon_type.type in data['half_damage_to']:
                attack_multiplier *= 0.5
            elif pokemon_type.type in data['no_damage_to']:
                attack_multiplier = 0
                break

        return attack_multiplier
