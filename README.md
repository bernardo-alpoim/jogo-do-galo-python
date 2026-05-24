# Jogo do Galo em Python 🎮

Este é um projeto desenvolvido de forma **totalmente individual e autónoma**, sem o recurso a ferramentas de Inteligência Artificial. O objetivo principal foi criar um jogo interativo  baseado em texto para ser executado diretamente na linha de comandos (terminal).

## 🚀 Algoritmo de Decisão (Lógica de Jogo)

O computador joga contra o utilizador através de um algoritmo de tomada de decisão inteligente

1. **Vitória Imediata:** O código analisa o tabuleiro para detetar se o computador tem duas peças em linha e fecha a jogada vitoriosa.
2. **Bloqueio Defensivo:** O algoritmo mapeia as jogadas do utilizador e, caso este tenha duas peças em linha, bloqueia o caminho para impedir a derrota.
3. **Ocupação Estratégica:** Prioriza a ocupação das posições geometricamente mais vantajosas (o centro do tabuleiro - posição 5 - e os cantos).
4. **Decisão de Contingência:** Utiliza a biblioteca `random` apenas quando não existem ameaças ou oportunidades prioritárias detetadas pela lógica principal.


## 📦 Como Executar o Projeto

1. Certifica-te de que tens o **Python 3** instalado no teu computador.
2. Transfere o ficheiro do script (`jogo_do_galo.py`).
3. Abre o terminal/linha de comandos na pasta onde guardaste o ficheiro.
4. Executa o seguinte comando:
   ```bash
   python jogo_do_galo.py
