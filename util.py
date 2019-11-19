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