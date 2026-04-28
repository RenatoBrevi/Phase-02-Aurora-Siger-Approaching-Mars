# Cadastro dos módulos - criando uma função

def criar_modulos():
    modulos = [
        {
            "id": 1,
            "nome": "Segurança",
            "prioridade": 1,
            "combustivel": 92,
            "massa": 8500,
            "criatividade_carga": 4,
            "criticidade": "Crítica",
            "chegada_orbita": "08:00",
            "status": "Normal",
            "risco_pouso": "Médio",
            "integridade": 98,
            "dependecia": "Energia",
            "tempo_pouso": 18,
            "sensores_integros": True,
            "energia": 92,
            "temperatura": 24,
            "pressao": 101,
            "velocidade": 420,
            "angulo": 12
        },
        {
            "id": 2,
            "nome": "Defesa Contra Radiação",
            "prioridade": 6,
            "combustivel": 80,
            "massa": 10500,
            "criatividade_carga": 4,
            "criticidade": "Alta",
            "chegada_orbita": "08:50",
            "status": "Normal",
            "risco_pouso": "Médio",
            "integridade": 96,
            "dependecia": "Energia",
            "tempo_pouso": 22,
            "sensores_integros": True,
            "energia": 84,
            "temperatura": 23,
            "pressao": 100,
            "velocidade": 430,
            "angulo": 11
        },
        {
            "id": 3,
            "nome": "Controle Ambiental",
            "prioridade": 5,
            "combustivel": 82,
            "massa": 9300,
            "criatividade_carga": 5,
            "criticidade": "Crítica",
            "chegada_orbita": "08:40",
            "status": "Normal",
            "risco_pouso": "Médio",
            "integridade": 97,
            "dependecia": "Energia/Habitação",
            "tempo_pouso": 20,
            "sensores_integros": True,
            "energia": 86,
            "temperatura": 22,
            "pressao": 102,
            "velocidade": 410,
            "angulo": 12
        },
        {
            "id": 4,
            "nome": "Navegação",
            "prioridade": 2,
            "combustivel": 88,
            "massa": 7200,
            "criatividade_carga": 5,
            "criticidade": "Crítica",
            "chegada_orbita": "08:10",
            "status": "Normal",
            "risco_pouso": "Baixo",
            "integridade": 99,
            "dependecia": "Comunicação",
            "tempo_pouso": 16,
            "sensores_integros": True,
            "energia": 90,
            "temperatura": 21,
            "pressao": 101,
            "velocidade": 390,
            "angulo": 10
        },
        {
            "id": 5,
            "nome": "Comunicação",
            "prioridade": 3,
            "combustivel": 85,
            "massa": 6800,
            "criatividade_carga": 4,
            "criticidade": "Crítica",
            "chegada_orbita": "08:20",
            "status": "Normal",
            "risco_pouso": "Baixo",
            "integridade": 98,
            "dependecia": "Energia",
            "tempo_pouso": 15,
            "sensores_integros": True,
            "energia": 88,
            "temperatura": 22,
            "pressao": 100,
            "velocidade": 400,
            "angulo": 11
        },
        {
            "id": 6,
            "nome": "Armazenamento de Dados",
            "prioridade": 10,
            "combustivel": 74,
            "massa": 5600,
            "criatividade_carga": 4,
            "criticidade": "Média",
            "chegada_orbita": "09:30",
            "status": "Normal",
            "risco_pouso": "Baixo",
            "integridade": 95,
            "dependecia": "Energia/Comunicação",
            "tempo_pouso": 14,
            "sensores_integros": True,
            "energia": 78,
            "temperatura": 23,
            "pressao": 101,
            "velocidade": 420,
            "angulo": 12
        },
        {
            "id": 7,
            "nome": "Estação de Cozinha",
            "prioridade": 13,
            "combustivel": 68,
            "massa": 6300,
            "criatividade_carga": 3,
            "criticidade": "Baixa",
            "chegada_orbita": "10:00",
            "status": "Atenção",
            "risco_pouso": "Baixo",
            "integridade": 94,
            "dependecia": "Habitação/Água",
            "tempo_pouso": 17,
            "sensores_integros": True,
            "energia": 75,
            "temperatura": 24,
            "pressao": 100,
            "velocidade": 440,
            "angulo": 12
        },
        {
            "id": 8,
            "nome": "Laboratório Científico",
            "prioridade": 12,
            "combustivel": 70,
            "massa": 9800,
            "criatividade_carga": 5,
            "criticidade": "Média",
            "chegada_orbita": "09:50",
            "status": "Normal",
            "risco_pouso": "Médio",
            "integridade": 96,
            "dependecia": "Energia/Dados",
            "tempo_pouso": 21,
            "sensores_integros": True,
            "energia": 82,
            "temperatura": 23,
            "pressao": 101,
            "velocidade": 430,
            "angulo": 12
        },
        {
            "id": 9,
            "nome": "Suporte Médico",
            "prioridade": 8,
            "combustivel": 76,
            "massa": 7900,
            "criatividade_carga": 5,
            "criticidade": "Alta",
            "chegada_orbita": "09:10",
            "status": "Normal",
            "risco_pouso": "Médio",
            "integridade": 97,
            "dependecia": "Comunicação/Energia",
            "tempo_pouso": 18,
            "sensores_integros": True,
            "energia": 80,
            "temperatura": 22,
            "pressao": 100,
            "velocidade": 420,
            "angulo": 11,
        },
        {
            "id": 10,
            "nome": "Propulsão Auxiliar",
            "prioridade": 9,
            "combustivel": 95,
            "massa": 11200,
            "criatividade_carga": 4,
            "criticidade": "Alta",
            "chegada_orbita": "09:20",
            "status": "Normal",
            "risco_pouso": "Alto",
            "integridade": 96,
            "dependecia": "Navegação",
            "tempo_pouso": 24,
            "sensores_integros": True,
            "energia": 89,
            "temperatura": 26,
            "pressao": 102,
            "velocidade": 450,
            "angulo": 13
        },
        {
            "id": 11,
            "nome": "Habitação",
            "prioridade": 7,
            "combustivel": 78,
            "massa": 15000,
            "criatividade_carga": 4,
            "criticidade": "Alta",
            "chegada_orbita": "09:00",
            "status": "Normal",
            "risco_pouso": "Alto",
            "integridade": 97,
            "dependecia": "Energia/Controle Ambiental",
            "tempo_pouso": 26,
            "sensores_integros": True,
            "energia": 83,
            "temperatura": 22,
            "pressao": 101,
            "velocidade": 460,
            "angulo": 12
        },
        {
            "id": 12,
            "nome": "Energia",
            "prioridade": 4,
            "combustivel": 90,
            "massa": 12000,
            "criatividade_carga": 5,
            "criticidade":  "Crítica",
            "chegada_orbita": "08:30",
            "status": "Normal",
            "risco_pouso": "Alto",
            "integridade": 98,
            "dependecia": "Segurança",
            "tempo_pouso": 25,
            "sensores_integros": True,
            "energia": 95,
            "temperatura": 25,
            "pressao": 101,
            "velocidade": 450,
            "angulo": 12
        },
        {
            "id": 13,
            "nome": "Lógistica",
            "prioridade": 11,
            "combustivel": 72,
            "massa": 13500,
            "criatividade_carga": 3,
            "criticidade": "Média",
            "chegada_orbita": "09:40",
            "status": "Atenção",
            "risco_pouso": "Médio",
            "integridade": 93,
            "dependecia": "Habitação",
            "tempo_pouso": 23,
            "sensores_integros": True,
            "energia": 76,
            "temperatura": 24,
            "pressao": 100,
            "velocidade": 440,
            "angulo": 12
        },
    ]
    return modulos

