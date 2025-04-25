pTempo = ["Ensolarado", "Nublado", "Chuvoso", "Tempestade", "Ensolarado"]
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

diasEnsolarados = []
diasSemSol = []

for i, d in enumerate(pTempo):
    if pTempo[i] == "Ensolarado":
        diasEnsolarados.append(dias[i])
    else:
        diasSemSol.append(dias[i])

print(f"Dias ensolarados: {diasEnsolarados}")
print(f"Dias sem sol: {diasSemSol}")