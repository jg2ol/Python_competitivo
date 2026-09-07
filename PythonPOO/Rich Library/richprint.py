# Instalando a rich no python:
# pip install rich

from rich import print # substitui o print padrão
# melhora cores e adiciona emojis

# [cor]Texto[/cor] -> [cor]Texto[/]
print("Hello, [bold red on white]World[/]! :earth_americas:")

from rich import inspect
# Melhora muito a exibição de docs do Python
print(int.__doc__)
inspect(int, all=True)
