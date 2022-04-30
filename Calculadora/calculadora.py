class Calculadora:
    def soma(x, y):
        return x + y

    def subtracao(x, y):
        return x - y

    def multiplicacao(x, y):
        if(x == 0 or y == 0):
            return 0
        else:
            return x * y

    def divisao(x, y):
        if y == 0:
            print ("Divisão por Zero, indefinição!!")
            dz = True
            return dz
        else:
            return x / y