# Setando os limites das condições críticas
limites = {
    "combustivel_minimo": 75,
    "energia_minima": 70,
    "temperatura_minima": 18,
    "temperatura_maxima": 35,
    "pressao_minima": 95,
    "pressao_maxima": 145,
    "velocidade_maxima": 500,
    "angulo_minimo": 8,
    "angulo_maximo": 15,
    "integridade_minima": 90
}

# Funções do algoritmo de busca 

def buscar_menor_combustivel(lista):
    if len(lista) == 0:
        return None 

    menor = lista[0]

    for modulo in lista: 
        if modulo["combustivel"] < menor ["combustivel"]:
            menor = modulo 

    return menor 

def buscar_maior_prioridade(lista): 
    if len(lista) == 0: 
        return None 

    # Quanto menor o número, maior será a prioridade 
    maior = lista[0]

    for modulo in lista: 
        if modulo["prioridade"] < maior["prioridade"]:
            maior = modulo 

    return maior 

def buscar_por_criticidade(lista, criticidade_desejada): 
    encontrados = [] 

    for modulo in lista:
        if modulo["criticidade"].lower() == criticidade_desejada.lower(): 
            encontrados.append(modulo) 

    return encontrados 

# Funções de algoritmos de ordenaçãoabs
def ordenar_por_prioridade(lista): 
    # Selection Sort 
    copia = lista[:]

    for i in range(len(copia)): 
        indice_menor = i 

        for j in range(i + 1, len(copia)): 
            if copia[j]["prioridade"] < copia[indice_menor]["prioridade"]:
                indice_menor = j 

        copia[i], copia[indice_menor] = copia[indice_menor], copia[i] 

    return copia

