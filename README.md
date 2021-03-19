# Pokemon - task
* [Task](#task)
* [Installation](#installation)
* [Input](#input)
* [Example](#example)
* [Language](#language)
* [Libraries](#libraries)

## Task
Using data from Pokemon API (pokeapi.co) calculate attack multiplier for specific Pokemon type against other types.

## Installation
pip install -r requirements.txt

## Input
Input as multiple lines of format (end of input - blank line):
[attacking_pokemon_type] -> [defencing_pokemon_type1] [defencing_pokemon_type2] ... [defencing_pokemon_typeN]

Output:
[Attack multiplier]x

## Example
fire -> grass\
fire -> ice grass\
\
2x\
2x

## Language
- Python

## Libraries
- requests
- unittest
