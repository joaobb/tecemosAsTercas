def infoAutomata(estados, estadoInicial, estadosAceitacao, transicao):
    print("estados:", statesModifieds(estados))
    print("inicial:", estadoInicial)
    print("aceita:", statesModifieds(estadosAceitacao))
    print("Transitions:\n", transitionsModifieds(transicao))

def myFilter(estados, estadosAceitacao):
    complemento = []
    for estado in estados:
        if(not (estado in estadosAceitacao)):
            complemento.append(estado)
    return complemento

def operationTransition(new_state, initial, transitions, final):
    new_transitions = {}
    transitions_final = transitions
    transition_newState = {new_state: {'e': [initial]}}

    #criando as transicoes dos estados de aceitacao para o antigo estado inicial
    for estado in final:
        transitions_final[estado].update({'e': [initial]})
    
    # unindo a nova transicao do novo estado criado com as transicoes ja existente
    new_transitions = dict(transition_newState, **transitions_final)

    return new_transitions

def myHelp():
    print("-i para operacao de interseccao, recebe dois arquivos referente aos automatos")
    print("-c para operacao de complemento, recebe um arquivo referente ao automato")
    print("-e para operacao de estrela, recebe um arquivo referente ao automato")
    print("-u para operacao de uniao, recebe dois arquivos referente aos automatos")
    print("-s para operacao do simulador, recebe dois parametros, o primeiro referente ao automato e o segundo referente a palavra")

def transitionsModifieds(transitions):
    saida = ''
    for keys in transitions:
        for second_keys in transitions[keys]:
            saida += keys + ' ' + transitions[keys][second_keys][0] + ' ' + second_keys + '\n' + ' '
    
    return saida

def statesModifieds(states):
    saida = ''
    lenght = len(states)
    for i in range(0, lenght):
        if ( i < lenght - 1):
            saida += states[i] + ', '
        else:
            saida += states[i]
    return saida