def ordenar_por_combustivel(lista):
    #BubbleSort  para organizar o maior combustível para o menor 
    copia = lista[:]

    for i in range(len(copia)):
        for j in range(0, len(copia) - 1 - i):
            if copia[j]["combustivel"] < copia[j + 1]["combustivel"]: 
                copia[j], copia[j + 1] = copia[j + 1], copia[j] 

    return copia 

# Utilizando o NOR da porta lógica 
# A porta NOR só retornara True quando as entradas forem False 
# Vai funcinar da seguinte forma:
# False = não há falha 
# True = há falha
def porta_nor(entradas):
    for entrada in entradas: 
        if entrada == True: 
            return False 

    return True 

# Lógica do s Circuitos AND + NOR 
# Avaliando condições de pouso 
def avaliar_regras_logicas(modulo, atmosfera_segura, area_livre): 
    C = modulo["combustivel"] >= limites["combustivel_minimo"]
    A = atmosfera_segura == True 
    L = area_livre == True 
    S = modulo["sensores_integros"] == True 
    E = modulo["energia"] >= limites["energia_minima"] 
    TEMP = limites["temperatura_minima"] <= modulo["temperatura"] <= limites["temperatura_maxima"]
    PRES = limites["pressao_minima"] <= modulo["pressao"] <= limites["pressao_maxima"]
    VEL = modulo["velocidade"] <= limites["velocidade_maxima"]
    ANG = limites["angulo_minimo"] <= modulo["angulo"] <= limites["angulo_maximo"]
    EST = modulo["integridade"] >= limites["integridade_minima"]

    condicoes = {
        "C": C,
        "A": A,
        "L": L,
        "S": S,
        "E": E,
        "TEMP": TEMP,
        "PRES": PRES,
        "VEL": VEL,
        "ANG": ANG,
        "EST": EST
    }

    # Bloco AND de autorização de pouso - todas as condições precisam ser verdadeiras
    bloco_autorizacao_and = (
        C and
        A and
        L and 
        S and 
        E and 
        TEMP and 
        PRES and 
        VEL and 
        ANG and 
        EST
    )

    # Bloco de falhas - cada falha será ao contrário da condição esperada 
    falhas = {
        "Falhas_C": not C,
        "Falhas_A": not A,
        "Falhas_L": not L,
        "Falhas_S": not S,
        "Falhas_E": not E,
        "Falhas_TEMP": not TEMP, 
        "Falhas_PRES": not PRES,
        "Falhas_VEL": not VEL,
        "Falhas_ANG": not ANG,
        "Falhas_EST": not EST,
    }

    # Entradas da porta NOR
    entradas_bloqueio = []

    for falha in falhas.values():
        entradas_bloqueio.append(falha) 

    # Se nenhuma falha existir, NOR retorna True,
    # Se qualquer falhar existir, NOR retorna False
    bloco_bloqueio_nor = porta_nor(entradas_bloqueio)

    # O pouso só é autorizado se AND = TRUE e NOR = TRUE
    saida_final = bloco_autorizacao_and and bloco_bloqueio_nor 

    falhas_detectadas = []

    for nome_falha, valor in falhas.items(): 
        if valor == True:
            falhas_detectadas.append(nome_falha)

    return saida_final, condicoes, falhas_detectadas, bloco_autorizacao_and, bloco_bloqueio_nor

