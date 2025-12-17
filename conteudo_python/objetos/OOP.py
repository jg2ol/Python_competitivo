# OOP --> metodos de programação que restrigem o acesso aos dados dos objetos

class Wallet:
   def __init__(self, balance):
       self.__balance = balance # dessa forma não se há acesso direto à 'balance' (é usado somente internamente)
       # se fosse prefixado com um underscore, acessar o valor fora da classe deve gerar bugs

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount

   def withdraw(self, amount):
       if 0 < amount <= self._balance:
           self.__balance -= amount
