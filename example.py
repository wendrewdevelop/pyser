# coding=utf-8

# ficheiro cfg
caminho = '/home/drew/Documentos/Estudos/Parser/CFG.txt'
# inicializar estrutura de dados
parametros = {}
# criar grupo geral para parâmetros sem grupo
parametros['geral'] = {}
# marcador para saber qual o grupo actual
grupo = 'geral'


with open(caminho, 'r') as cfg:
    for linha in cfg.readlines():
        # apagar espaços em branco no início e fim
        linha = linha.strip()
        # a linha é um comentário ou está vazia, passar à próxima
        if not linha or linha.startswith('#'):
            continue
        # criar grupo
        if linha.endswith(':'):
            grupo = linha.split(':')[0]
            parametros[grupo] = {}

print(parametros)
