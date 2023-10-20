import pandas as pd
import numpy as np
import datetime

# Carregue o arquivo de feriados brasileiros
feriados = pd.read_csv("feriados_brasil.csv", parse_dates=["data"])

# Função para calcular o número de horas úteis em um mês
def horas_uteis_mes(ano, mes):
    # Data inicial (dia 20 do mês anterior)
    data_inicial = pd.Timestamp(f"{ano}-{mes-1}-20")

    # Data final (dia 19 do mês atual)
    if mes == 12:
        data_final = pd.Timestamp(f"{ano+1}-01-19")
    else:
        data_final = pd.Timestamp(f"{ano}-{mes}-19")

    # Gere um intervalo de datas diárias
    datas = pd.date_range(data_inicial, data_final)

    # Filtrar feriados
    datas = datas[~datas.isin(feriados["data"])]

    # Filtrar fins de semana (sábado = 5, domingo = 6)
    datas = datas[datas.dayofweek < 5]

    # Calcular o número de horas úteis (considerando um dia de 8 horas)
    horas_uteis = len(datas) * 8

    return horas_uteis


def calculaValorMes(valorHora):
    # Get the current date
    current_date = datetime.date.today()
    ano = current_date.year
    mes = current_date.month
    horas = horas_uteis_mes(ano, mes)
    print(f"Horas úteis em {ano}-{mes}: {horas} horas - Serviço; R$ {valorHora * horas:,.0f}")

def calculaValorAnual(valorHora):
    current_date = datetime.date.today()
    ano = current_date.year
    mes = current_date.month
    total = 0
    month = 1
    while month <= 12:
        horas = horas_uteis_mes(ano, mes)
        total += horas * valorHora
        month += 1

    print(f"Total anual: R$ {total:,.0f}")

if __name__ == "__main__":
    valorHora = 110
    calculaValorMes(valorHora)
    calculaValorAnual(valorHora)

