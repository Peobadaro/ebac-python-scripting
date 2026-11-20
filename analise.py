"""Extrai a taxa CDI do site do Banco Central e gera um gráfico com os dados.

Combinação dos scripts ``extracao.py`` e ``visualizacao.py``.

Uso:
    python analise.py <nome-do-grafico>
"""

import json
import os
import time
from datetime import datetime
from random import random
from sys import argv

import matplotlib

matplotlib.use("Agg")  # gera a imagem sem precisar abrir uma janela

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import requests  # noqa: E402
import seaborn as sns  # noqa: E402

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados"
ARQUIVO_CSV = "./taxa-cdi.csv"
QUANTIDADE_EXTRACOES = 10


def extrair_taxa_cdi() -> float | None:
    """Captura a taxa CDI mais recente no site do BCB."""
    try:
        response = requests.get(url=URL, timeout=30)
        response.raise_for_status()
    except requests.HTTPError:
        print("Dado não encontrado, continuando.")
        return None
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    return float(json.loads(response.text)[-1]["valor"])


def salvar_dados(cdi: float | None) -> None:
    """Gera 10 registros (data, hora e taxa) no arquivo taxa-cdi.csv."""
    for _ in range(QUANTIDADE_EXTRACOES):
        data_e_hora = datetime.now()
        data = datetime.strftime(data_e_hora, "%Y/%m/%d")
        hora = datetime.strftime(data_e_hora, "%H:%M:%S")

        taxa = cdi + (random() - 0.5) if cdi is not None else None

        # Cria o arquivo com o cabeçalho caso ele ainda não exista
        if not os.path.exists(ARQUIVO_CSV):
            with open(file=ARQUIVO_CSV, mode="w", encoding="utf8") as fp:
                fp.write("data,hora,taxa\n")

        with open(file=ARQUIVO_CSV, mode="a", encoding="utf8") as fp:
            fp.write(f"{data},{hora},{taxa}\n")

        time.sleep(1)


def gerar_grafico(nome_grafico: str) -> None:
    """Lê o arquivo taxa-cdi.csv e salva o gráfico em <nome_grafico>.png."""
    df = pd.read_csv(ARQUIVO_CSV)

    grafico = sns.lineplot(x=df["hora"], y=df["taxa"])
    grafico.tick_params(axis="x", labelrotation=90)
    grafico.set_title("Taxa CDI")
    grafico.get_figure().tight_layout()
    grafico.get_figure().savefig(f"{nome_grafico}.png")
    plt.close(grafico.get_figure())


def main() -> None:
    if len(argv) < 2:
        print("Uso: python analise.py <nome-do-grafico>")
        raise SystemExit(1)

    nome_grafico = argv[1]

    cdi = extrair_taxa_cdi()
    salvar_dados(cdi)
    gerar_grafico(nome_grafico)

    print("Sucesso")


if __name__ == "__main__":
    main()