# Simulando a fila de pouso

def simular_pouso(fila_pouso, horario_atual, atmosfera_segura, area_livre): 
    #Listas Auxiliares
    modulos_pousados = []
    modulos_em_espera = []
    modulos_em_alerta = [] 

    # Pilha de revisão
    pilha_revisao = []

    print("\n===== SIMULAÇÃO DE POUSO DA NAVE AURORA =====")

    while len(fila_pouso) > 0: 
        modulo = fila_pouso.pop(0) # A fila usa pop(0), para retirar o primeiro elemento
        print("\nMódulo analisado:", modulo["nome"])

        # Verificando se o módulo chegou à órbita
        if modulo["chegada_orbita"] > horario_atual:
            print("Resultado: EM ESPERA")
            print("Motivo: ainda não chegou à órbita no horário atual.")
        else:
            autorizado, condicoes, falhas, bloco_and, bloco_nor = avaliar_regras_logicas(
                modulo,
                atmosfera_segura,
                area_livre
            )

            # If do pouso autorizado
            if autorizado:
                modulos_pousados.append(modulo) 
                print("Resultado: POUSO AUTORIZADO")
                print("Bloco AND:", int(bloco_and), "| Bloco NOR:", int(bloco_nor))

            #ELIF do pouso bloqueado ou módulo em alerta
            elif len(falhas) > 0 or modulo["status"] == "Atenção": 
                modulos_em_alerta.append(modulo)
                pilha_revisao.append(modulo)
                print("Resultado: POUSO ADIADO/BLOQUEADO")
                print("Bloco AND:", int(bloco_and), "| Bloco NOR:", int(bloco_nor))
                print("Falhas detectadas:", ", ".join(falhas))

            #ELSE caso não se encaixe nos casos anteriores
            else:
                modulos_em_espera.append(modulo)
                print("Resultado: EM ESPERA")
                print("Motivo: aguardando nova verificação.")

        return modulos_pousados, modulos_em_espera, modulos_em_alerta, pilha_revisao
        

# Função auxiliar para mostrar os resultados
def mostrar_nomes(titulo, lista):
    print("\n", titulo)

    if len(lista) == 0:
        print("Nenhum módulo.")
    else: 
        for modulo in lista:
            print("-", modulo["nome"])

modulos = criar_modulos()

# Lista principal com todos os módulos cadastrados 
lista_modulos = modulos 

# Fila principal organizada por prioridade 
fila_principal = ordenar_por_prioridade(lista_modulos)

# Busca por características
menor_combustivel = buscar_menor_combustivel(lista_modulos)
maior_prioridade = buscar_maior_prioridade(lista_modulos)
modulos_criticos = buscar_por_criticidade(lista_modulos, "Crítica")

# Ordenação alternativa por combustível
fila_por_combustivel = ordenar_por_combustivel(lista_modulos)

print("Módulo com menor combustível:", menor_combustivel["nome"], "-", str(menor_combustivel["combustivel"]) + "%")
print("Módulo com maior prioridade:", maior_prioridade["nome"], "- prioridade", maior_prioridade["prioridade"])

print("\nMódulos com criticidade Crítica:")
for modulo in modulos_criticos:
    print("-", modulo["nome"])

print("\nFila principal organiada por prioridade: ")
for modulo in fila_principal:
    print(modulo["prioridade"], "-", modulo["nome"])

print("\nFila reorganizada por Combustível:")
for modulo in fila_por_combustivel: 
    print(modulo["combustivel"], "% -", modulo["nome"])

# Condições simuladas do ambiente externo 
horario_atual = "09:30"
atmosfera_segura = True 
area_livre = True 

# Simulação de Pouso
pousados, espera, alerta, revisao, = simular_pouso(
    fila_principal,
    horario_atual,
    atmosfera_segura,
    area_livre
)

# Resultados finais
mostrar_nomes("MÓDULOS POUSADOS:", pousados) 
mostrar_nomes("MÓDULOS EM ESPERA:", espera)
mostrar_nomes("MÓDULOS EM ALERTA:", alerta)

print("\nPILHA DE REVISÃO:")

if len(revisao) > 0:
    print("Topo da pilha:", revisao[-1]["nome"])
else:
    print("Nenhum módulo na pilha.")

