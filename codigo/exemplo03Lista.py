pTempo = ["Ensolarado", "Nublado", "Chuvoso", "Tempestade", "Ensolarado"]

print(pTempo)

PREVISAO_FELIZ = "Ensolarado"

for previsao in pTempo:
    if previsao == PREVISAO_FELIZ:
        print(f"Ótimo dia para passear!, previsão: {previsao}")
    else:
        print(f"Não esqueça do guarda-chuva!, previsão: {previsao}")