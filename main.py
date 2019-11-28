import prog
import sys
import util


# param_1: AFD
def complemento(param_1):
    states, initial, final, transitions = prog.fileParser(param_1)

    states_c = states
    initial_c = initial
    final_c = util.myFilter(states, final)
    transitions_c = transitions
    print("O complemento do automato é: ")
    util.infoAutomata(states_c, initial_c, final_c, transitions_c)

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
    states, initial, final, transitions = prog.fileParser(param_1)
    states_2, initial_2, final_2, transitions_2 = prog.fileParser(param_2)

    # Inicializando as variaveis
    states_i, initial_i, final_i, transitions_i = [], '', [], {}

    initial_i = initial + initial_2

    # Seta os valores dos estados e estado final
    for estado_afd1 in states:
        for estado_afd2 in states_2:
            states_i.append(estado_afd1 + estado_afd2)
            if(estado_afd1 in final and estado_afd2 in final_2):
                final_i.append(estado_afd1 + estado_afd2)

    # Setar as transicoes
    for keys_1 in transitions:
        for keys_2 in transitions_2:
            new_state = keys_1+keys_2
            transitions_i[new_state] = {
                '1':[transitions[keys_1]['1'][0]+ transitions_2[keys_2]['1'][0]],
                '0':[transitions[keys_1]['0'][0]+ transitions_2[keys_2]['0'][0]]
            }

    print("Novo automato pos operacao de Interseccao: ")
    util.infoAutomata(states_i, initial_i, final_i, transitions_i)





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
    print(prog.afn_checker(transitions))
    pass

# param_1: AFD1
# param_2: AFD2
def union(param_1, param_2):
    # Coletando informações sobre os dois automatos.
    states, initial, final, transitions = prog.fileParser(param_1)
    states_2, initial_2, final_2, transitions_2 = prog.fileParser(param_2)

    # novo estado para unir os automatos. 
    # Talvez precise fazer uma verificacao antes para nao repetir o nome de um possivel estado ja existente
    # No caso, criaria uma nome randomico
    new_state = 'q0'

    # As seguintes operacoes sao para o novo automato gerado pela UNIAO

    # estados
    states_u = [new_state] + states + states_2

    # estado inicial
    initial_u = new_state

    # Estados finais
    final_u = final + final_2

    # transicao do estado novo para os antigos estados iniciais
    transition_initial = {new_state: {'e': [initial, initial_2]}}
    # Concatenando as transicoes dos automatos
    # Esta forma de concatenar dicionarios eh mais eficiente
    transitions_u = dict(transition_initial, **transitions)
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
    
