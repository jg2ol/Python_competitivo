# Canadense, eh?, fácil
# link: https://neps.academy/br/exercise/2339

frase = input()
palavras = frase.split()

if palavras[len(palavras) - 1] == "eh?":
    print("Canadian!")
else:
    print("Imposter!")