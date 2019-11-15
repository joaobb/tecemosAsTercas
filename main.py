import prog
import sys

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
    print("States: ", states_u)
    print("Initial: ", initial_u)
    print("Final: ", final_u)
    print("Transition: ", transitions_u)

def main():

    option = param1 = param2 = ''
    # Se tiver mais de um arg, eh entendido que o primeiro arg 
    # tratasse da opcao desejada.
    if (len(sys.argv) > 1):
        option = sys.argv[1]
    else:
        print ('Informe uma opcao de uso do programa.\n Use a opcao -h para obter ajuda.')
    
    # Casos que recebem a opcao desejada e dois parametros.
    if (len(sys.argv) > 3):
        param1 = sys.argv[2]
        param2 = sys.argv[3]
    
    # Casos que recebem apenas a opcao desejada e um parametro.
    elif (len(sys.argv) > 2):
        param1 = sys.argv[2]
    
    # Tira o menos e reconhece com Upper ou Lower case.
    option = option.split('-')[1]
    if (option.lower() == 'c'):
        pass
    
    elif (option.lower() == 'e'):
        pass
    
    elif (option.lower() == 'h'):
        pass

    elif (option.lower() == 'i'):
        pass
    
    elif (option.lower() == 's'):
        word = param2
        states, initial, final, transitions = prog.fileParser(param1)
        print("States: ", states)
        print(type(states))
        print("Initial: ", initial)
        print(type(initial))
        print("Final: ", final)
        print(type(final))
        print("Transition: ", transitions)
        print(type(transitions))
        print(prog.wordParser(states, initial, final, transitions, word))
    
    elif (option.lower() == 't'):
        pass
    
    elif (option.lower() == 'u'):
        union(param1, param2)

    else:
        print ('Opcao invalida!')

main()
    
