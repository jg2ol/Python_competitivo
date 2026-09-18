from hashlib import sha256
# biblioteca p/ criptografia de strings
# sha256 -> algoritmo utilizado
# encode("utf-8") -> codifica caracteres especiais (como ç e á)
# hexdigest() -> retorna a criptografia em hexadecimal (16 dígitos) [64 caracteres]

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        else:
            raise ValueError("A senha não pode ser vazia.")

    def validar(self, chave):
        return sha256(chave.encode("utf-8")).hexdigest() == self.__hash
