# Aplicativo de orçamento - exibe gastos e conjunto percentual de gastos

class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
    
    def get_balance(self):
        saldo = 0
        for i in self.ledger:
            saldo += i["amount"]
        return saldo

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def __str__(self):
        result = f"{self.name:*^30}"
        for t in self.ledger:
            if len(t["description"]) > 23:
                result += f"\n{t['description'][:23]:<23}{t['amount']:>7.2f}"
            else:
                result += f"\n{t['description']:<23}{t['amount']:>7.2f}"
        result += f"\nTotal: {self.get_balance():.2f}"
        return result

def matriz_em_pe(matriz):
    n = len(matriz) # linhas
    m = len(matriz[0]) # colunas
    if n + m == 0:
        return []
    result = []
    for j in range(0, m):
        linha_result = []
        for i in range(0, n):
            linha_result.append(matriz[i][j])
        result.append(linha_result)
    return result

def create_spend_chart(categories):
    result = "Percentage spent by category\n"
    names = []
    saques = []
    grafico = [list("1" + " "*10), list("0987654321 "), list("0"*11), list("|"*11), list(" "*11)]
    n = len(categories)

    for category in categories:
        names.append(category.name)
        total_saque = 0
        for saque in category.ledger:
            if saque['amount'] < 0:
                total_saque += -saque['amount']
        saques.append(total_saque)
    total_gastos = sum(saques)

    for i in range(0, n):
        qtd = int((100*saques[i]/total_gastos)//10)
        grafico.append(list(" "*(10-qtd) + "o"*(qtd+1)))
        grafico.append(list(" "*11))
        grafico.append(list(" "*11))
    
    grafico = matriz_em_pe(grafico)
    for string in grafico:
        linha = "".join(string)
        result += f"{linha}\n"

    result += "    " + "-"*(1+3*n)

    maior_nome = 0
    for name in names:
        if len(name) > maior_nome:
            maior_nome = len(name)
    for i in range(0, n):
        while len(names[i]) < maior_nome:
            names[i] += " "

    back_string = [[" "]*maior_nome]*5
    for name in names:
        back_string.append(list(name))
        back_string.append(list(" "*maior_nome))
        back_string.append(list(" "*maior_nome))

    back_string = matriz_em_pe(back_string)
    for linha in back_string:
        string = "".join(linha)
        result += f"\n{string}"
    
    return result

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(5.50, "sugar")
clothing.withdraw(15.0, "coffee")
print(create_spend_chart([food, clothing]))
