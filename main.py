import prog
import sys
import util
from random import randint

# param_1: AFD
def complemento(param_1):
    states, initial, final, transitions = prog.fileParser(param_1)

    if prog.afn_checker(transitions):
        states, initial, final, transitions = prog.automataConverter(states, initial, final, transitions, False)

    # print(states, initial, final, transitions)

    states_c = states
    initial_c = initial
    final_c = util.myFilter(states, final)
    transitions_c = transitions
    print("O complemento do automato é: ")
    util.infoAutomata(states_c, initial_c, final_c, transitions_c, True)

# param_1: AFD
def star(param_1):
    states, initial, final, transitions = prog.fileParser(param_1)

    new_state = 'q0'
    states_e = [new_state] + states
    initial_e = new_state
    final_e = [new_state] + final
    transitions_e = util.operationTransition(new_state, initial, transitions, final)
    print("Novo automato pos operacao estrela: ")
    util.infoAutomata(states_e, initial_e, final_e, transitions_e)

# param_1: AFD1
# param_2: AFD2
def intersection(param_1, param_2):
    # Automato 1
    states_1, initial_1, final_1, transitions_1 = prog.fileParser(param_1, 1)
    # Automato 2
    states_2, initial_2, final_2, transitions_2 = prog.fileParser(param_2, 2)

    # A união dos automatos resulta na uniao de seus estados
    new_states = states_1 + states_2
    # O estado inicial do resultado da uniao eh o estado inicial do primeiro
    new_initial= initial_1
    # O estado de aceitacao do resultado da uniao eh o estado final do segunda
    new_final = final_2
    # As transicoes do novo automato gerado pela uniao eh constituida das transicoes de ambos,
    # com algumas alteracoes
    transitions_1.update(transitions_2)

    # Para esta operacao, eh adicionada uma transicao epslon partido do estado
    # de aceitacao do primeiro automato para o estado inicial do segundo automato,
    # este fato decorre de que por ser uma interseccao, ambos os automatos devem
    # aceitar a palavra inserida, logo, ambos os estados de aceitacao deverao ser
    # alcancados, um apos o outro.
    for qF in final_1:
        if not qF in transitions_1:
            transitions_1[qF] = {}    
        if not "e" in transitions_1[qF]:
            transitions_1[qF]['e'] = []
        transitions_1[qF]['e'].append(initial_2)

    print("Novo automato pos operacao de Interseccao: ")
    util.infoAutomata(new_states, new_initial, new_final, transitions_1)

# param_1: AFD
# param_2: word
def simulator(param_1, param_2):
    word = param_2
    states, initial, final, transitions = prog.fileParser(param_1)
    util.infoAutomata(states, initial, final, transitions)
    print(prog.wordParser(states, initial, final, transitions, word))


# Recebe um AFND e transforma para AFD
def transform(param_1):
    states, initial, final, transitions = prog.fileParser(param_1)
    print("Novo automato pos operacao de Conversao: ")
    if not prog.afn_checker(transitions):
        util.infoAutomata(states, initial, final, transitions)
    else:
        prog.automataConverter(states, initial, final, transitions)

# param_1: AFD1
# param_2: AFD2
def union(param_1, param_2):
    # Coletando informações sobre os dois automatos.
    states_1, initial_1, final_1, transitions_1 = prog.fileParser(param_1, 1)
    states_2, initial_2, final_2, transitions_2 = prog.fileParser(param_2, 2)

    # novo estado para unir os automatos. 
    new_state = 'q0'

    # As seguintes operacoes sao para o novo automato gerado pela UNIAO

    # estados
    states_u = [new_state] + states_1 + states_2

    # estado inicial
    initial_u = new_state

    # Estados finais
    final_u = final_1 + final_2

    # transicao do estado novo para os antigos estados iniciais
    transition_initial = {new_state: {'e': [initial_1, initial_2]}}
    # Concatenando as transicoes dos automatos
    # Esta forma de concatenar dicionarios eh mais eficiente
    transitions_u = dict(transition_initial, **transitions_1)
    # Unindo as transicoes
    transitions_u.update(transitions_2)
    
    print("Novo automato gerado pela Uniao:")
    util.infoAutomata(states_u, initial_u, final_u, transitions_u)
 

def main():

    option = arq_automata = arq_automata_2 = ''
    # Se tiver mais de um arg, eh entendido que o primeiro arg 
    # tratasse da opcao desejada.
    if (len(sys.argv) > 1):
        option = sys.argv[1]
    else:
        print ('Informe uma opcao de uso do programa.\n Use a opcao -h para obter ajuda.')
    
    # Casos que recebem a opcao desejada e dois parametros.
    if (len(sys.argv) > 3):
        arq_automata = sys.argv[2]
        arq_automata_2 = sys.argv[3]
    
    # Casos que recebem apenas a opcao desejada e um parametro.
    elif (len(sys.argv) > 2):
        arq_automata = sys.argv[2]
    
    # Tira o menos e reconhece com Upper ou Lower case.
    option = option.split('-')[1]
    if (option.lower() == 'c'):
        complemento(arq_automata)
    
    elif (option.lower() == 'e'):
        star(arq_automata)
    
    elif (option.lower() == 'h'):
        util.myHelp()

    elif (option.lower() == 'i'):
        intersection(arq_automata, arq_automata_2)
    
    elif (option.lower() == 's'):
        simulator(arq_automata, arq_automata_2)
        
    elif (option.lower() == 't'):
        transform(arq_automata)
    
    elif (option.lower() == 'u'):
        union(arq_automata, arq_automata_2)

    else:
        print ('Opcao invalida!')

main()
    
