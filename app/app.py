from app.exceptions import InvalidInputException
from app.pokemons import PokemonType


def parse_input_to_attacking_pokemons(lines):
    attacking_pokemons = []

    for line in lines:
        pokemons = line.split("->")

        if len(pokemons) != 2:
            raise InvalidInputException("Invalid input - only allowed two attacking pokemons per line")

        attacking_pokemon_type = PokemonType(pokemons[0].strip())
        defencing_pokemon_types = [PokemonType(pokemon_type) for pokemon_type in pokemons[1].split()]

        attacking_pokemons.append((attacking_pokemon_type, defencing_pokemon_types))

    return attacking_pokemons


def get_input():
    lines = []
    while True:
        line = input()

        if line:
            lines.append(line)
        else:
            break

    return lines


def app():
    print('Task - Pokemon types')
    lines = get_input()

    attacking_pokemons = parse_input_to_attacking_pokemons(lines)

    for pokemons in attacking_pokemons:
        multiplier = pokemons[0].calculate_attack_multiplier(pokemons[1])
        print(str(multiplier) + 'x')
