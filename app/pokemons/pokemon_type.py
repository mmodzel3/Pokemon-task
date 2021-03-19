class PokemonType:
    def __init__(self, type_name):
        self._type = type_name

    @property
    def type(self):
        return self._type