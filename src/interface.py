import tkinter as tk  # Importa a lib Tkinter (interfaces desktop em Python)
from calculadora import Calculadora  # Importa a classe responsavel pela logica do programa
import os  # Importa modulo responsavel por interacoes com o sistema operacional

# Cria a classe responsavel pela interface grafica do programa
class CalculadoraGUI:
    def __init__(self):  # Metodo construtor da classe
        self.janela = tk.Tk()  # Cria a janela
        self.janela.title("Calculadora")  # Titulo da janela
        self.janela.geometry("235x310")  # Dimensiona a janela (Largura x Altura)
        self.janela.resizable(False, False)  # Janela nao pode ser redimensionada pelo usuario

        # Obtem o caminho absoluto do icone da janela
        caminho_icone = os.path.abspath(os.path.join(os.path.dirname(__file__), "../img/icone_calculadora.ico"))
        
        # Tenta definir o icone da janela, caso o arquivo seja encontrado
        try:
            self.janela.iconbitmap(caminho_icone)
        except Exception as e:
            print(f"Erro! Nao foi possivel carregar o icone da janela. Codigo do erro: {e}\n")

        self.calculadora = Calculadora()  # Instancia responsavel pela logica

        # Cria e aplica frame responsavel pelo display da calculadora
        self.frame_display = tk.Frame(self.janela, height=50, bg="#A1B6A1")
        self.frame_display.pack(fill="both")

        # Cria e aplica label responsavel pelo display dentro do frame dele
        self.display = tk.Label(self.frame_display, text="", anchor="e", font=("Arial", 30), bg="#A1B6A1", fg="#1C1C1C", padx=10)
        self.display.pack(fill="both", expand=True)

        # Cria e aplica frame responsavel pelos botoes (teclado) da calculadora
        self.frame_botoes = tk.Frame(self.janela, bg="#2C2C2C")
        self.frame_botoes.pack(fill="both", expand=True)

        # Chama a funcao responsavel por criar e posicionar os botoes
        self.criar_botoes()
    
    # Metodo responsavel por atualizar o display da calculadora
    def atualizar_display(self):
        self.display.config(text=self.calculadora.expressao)

    # Metodo chamado ao clicar em um botao
    def clique_botao(self, valor):
        self.calculadora.adicionar(valor)
        self.atualizar_display()

    # Metodo que chama o metodo de calculo do resultado da expressao e o exibe
    def calcular_resultado(self):
        resultado = self.calculadora.calcular()
        self.display.config(text=resultado)
    
    # Reseta a calculadora
    def limpar_display(self):
        self.calculadora.limpar()
        self.atualizar_display()

    # Chama o metodo para apagar o ultimo digito da expressao e atualiza a tela
    def apagar_ultimo(self):
        self.calculadora.apagar_ultimo()
        self.atualizar_display()

    # Cria e posiciona os botoes da calculadora de forma iterativa
    def criar_botoes(self):
        """ Lista com o texto de cada botao, o comando a ser executado ao pressiona-lo
            e a sua posicao (linha e coluna) """
        botoes = [
            ("C", self.limpar_display, 0, 0), ("←", self.apagar_ultimo, 0, 1), ("/", self.clique_botao, 0, 2), ("*", self.clique_botao, 0, 3),
            ("7", self.clique_botao, 1, 0), ("8", self.clique_botao, 1, 1), ("9", self.clique_botao, 1, 2), ("-", self.clique_botao, 1, 3),
            ("4", self.clique_botao, 2, 0), ("5", self.clique_botao, 2, 1), ("6", self.clique_botao, 2, 2), ("+", self.clique_botao, 2, 3),
            ("1", self.clique_botao, 3, 0), ("2", self.clique_botao, 3, 1), ("3", self.clique_botao, 3, 2), ("=", self.calcular_resultado, 3, 3),
            ("0", self.clique_botao, 4, 0), (".", self.clique_botao, 4, 1)    
        ]

        # Itera sobre a lista criando e posicionando os botoes
        for texto, comando, linha, coluna in botoes:
            columnspan = 2 if texto == "=" else 1
            botao = tk.Button(self.frame_botoes, text=texto, font=("Arial", 14), bg="#4A4A4A", fg="#E4E7ED", width=5, height=2, command=lambda t=texto, c=comando: c(t) if c == self.clique_botao else c())
            botao.grid(row=linha, column=coluna, columnspan=columnspan, padx=2, pady=2, sticky="nsew")

        # Ajustes de posicionamento no frame dos botoes
        for i in range(4):
            self.frame_botoes.columnconfigure(i, weight=1)
        for i in range(5):
            self.frame_botoes.rowconfigure(i, weight=1)

    # Metodo para manter a janela na tela
    def iniciar(self):
        self.janela.mainloop()

# Instancia a classe da janela e chama o seu metodo para iniciar
def iniciar_interface():
    app = CalculadoraGUI()
    app.iniciar()
