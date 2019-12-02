def infoAutomata(estados, estadoInicial, estadosAceitacao, transicao, afd=False):
    print("estados", ', '.join(estados))
    print("inicial", estadoInicial)
    print("aceita", ", ".join(estadosAceitacao))

    for fonte in transicao:
        for simbolo in transicao[fonte]:
            if afd:
                print(beatifyState(fonte), beatifyState(transicao[fonte][simbolo]), simbolo)
            else:
                for alvo in transicao[fonte][simbolo]:
                    print(beatifyState(fonte), beatifyState(alvo), simbolo)


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

    # criando as transicoes dos estados de aceitacao para o antigo estado inicial
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

# Retorna o power set da lista de estados recebidos.
def states_power_set(states):
    result = [[]]
    for x in states:
        result.extend([subset + [x] for subset in result])

    for state in range(len(result)):
        result[state] = tuple(result[state])
    return result

# Formata a string do estado recebido como parametro
def beatifyState(state):
    if type(state) == str:
        return state
    elif type(state) == list and len(state) == 1:
        return "".join(state)
    return "{" + (",".join(map(str,state))) + "}"

def get_epslon_closure(state, transitions):
    result = []
    current_states = []
    current_states += state
    end = 0

    while True:
        new_state = []

        for st in current_states:
            print(st)
            if "e" in transitions[st]:
                new_state += transitions[st]["e"]
                end += 1

        if not len(new_state):
            return beatifyState(set(result))
        
        result += new_state
        current_states = new_state

    