# coding: utf-8

import re

# f=open("ex.txt", "r")

# contents = f.readlines()

states = initial = final = ""


def fileParser(fileName):
    f = open(fileName, "r")
    file_content = f.readlines()

    states = final = []
    initial = ""
    transitions = {}

    for line in file_content:
        line = line.replace(",", "")
        splitted = line.split()

        if line.startswith("estados"):
            states = splitted[1:]
            
        elif line.startswith("inicial"):
            initial = splitted[1]

        elif line.startswith("aceita"):
            final = splitted[1:]

        elif len(splitted) == 3 and splitted[0] in states and splitted[1] in states:
            current_state, target_state, next_state = splitted

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

def afn_checker(transitions):
    for transition in transitions:
        if "e" in transitions[transition]:
            return True;
        for letter in transitions[transition]: 
            if len(transitions[transition][letter]) > 1:
                return True;
    
    return False