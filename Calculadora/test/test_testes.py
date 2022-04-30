import Calculadora.calculadora as calc
import pytest


class Testes():
    def test_soma(self):
        assert calc.Calculadora.soma(1, 2) == 3

    def test_subtracao_com_string(self):
        with pytest.raises(TypeError):
            calc.Calculadora.soma(3, "2")

    def test_subtracao(self):
        assert calc.Calculadora.subtracao(9, 3) == 6

    def test_multiplicacao(self):
        assert calc.Calculadora.multiplicacao(6, 2) == 12

    def test_divisao(self):
        assert calc.Calculadora.divisao(10, 2) == 5

    def test_divisaoZero(self):
        assert calc.Calculadora.divisao(3, 0) == 0
