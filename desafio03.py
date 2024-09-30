import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento = []
for dia in dados['faturamento']:
    if dia['valor'] > 0:
        faturamento.append(dia['valor'])

if faturamento:
    media_mensal = sum(faturamento) / len(faturamento)
else:
    media_mensal = 0

menor_faturamento = min(faturamento) if faturamento else 0
maior_faturamento = max(faturamento) if faturamento else 0

dias_acima_media = 0
for valor in faturamento:
    if valor > media_mensal:
        dias_acima_media += 1

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")