def infoAutomata(estados, estadoInicial, estadosAceitacao, transicao):
    print("States: ", estados)
    print("Initial: ", estadoInicial)
    print("Final: ", estadosAceitacao)
    print("Transition: ", transicao)

def myFilter(estados, estadosAceitacao):
    complemento = []
    for estado in estados:
        if(not (estado in estadosAceitacao)):
            complemento.append(estado)
    return complemento

def myHelp():
    print("-i para operacao de interseccao, recebe dois arquivos referente aos automatos")
    print("-c para operacao de complemento, recebe um arquivo referente ao automato")
    print("-e para operacao de estrela, recebe um arquivo referente ao automato")
    print("-u para operacao de uniao, recebe dois arquivos referente aos automatos")
    print("-s para operacao do simulador, recebe dois parametros, o primeiro referente ao automato e o segundo referente a palavra")
    