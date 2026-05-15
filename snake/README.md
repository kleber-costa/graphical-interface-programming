# Snake

Um jogo simples da cobrinha (Snake) implementado em Python usando Tkinter.

## Visão geral

Este projeto implementa uma interface gráfica para jogar Snake. A cobrinha se move em uma grade, cresce ao comer a comida e o jogo termina quando a cobrinha colide com as paredes ou com o próprio corpo.

## Requisitos

- Python 3.x
- Tkinter (geralmente incluído na instalação padrão do Python)

## Como executar

1. Abra um terminal na pasta `snake`.
2. Execute:

```bash
python snake.py
```

## Como jogar

- Use as setas do teclado para controlar a direção da cobrinha (↑ ↓ ← →).
- Cada vez que a cobrinha come a comida vermelha, a pontuação aumenta e a cobrinha cresce.
- O jogo termina se a cobrinha tocar uma das paredes ou colidir com seu próprio corpo.

## Estrutura do projeto

- `snake.py` - Implementação principal do jogo usando Tkinter.

## Observações

- A velocidade e o tamanho da grade podem ser ajustados através das constantes no início de `snake.py` (`WIDTH`, `HEIGHT`, `GRID_SIZE`, `SPEED`).
- O jogo é para um jogador (controle manual); não há IA implementada.
