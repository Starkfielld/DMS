
def competicao(competidor,campeonato):
    atl = competidor
    nome = input("Digite o nome da competição: ")
    local = input("Digite o local da competição: ")
    dia = int(input("Digite o dia da competição: "))
    mes = int(input('Digite o mês da competição: '))
    ano = int(input('Digite o ano da competição: '))
    data = (f'{dia} - {mes} - {ano}')
    hora = int(input("Digite a hora da competição: "))
    mim = int(input('Digite o minuto da competição: '))
    horario = (f'{hora}:{mim}')
    campeonato[nome] = [local, data, horario]
    print("Competição cadastrada com sucesso!")
    print(campeonato)
    print(atl)

def competidor(atleta):
    option = input('Gostaria de cadastrar um competidor (s/n) ')
    while option.lower() == 's':
        cod = (input('Digite o código do atleta: '))
        nome = input("Digite o nome da competidor: ")
        idade = int(input("Digite a idade da competidor: "))
        altura = float(input("Digite a altura da competidor: "))
        peso = float(input("Digite o peso da competidor: "))
        atleta[cod] = [f'nome: {nome}',f'idade: {idade}',f'altura: {altura}',f'peso {peso}']
        print("Competidor cadastrado com sucesso!")
        print(atleta)
        option = input('Gostaria de cadastrar outro competidor ? (s/n) ')
    return atleta

def dardo(atleta, dardos):
    atl = atleta
    option = input('Gostaria de cadastrar os dardos de um competidor (s/n) ')
    while option.lower() == 's':
        cod = input("Digite o código do competidor: ")
        if cod in atl:
            distancia = float(input("Digite a distância do dardo nº1: "))
            distancia_2 = float(input("Digite a distância do dardo nº2: "))
            distancia_3 = float(input("Digite a distância do dardo nº3: "))
            if distancia > distancia_2 and distancia > distancia_3:
                dardos[cod] =[f'maior distância: {distancia}',atl[cod][0]]
            elif distancia_2 > distancia and distancia_2 > distancia_3:
                dardos[cod] =[f'maior distância: {distancia_2}',atl[cod][0]]
            elif distancia_3 > distancia and distancia_3 > distancia_2:
                dardos[cod] =[f'maior distância: {distancia_3}',atl[cod][0]]
        atl.update(dardos)
        option = input('Gostaria de cadastrar outro dardos de outro competidor  ? (s/n) ')
    print('competição encerrada')
    print(atl)
    ranking = []
    for i in sorted(atl, key = atl.get, reverse=True):
        ranking.append(atl[i][0])
    print(f'o ranking final é: {ranking}')        

def cem_metros(atleta, corrida):
    atl = atleta
    option = input('Gostaria de cadastrar o tempo de um competidor (s/n) ')
    while option.lower() == 's':
        cod = input("Digite o código do competidor: ")
        if cod in atl:
            tempo = float(input("Digite o tempo do competidor: "))
            corrida[cod]= [f'tempo: {tempo}',atl[cod][0]]
            
        atl.update(corrida)
        option = input('Gostaria de cadastrar tempo de outro competidor  ? (s/n) ')
    print('competição encerrada')
    print(atl)
    ranking = []
    for i in sorted(atl, key = atl.get):
        ranking.append(atl[i])
    print(f'o ranking final é: {ranking}')
    
    

def main():
    dardos = {}
    corrida = {}
    campeonato = {}
    atleta = {}
    competidor(atleta)
    competicao(atleta,campeonato)
    dardo(atleta, dardos)
    cem_metros(atleta, corrida)

dardos = {}
corrida = {}
campeonato = {}
atleta = {}
competidor(atleta)
dardo(atleta, dardos)
cem_metros(atleta,corrida)