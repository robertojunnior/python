def busca_binaria(v, p, r, x):
    # condição de parada
    if p <= r:
        q = (p + r) // 2  # buscando o índice do meio do vetor
        if x > v[q]:
            return busca_binaria(v, q + 1, r, x)
        elif x < v[q]:
            return busca_binaria(v, p, q - 1, x)
        else:
            return q  # encontrado

    return -1  # não encontrado


vacas_ordenhadas = list(range(1, 5000))
vaca = 5001
posicao = busca_binaria(vacas_ordenhadas, 0, len(vacas_ordenhadas) - 1, vaca)

if posicao >= 0:
    print("A vaca %d foi ordenhada e se encontra na posição: %d." % (vaca, posicao))
else:
    print("A vaca NÃO foi ordenhada.")

print(vacas_ordenhadas)
