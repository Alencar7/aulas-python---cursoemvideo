pessoas = {'nome':'Adriano', 'sexo':'M', 'idade': 23}
#aspas duplas pra definir
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#keys
print(pessoas.keys())
#values
print(pessoas.values())
#items
print(pessoas.items())

for k in pessoas.keys():
    print(f'{k}')

for k in pessoas.values():
    print(f'{k}')

for k, v in pessoas.keys():
    print(f'{k} = {v}')

#apagar
# del pessoas['sexo']

#mudar o valor
pessoas['nome'] = 'Alencar'

#add valor
pessoas['peso'] = 96.5

#add dicionarios in listas
brasil = []
estado1 = {'uf':'Pernambuco', 'sigla':'PE'}
estado2 = {'uf': 'Acre','sigla':'AC'}

print(brasil[0]['uf']) #PE

#METODO PARA COPIAR = .COPY() = LEMBRA O [:] EM LISTAS
estado = {}
pais = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    pais.append(estado.copy())
print(pais)

for e in pais:
    for z, m in e.items():
        print(f'O campo {z} tem valor {m}')




























