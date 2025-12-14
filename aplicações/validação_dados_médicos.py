import re

dados_medicos = [
    {
        'idpaciente': 'P1001',
        'idade': 34,
        'sexo': 'Feminino',
        'diagnostico': 'Hypertension',
        'medicacoes': ['Lisinopril'],
        'id_ultimavisita': 'V2301',
    },
    {
        'idpaciente': 'p1002',
        'idade': 47,
        'sexo': 'masculino',
        'diagnostico': 'Type 2 Diabetes',
        'medicacoes': ['Metformin', 'Insulin'],
        'id_ultimavisita': 'v2302',
    },
    {
        'idpaciente': 'P1003',
        'idade': 29,
        'sexo': 'feminino',
        'diagnostico': 'Asthma',
        'medicacoes': ['Albuterol'],
        'id_ultimavisita': 'v2303',
    },
    {
        'idpaciente': 'p1004',
        'idade': 56,
        'sexo': 'Masculino',
        'diagnostico': 'Chronic Back Pain',
        'medicacoes': ['Ibuprofen', 'Physical Therapy'],
        'id_ultimavisita': 'V2304',
    }
]

def dados_invalidos(idpaciente, idade, sexo, diagnostico, medicacoes, id_ultimavisita):
    contrastes = {
        "idpaciente": isinstance(idpaciente, str) and re.fullmatch(r"p\d+", idpaciente, re.IGNORECASE),
        "idade": isinstance(idade, int) and idade >= 18,
        "sexo": isinstance(sexo, str) and sexo.lower() in ("masculino", "feminino"),
        "diagnostico": isinstance(diagnostico, str) or diagnostico is None,
        "medicacoes": isinstance(medicacoes, list) and all([isinstance(i, str) for i in medicacoes]),
        "id_ultimavisita": isinstance(id_ultimavisita, str) and re.fullmatch(r"v\d+", id_ultimavisita, re.IGNORECASE)
    }
    return [chave for chave, value in enumerate(contrastes.items()) if not value]

def validacao(data):
    if not isinstance(data, (list, tuple)):
        print("Formato inválido: passe uma lista ou tupla como parâmetro.")
        return False
    
    invalido = False
    keys_set = set(["idpaciente", "idade", "sexo", "diagnostico", "medicacoes", "id_ultimavisita"])

    for index, dic in enumerate(data):
        if not isinstance(dic, dict):
            print(f"Formato inválido: na posição {index} deve haver um dicionário.")
            invalido = True
            continue

        if set(dic.keys()) != keys_set:
            print(f"Formato inválido: {dic} na posição {index} tem chaves inválidas ou está faltando dados.")
            invalido = True
            continue

        for chave_invalida in dados_invalidos(**dic):
            print(f"Formato inválido '{chave_invalida}: {dic[chave_invalida]}' na posição {index}.")
            invalido = True
    
    if invalido:
        return False
    else:
        print("Formato válido!")
        return True

validacao(dados_medicos)
