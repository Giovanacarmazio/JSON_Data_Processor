#1
entries = response["hits"]["hits"]
ufs = []
for entry in entries:
    ufs.append(entry['_source']['estabelecimento_uf'])

print(set(ufs))
print(len(set(ufs)))

#2
entries = response["hits"]["hits"]
fabricantes = []
for entry in entries:
    fabricantes.append(entry['_source']['vacina_fabricante_nome'])

print(set(fabricantes))
print(len(set(fabricantes)))

#3
entries = response["hits"]["hits"]
sexo = {}
for entry in entries:
    sexo_valor = entry['_source']['paciente_enumSexoBiologico']
    if sexo_valor not in sexo:
        sexo[sexo_valor] = 1
    else:
        sexo[sexo_valor] += 1

print(sexo)
