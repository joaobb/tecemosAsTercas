import prog
import sys

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
        print("Initial: ", initial)
        print("Final: ", final)
        print("Transition: ", transitions)
        print(prog.wordParser(states, initial, final, transitions, word))
    
    elif (option.lower() == 't'):
        pass
    
    elif (option.lower() == 'u'):
        pass

    else:
        print ('Opcao invalida!')

main()
    
