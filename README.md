# Calculadora Simples em Python com Tkinter

Este é um projeto de uma calculadora básica desenvolvida em Python com interface gráfica utilizando Tkinter. O objetivo deste projeto foi aplicar conceitos de POO (Programação Orientada a Objetos), modularização e boas práticas de desenvolvimento, criando um código organizado e de fácil manutenção.

## Funcionalidades:
- Interface gráfica intuitiva e minimalista, semelhante a calculadoras físicas.
- Operações matemáticas básicas: adição (+), subtração (-), multiplicação (*), divisão (/).
- Botões para limpar o display (C) e apagar o último dígito (←).
- Cálculo do resultado ao pressionar "=".

## Tecnologias Utilizadas:
- Python 3
- Tkinter (para a interface gráfica)

## Estrutura do Projeto:
calculadora_python/  
│── src/  
│   │── calculadora.py  # Lógica da calculadora  
│   │── interface.py    # Interface gráfica com Tkinter  
│   │── main.py         # Ponto de entrada do programa  
│── img/  
│   │── icone_calculadora.ico  # Ícone da aplicação  

## Como Executar:
1.Clone este repositório:
`git clone https://github.com/seu-usuario/calculadora_python.git`

2. Acesse o diretório do projeto:
`cd calculadora_python/src`

3. Execute o programa:
`python main.py # ou `python3 main.py`, a depender do sistema operacional`

## Observações
- O projeto não requer bibliotecas externas, pois utiliza apenas módulos padrão do Python.
- Caso deseje, pode criar um ambiente virtual para isolar o projeto:
`python -m venv venv  
source venv/bin/activate  # No Linux/macOS  
venv\Scripts\activate  # No Windows`
