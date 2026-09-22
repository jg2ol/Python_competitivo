from abc import ABC, abstractmethod

class Validador(ABC):
    @abstractmethod
    def validar(self):
        pass



class Email(Validador):
    def validar(self, email:str):
        # 1 @ - Letras Numeross & podeSímbolos - TLD encerra com pelo menos 2 letras
        if email.count('@') != 1: return False
        if email[0] == '@': return False
        if len(email[email.index('@')+1:]) < 2: return False
        return True


class Usuario(Validador):
    def validar(self, usuario:str):
        # 5 a 20 carac. - Letras minúsculas apenas
        if 20 < len(usuario) < 5: return False
        if usuario.lower() != usuario: return False
        return True


class Senha(Validador):
    def validar(self, senha:str):
        # pelo menos 8 carac. - 1 maiúscula - 1 minúscula - 1 símbolo
        if len(senha) < 8: return False
        aux = [False, False, False]
        for x in senha:
            if x.islower(): aux[0] = True
            if x.isupper(): aux[1] = True
            if x in ['@', '!', '?', ':', ';', '%', '$', '#']: aux[2] = True
        return all(aux)


def validar_dado(validador, valor:str):
    try:
        print(f"Valor: {valor} é válido? ", end="")
        print("SIM" if validador.validar(valor) else "NÃO")
    except Exception as e:
        print(f"Erro: {e}")
