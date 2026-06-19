# Deteccao de Anomalias em Transacoes em Python
# Bootcamp Bradesco - GenAI, Dados & Cyber
# Autor: Nathan Da Silva Oliveira

import statistics


def detectar_anomalias(transacoes, limiar_zscore=2.0):
      if len(transacoes) < 2:
                return []
            valores = [t['valor'] for t in transacoes]
    media = statistics.mean(valores)
    desvio = statistics.stdev(valores)
    if desvio == 0:
              return []
          anomalias = []
    for t in transacoes:
              z_score = (t['valor'] - media) / desvio
              if abs(z_score) > limiar_zscore:
                            anomalias.append({**t, 'z_score': round(z_score, 2)})
                    return anomalias


def processar_extrato(linhas):
      transacoes = []
    for linha in linhas:
              partes = linha.strip().split(',')
        if len(partes) == 3:
                      try:
                                        transacoes.append({
                                                              'id': partes[0].strip(),
                                                              'valor': float(partes[1].strip()),
                                                              'tipo': partes[2].strip()
                                        })
except ValueError:
                pass
    return transacoes


def main():
      extrato_csv = [
                "TX001,150.00,PIX",
                "TX002,200.00,TED",
                "TX003,180.00,PIX",
                "TX004,5800.00,TED",
                "TX005,160.00,PIX",
                "TX006,190.00,TED",
                "TX007,170.00,PIX",
                "TX008,9200.00,TED",
                "TX009,145.00,PIX",
                "TX010,155.00,TED",
      ]
    transacoes = processar_extrato(extrato_csv)
    valores = [t['valor'] for t in transacoes]
    media = statistics.mean(valores)
    print(f"Total de transacoes: {len(transacoes)}")
    print(f"Valor medio: R$ {media:.2f}")
    anomalias = detectar_anomalias(transacoes)
    if anomalias:
              print(f"\nAnomalias detectadas ({len(anomalias)}):")
        for a in anomalias:
                      print(f"  [{a['id']}] R$ {a['valor']:.2f} ({a['tipo']}) Z-score: {a['z_score']}")
else:
        print("\nNenhuma anomalia detectada.")


if __name__ == "__main__":
      main()
