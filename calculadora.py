class Soma:

    def adicao(self, valor1, valor2):
        return f'O resultado da soma e {valor1 + valor2}'

class Subtracao:

    def subtracao(self, valor1, valor2):
        return f'O resultado da subtracao e {valor1 - valor2}'

class Multiplicacao:

    def multiplicacao(self, valor1, valor2):
        return f'O resultado da multiplicacao e {valor1 * valor2}'

class Divisao:

    def divisao(self, valor1, valor2):
        return f'O resultado da divisao e {valor1 / valor2}'


class Calculadora(Soma, Subtracao, Multiplicacao, Divisao):
    pass


