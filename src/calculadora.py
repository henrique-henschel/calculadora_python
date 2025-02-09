# Cria a classe responsavel pela logica do programa
class Calculadora:
    def __init__(self):
        self.expressao = ""  # Cria e inicializa atributo como string vazia

    # Metodo para concatenar valores e operacoes na expressao
    def adicionar(self, valor):
        self.expressao += str(valor)
    
    # Metodo responsavel por realizar os calculos (se a expressao for valida)
    def calcular(self):
        try:
            """ Verifica, valida (para impedir expressoes invalidas como '5-+3/*+4'
            e divisoes por zero) e calcula o resultado da expressao (caso ela seja
            valida) """
            resultado = eval(self.expressao)  # Metodo responsavel por verificar e calcular
            self.expressao = str(resultado)
            return resultado  
        except Exception:  # Caso a expressao seja invalida
            self.expressao = ""  # Reseta a expressao
            return "Erro"  # Exibira mensagem de erro no display
    
    # Metodo para resetar a expressao armazenada para uma string vazia (resetar a calculadora)
    def limpar(self):
        self.expressao = ""
    
    # Metodo para apagar o ultimo digito armazenado na expressao (corrigir)
    def apagar_ultimo(self):
        self.expressao = self.expressao[:-1]
