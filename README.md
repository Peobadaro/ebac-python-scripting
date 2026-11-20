# Python: Scripting – Exercício Módulo 9 (EBAC)

Extração da taxa CDI da API do Banco Central e geração de um gráfico, rodando o Python **na própria máquina**, pelo terminal.

## Arquivos

| Arquivo | O que faz |
|---|---|
| `extracao.py` | Script de extração (original do exercício): grava 10 registros da taxa CDI em `taxa-cdi.csv` |
| `visualizacao.py` | Script de visualização (original do exercício): gera o gráfico a partir do `taxa-cdi.csv` |
| **`analise.py`** | **Combinação dos dois scripts**, organizada em funções (PEP8) |
| `Profissao_Analista_de_dados_M9_Exercicio.ipynb` | Caderno do exercício com o código combinado na última célula |
| `taxa-cdi.csv` / `grafico-cdi.png` | Resultado de uma execução do `analise.py` |

## Como rodar

```shell
python -V
pip -V
pip install -r requirements.txt

python analise.py grafico-cdi
```

No final ficam o arquivo `taxa-cdi.csv` e a imagem `grafico-cdi.png`.
