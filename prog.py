# coding: utf-8

import re
import util

states = initial = final = ""

def fileParser(fileName, autoN = 0):
    f = open(fileName, "r")
    file_content = f.readlines()

    if not autoN: 
        autoN = ""
    else: 
        autoN = str(autoN)

    states = []
    final = []
    initial = ""
    transitions = {}

    for line in file_content:
        line = line.replace(",", "")
        splitted = line.split()

        if line.startswith("estados"):
            for state in splitted[1:]:
                states.append(state + autoN)
          
        elif line.startswith("inicial"):
            initial = splitted[1] + autoN

        elif line.startswith("aceita"):
            for state in splitted[1:]:
                final.append(state + autoN)

        elif len(splitted) == 3 and splitted[0]+autoN in states and splitted[1]+autoN in states:
            current_state, target_state, next_state = splitted
            current_state += autoN
            target_state += autoN

            if current_state not in transitions:
                transitions[current_state] = {}

            if next_state not in transitions[current_state]:
                transitions[current_state][next_state] = []

            transitions[current_state][next_state].append(target_state)

    return (states, initial, final, transitions)


def wordParser(states, initial, final, transitions, word):
    #Define o estado atual, como o estado inicial do automato
    currentStates = [initial]
    #Variável que terá serventia de atualizar a variavel acima após iteração
    newCurrentStates = []
    #Apresenta o estado da palavra como aceito ou não.
    accepted = "não "

    print("{} {: >25}".format("Estados", "Palavra"))

    #Iteração sobre a palavra
    for index in range(len(word)):
        #Iteração sobre todos os estados atuais (para que seja possível utilizar em uma AFN)
        for currentState in currentStates:    
            if (currentState in transitions) and (word[index] in transitions[currentState]):
                if 'e' in transitions[currentState]:
                    currentStates.extend(transitions[currentState]['e'])
                newCurrentStates.extend(transitions[currentState][word[index]])

        currentStates.sort()
        print("{} {:>25}".format(", ".join(currentStates), word[index:]))

        currentStates = newCurrentStates
        newCurrentStates = []

    print("{} {: >25}".format(", ".join(currentStates), 'e'))

    for states in currentStates:
        if states in final and accepted != "":
            accepted = ""

    return "\nA palavra {}foi aceita".format(accepted)

# Verifica se o automato eh um afn de acordo com as transicoes recebidas como parametro
def afn_checker(transitions):
    for transition in transitions:
        if "e" in transitions[transition]:
            return True
        for letter in transitions[transition]: 
            if len(transitions[transition][letter]) > 1:
                return True
    
    return False

def automataConverter(states, initial, final, transitions):
    # Power set dos estados
    states_power_set = util.states_power_set(states)

    transitions["Ø"] = {"0": "Ø", "1": "Ø"}

    # Para cada estado no power set de estados
    for ps_state in states_power_set:

        # Se este estado nao tiver nenhuma transicao no automato,
        # esta sera criada
        if (len(ps_state) > 1 and not(ps_state in transitions) and ps_state) or (len(ps_state) == 1 and (ps_state[0] not in transitions)):
            # Criar um novo slot na estutura de transicoes para um estado unico
            if len(ps_state) == 1:
                transitions[ps_state[0]] = {}

            # Cria um novo slot na estrutura de transicoes para estados complexos
            else:
                transitions[ps_state] = {}

            # Para cada sub-estado (A) no estado composto (A, B)
            for state in ps_state:
                # Para cada simbolo que gere uma transicao neste estado
                for symbol in transitions[state]:

                    # Cria um slot para a transicao do novo estado com os simbolos que nao estao presentes neste 
                    if not symbol in transitions[ps_state]:
                        transitions[ps_state][symbol] = []

                    # Realizamos a uniao das transocoes dos sub-estados geradores do estado
                    transitions[ps_state][symbol] += transitions[state][symbol]

    
    # Setando os estados de aceitacao do AFD como todos que possuem em sua composicao
    # ao menos um dos estados de aceitacao da AFN original
    for transition in transitions:
        if set(transition) & set(final):
            final.append(util.beatifyState(transition))

    # Define os estados do automato como todos os alcancaveis, limpando assim a saida do programa
    afd_states = get_reachable_states(initial, transitions)

    # Adiciona o estado lixo aos estados do AFD 
    afd_states.add(("Ø",))

    # Define as transicoes do afd como todas as que sao possiveis de serem percorridas.
    afd_transitions = clear_states(transitions, get_reachable_states(initial, transitions))

    # Define o estado inicial do afd, como todos os estados alcançaveis por transicoes epslon,
    # o chamado eplson closure
    afd_initial = util.get_epslon_closure(initial, transitions)

    # Formatando os estados textualmente, para que fique na forma {a,b} ou a
    for st in afd_states.copy():
        if len(st) == 1:
            afd_states.remove(st)
            afd_states.add("".join(map(str,st)))
        else:
            afd_states.remove(st)
            afd_states.add(util.beatifyState(st))

    # Retira todos os estados finais inalcancaveis
    afd_final = [st for st in final if st in afd_states]

    util.infoAutomata(afd_states, afd_initial, afd_final, afd_transitions, True)


def get_reachable_states(state, transitions):
    current_states = []
    reachable_states = []
    
    current_states += state   
    reachable_states += state

    while True:
        new_current_states = []

        for cs in set(current_states): 
            for st in transitions[cs]:
                reachable_states.append(tuple(transitions[cs][st]))
                new_current_states += transitions[cs][st]

        if set(new_current_states) == set(current_states): break    
        current_states = new_current_states

    reachable_states = set(reachable_states)
    
    return reachable_states

def clear_states(transitions, reachable_states):
    clean_transitions = transitions.copy()

    for st in transitions:
        if not tuple(st) in reachable_states:
            del clean_transitions[st]

    return clean_transitions